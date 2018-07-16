import requests
from util.constants import *
import grequests
import time
import requests

"""
Demo command:

curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
    "name": "John Doe"
}
'
"""


def put_data(json_data, id):
    r = requests.put(url='http://%s:%s/customer/_doc/%s?pretty' % (HOST, PORT, id), json=json_data)
    print r.content


def test_post():
    data = {'name': 'Junk Dog'}
    tasks = [grequests.post(url='http://%s:%s/customer/_doc/%s?pretty' % (HOST, PORT, id), json=data) for id in
             range(10000)]
    t1 = time.time()
    res = grequests.map(tasks, size=100)
    t2 = time.time()
    print t2 - t1


def _generate_get_url(id, index):
    return 'http://%s:%s/%s/_doc/%s?pretty' % (HOST, PORT, index, id)


def test_get():
    tasks = [grequests.get(url=_generate_get_url(id,'customer')) for id in range(10000)]
    t1 = time.time()
    res = grequests.map(tasks, size=100)
    for r in res:
        print r.content
    t2 = time.time()
    print t2 - t1


if __name__ == '__main__':
    # test_post()
    test_get()
