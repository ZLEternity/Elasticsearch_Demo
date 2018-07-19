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


def generate_get_by_id_url(id, index):
    return 'http://%s:%s/%s/_doc/%s?pretty' % (HOST, PORT, index, str(id))


def generate_post_url(index):
    return 'http://%s:%s/%s/_doc?pretty' % (HOST, PORT, index)


def generate_post_by_id_url(index, id):
    return 'http://%s:%s/%s/_doc/%s?pretty' % (HOST, PORT, index, str(id))



