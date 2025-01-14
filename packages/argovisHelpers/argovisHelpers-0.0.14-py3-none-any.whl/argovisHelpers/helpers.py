import requests, datetime, copy, time, re, area, math

# networking helpers

def argofetch(route, options={}, apikey='', apiroot='https://argovis-api.colorado.edu/', suggestedLatency=0, verbose=False):
    # GET <apiroot>/<route>?<options> with <apikey> in the header.
    # raises on anything other than success or a 404.

    o = copy.deepcopy(options)
    for option in ['polygon', 'multipolygon']:
        if option in options:
            options[option] = str(options[option])

    dl = requests.get(apiroot + route, params = options, headers={'x-argokey': apikey})
    statuscode = dl.status_code
    if verbose:
        print(dl.url)
    dl = dl.json()

    if statuscode==429:
        # user exceeded API limit, extract suggested wait and delay times, and try again
        wait = dl['delay'][0]
        latency = dl['delay'][1]
        time.sleep(wait*1.1)
        return argofetch(route, options=o, apikey=apikey, apiroot=apiroot, suggestedLatency=latency, verbose=verbose)

    if statuscode!=404 and statuscode!=200:
        if statuscode == 413:
            print('The temporospatial extent of your request is enormous! Consider using the `query` helper in this package to split it up into more manageable chunks.')
        elif statuscode >= 500:
            print("Argovis' servers experienced an error. Please try your request again, and email argovis@colorado.edu if this keeps happening; please include the full details of the the request you made so we can help address.")
        raise Exception(statuscode)

    if (statuscode==404) or (type(dl[0]) is dict and 'code' in dl[0] and dl[0]['code']==404):
        return [], suggestedLatency

    return dl, suggestedLatency

def query(route, options={}, apikey='', apiroot='https://argovis-api.colorado.edu/', verbose=False):
    # middleware function between the user and a call to argofetch to make sure individual requests are reasonably scoped and timed.
    r = re.sub('^/', '', route)
    r = re.sub('/$', '', r)

    data_routes = ['argo', 'cchdo', 'drifters', 'tc', 'argotrajectories', 'grids/rg09', 'grids/kg21', 'grids/glodap' 'timeseries/noaasst', 'timeseries/copernicussla', 'timeseries/ccmpwind']
    
    scoped_parameters = {
        'argo': ['id','platform'],
        'cchdo': ['id', 'woceline', 'cchdo_cruise'],
        'drifters': ['id', 'wmo', 'platform'],
        'tc': ['id', 'name'],
        'argotrajectories': ['id', 'platform'],
        'grids/rg09': ['id'],
        'grids/kg21': ['id'],
        'grids/glodap': ['id'],
        'timeseries/noaasst': ['id'],
        'timeseries/copernicussla': ['id'],
        'timeseries/ccmpwind': ['id']
    }
    
    earliest_records = {
        'argo': parsetime("1997-07-27T20:26:20.002Z"),
        'cchdo': parsetime("1972-07-23T09:11:00.000Z"),
        'drifters': parsetime("1987-10-01T13:00:00.000Z"),
        'tc': parsetime("1851-06-24T00:00:00.000Z"),
        'argotrajectories': parsetime("2001-01-03T22:46:33.000Z"),
        'grids/rg09': parsetime("2004-01-14T00:00:00.000Z"),
        'grids/kg21': parsetime("2005-01-14T00:00:00.000Z"),
        'grids/glodap': parsetime("0001-01-01T00:00:00.000Z"),
        'timeseries/noaasst': parsetime("1989-12-30T00:00:00.000Z"),
        'timeseries/copernicussla': parsetime("1993-01-02T00:00:00Z"),
        'timeseries/ccmpwind': parsetime("1993-01-02T00:00:00Z")
    }

    last_records = {
        'argo': datetime.datetime.now(),
        'cchdo': parsetime("2023-03-10T17:48:00.000Z"),
        'drifters': parsetime("2020-07-01T23:00:00.000Z"),
        'tc': parsetime("2020-12-26T12:00:00.000Z"),
        'argotrajectories': parsetime("2021-01-02T01:13:26.000Z"),
        'grids/rg09': parsetime("2022-05-16T00:00:00.000Z"),
        'grids/kg21': parsetime("2020-12-16T00:00:00.000Z"),
        'grids/glodap': parsetime("0001-01-02T00:00:00.000Z"),
        'timeseries/noaasst': parsetime("2023-01-30T00:00:00.000Z"),
        'timeseries/copernicussla': parsetime("2022-08-01T00:00:00.000Z"),
        'timeseries/ccmpwind': parsetime("1993-12-31T00:00:00Z")
    }

    if r in data_routes:
        # these are potentially large requests that might need to be sliced up

        ## if a data query carries a scoped parameter, no need to slice up:
        if r in scoped_parameters and not set(scoped_parameters[r]).isdisjoint(options.keys()):
            return argofetch(route, options=options, apikey=apikey, apiroot=apiroot, verbose=verbose)[0]

        ## slice up in time bins:
        start = None
        end = None
        if 'startDate' in options:
            start = parsetime(options['startDate'])
        else:
            start = earliest_records[r]
        if 'endDate' in options:
            end = parsetime(options['endDate'])
        else:
            end = last_records[r]

        ### determine appropriate bin size
        maxbulk = 1000000 # should be <= maxbulk used in generating an API 413
        timestep = 30 # days

        if 'polygon' in options:
            extent = area.area({'type':'Polygon','coordinates':[ options['polygon'] ]}) / 13000 / 1000000 # poly area in units of 13000 sq. km. blocks
            timestep = min(400, math.floor(maxbulk / extent))
        elif 'multipolygon' in options:
            extents = [area.area({'type':'Polygon','coordinates':[x]}) / 13000 / 1000000 for x in options['multipolygon']]
            extent = min(extents)
            timestep = min(400,math.floor(maxbulk / extent))

        delta = datetime.timedelta(days=timestep)
        times = [start]
        while times[-1] + delta < end:
            times.append(times[-1]+delta)
        times.append(end)
        times = [parsetime(x) for x in times]
        results = []
        ops = copy.deepcopy(options)
        delay = 0
        for i in range(len(times)-1):
            ops['startDate'] = times[i]
            ops['endDate'] = times[i+1]
            increment = argofetch(route, options=ops, apikey=apikey, apiroot=apiroot, suggestedLatency=delay, verbose=verbose)
            results += increment[0]
            delay = increment[1]
            time.sleep(increment[1]*0.8) # assume the synchronous request is supplying at least some of delay
        return results

    else:
        return argofetch(route, options=options, apikey=apikey, apiroot=apiroot, verbose=verbose)[0]

# data munging helpers

def data_inflate(data_doc, metadata_doc=None):
    # given a single JSON <data_doc> downloaded from one of the standard data routes,
    # return the data document with the data key reinflated to per-level dictionaries.

    data = data_doc['data']
    data_info = find_key('data_info', data_doc, metadata_doc)

    d = zip(*data) # per-variable becomes per-level 
    return [{data_info[0][i]: v for i,v in enumerate(level)} for level in d]

def find_key(key, data_doc, metadata_doc):
    # some metadata keys, like data_info, may appear on either data or metadata documents,
    # and if they appear on both, data_doc takes precedence.
    # given the pair, find the correct key assignment.

    if key in data_doc:
        return data_doc[key]
    else:
        if metadata_doc is None:
            raise Exception(f"Please provide metadata document _id {data_doc['metadata']}")
        if '_id' in metadata_doc and 'metadata' in data_doc and metadata_doc['_id'] not in data_doc['metadata']:
            raise Exception(f"Data document doesn't match metadata document. Data document needs metadata document _id {data_doc['metadata']}, but got {metadata_doc['_id']}")

        return metadata_doc[key]

def parsetime(time):
    # time can be either an argopy-compliant datestring, or a datetime object; 
    # returns the opposite.

    if type(time) is str:
        if '.' not in time:
            time = time.replace('Z', '.000Z')
        return datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
    elif type(time) is datetime.datetime:
        return time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    else:
        raise ValueError(time)

def units_inflate(data_doc, metadata_doc=None):
    # similar to data_inflate, but for units

    data_info = find_key('data_info', data_doc, metadata_doc)
    uindex = data_info[1].index('units')

    return {data_info[0][i]: data_info[2][i][uindex] for i in range(len(data_info[0]))}



