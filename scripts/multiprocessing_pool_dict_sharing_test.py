def print_res(url, json_data, proc_num=None, return_dict=None):
    import requests
    import json
    res = requests.get(url, json=json_data)

    response_json = json.loads(res.content)

    if proc_num is not None and return_dict is not None:
        return_dict[proc_num] = response_json


def main():
    from multiprocessing import Pool, Manager
    manager = Manager()
    return_dict = None
    return_dict = manager.dict()

    query_json = {
        "query": {
            "match": {
                "name": "teso"
            }
        }
    }
    from util.commands import get_cluster_url
    query_url = get_cluster_url() + '/b/_search?size=30'

    print 'testing query:%s' % query_json
    print 'query_url:%s' % query_url
    import time
    query_time = 1000
    t1 = time.time()

    p = Pool()

    for i in range(query_time):
        p.apply_async(print_res, args=[query_url, query_json, i, return_dict, ])

    p.close()
    p.join()
    t2 = time.time()
    print t2 - t1
    print return_dict[0]['hits']['total']


if __name__ == '__main__':
    main()
