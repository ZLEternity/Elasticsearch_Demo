import grequests
import requests
from basic_commands.post_data import *
from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk
from util.commands import *
from multiprocessing import Pool

es = Elasticsearch()

_responses = []


count = 0
tot = 0



def print_res(url, json):


    res = requests.get(url, json=json)
    # _responses.append(res)


def multi_processing_query_test():
    query_json = {
        "query": {
            "fuzzy": {
                "name": "a.ng"
            }
        }
    }

    query_url = get_cluster_url() + '/twitter/tweet/_search?size=30'

    t1 = time.time()
    p = Pool()

    test_time = 10000

    for i in range(test_time):
        p.apply_async(print_res, args=[query_url, query_json, ])

    p.close()
    p.join()
    t2 = time.time()
    print t2 - t1


def generate_batch_data(index=None, id=None, type='doc', single_data=None):
    output = {}
    if id is not None:
        output['_id'] = id
    output['_type'] = type
    output['_source'] = single_data
    output['_index'] = index
    return output


def grequests_post_test(index=None):
    data = {'name': 'Junk Dog'}
    tasks = [grequests.post(url=generate_post_by_id_url('customer', id), json=data) for id in
             range(10000)]
    t1 = time.time()
    res = grequests.map(tasks, size=100)
    t2 = time.time()
    print t2 - t1


def grequests_get_test(index=None):
    tasks = [grequests.get(url=generate_get_by_id_url(id, 'customer')) for id in range(10000)]
    t1 = time.time()
    res = grequests.map(tasks, size=100)
    # for r in res:
    # print r.content
    t2 = time.time()
    print t2 - t1


def multi_processing_get_test(index=None, test_time=None, datas=None):
    from multiprocessing import Pool
    p = Pool()
    t1 = time.time()
    for id in range(test_time):
        url = generate_get_by_id_url(id, index)
        p.apply_async(requests.get, args=(url,))
    p.close()
    p.join()
    t2 = time.time()
    print t2 - t1


def multi_processing_post_test(index=None, datas=None):
    from multiprocessing import Pool
    p = Pool()
    t1 = time.time()
    for id in range(len(datas)):
        url = generate_get_by_id_url(id, index)
        p.apply_async(requests.post, args=(url, None, datas[id],))
    p.close()
    p.join()
    t2 = time.time()
    print t2 - t1


def post_test(index=None, data=None):
    url = generate_post_url('customer')
    data = {'name': 'Zero'}
    res = requests.post(url=url, json=data)
    import json
    print 'id:%s' % json.loads(res.content)['_id']
    print res.content


import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def data_generation(index='merchant_detail', data_number=1000000):
    for i in range(data_number):
        yield {
            '_id': str(i),
            '_type': 'doc',
            '_index': index,
            '_doc': {'merchant': id_generator(), 'content': 'no' * 10}
        }


def test_batch_data_insert_time(datas=None):
    print 'begin batch data insert...'
    from elasticsearch.helpers import scan, bulk
    import time
    t1 = time.time()
    if datas is None:
        datas = data_generation()
    bulk(es, datas)
    t2 = time.time()
    print 'batch data insert done,time cost:%f' % (t2 - t1)


def test_batch_scan_time(index=None, display=False):
    print 'begin batch data scan...'
    from elasticsearch.helpers import scan, bulk
    t1 = time.time()
    tot = 0
    for hit in scan(es, index=index):
        tot += 1
        if display:
            print hit
    print tot
    t2 = time.time()
    print 'batch data scan done,time cost:%f' % (t2 - t1)


def batch_data_put(datas):
    for i in range(len(datas)):
        datas[i]['index'] = {'_id': str(i)}
    return datas


def gendata():
    mywords = ['foo', 'bar', 'baz']
    for word in mywords:
        yield {'_type': 'doc',
               "_index": "mywords",
               "doc": {"word": word},
               }


def generate_test_data(index=None, data_number=None):
    data = [
        {'_id': str(i), '_index': index, '_type': 'doc', 'doc': {'merchant': id_generator(), 'content': 'no' * 10}}
        for i in range(data_number)]
    return data


def main():
    # generate 100w merchant data
    # datas = generate_test_data('merchant',1000000)

    # test_batch_data_insert_time(datas)
    # test_batch_scan_time('merchant')

    # datas = generate_test_data('books',10000)
    # multi_processing_post_test('book',datas) # too slow
    multi_processing_query_test()


def generate_random_merchant_info():
    data = {"account_number": 18, "balance": 4180, "firstname": "Dale", "lastname": "Adams", "age": 33, "gender": "M",
            "address": "467 Hutchinson Court", "employer": "Boink", "email": "daleadams@boink.com", "city": "Orick",
            "state": "MD"}
    return data


if __name__ == '__main__':
    # test_post()
    # multi_processing_get_test()
    # grequests_get_test()
    # post_test()
    # datas = data_generation(data_number=10)
    main()
