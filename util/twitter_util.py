import random
import string
from util.commands import *
import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, scan

_name_prefix_list = ['James','Arthur','Smith','Jinks','Marvel','DC','Dr.','Sr.']
_date_range = [str(datetime.datetime.today() - datetime.timedelta(days=x)) for x in range(10)]

def word_generator(chars=string.lowercase,length=6):
    return ''.join(random.choice(chars) for i in range(length))


def tweet_generator(username_prefixs=_name_prefix_list, data_range=_date_range, data_num=100):

    random_names = [random_name for random_name in random_name_generator(username_prefixs,data_num)]

    random_messages = [' '.join([word_generator() for k in range(6)]) for i in range(data_num)]

    random_dates = [random.choice(data_range) for i in range(data_num)]

    random_tweet_jsons = [get_tweet_json(username=random_names[i], postdate=random_dates[i], message=random_messages[i])
                          for i in range(data_num)]

    return random_tweet_jsons


def test():
    print word_generator()
    for json in tweet_generator():
        print json

if __name__ == '__main__':
    test()