import random
import string
from util.commands import *
import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan, bulk

_name_prefix_list = ['James', 'Arthur', 'Smith', 'Jinks', 'Marvel', 'DC', 'Dr.', 'Sr.']
_date_range = [str(datetime.datetime.today() - datetime.timedelta(days=x)) for x in range(10)]


def word_generator(chars=string.lowercase, length=6):
    return ''.join(random.choice(chars) for i in range(length))


def tweet_generator(username_prefixs=_name_prefix_list, data_range=_date_range, data_num=100):
    random_names = [random_name for random_name in random_name_generator(username_prefixs, data_num)]

    random_messages = [' '.join([word_generator() for k in range(6)]) for i in range(data_num)]

    random_dates = [random.choice(data_range) for i in range(data_num)]

    random_tweet_jsons = [get_tweet_json(username=random_names[i], postdate=random_dates[i], message=random_messages[i])
                          for i in range(data_num)]

    return random_tweet_jsons


def test():
    print word_generator()
    for json in tweet_generator():
        print json


def _data_generate_and_insert():
    true_prefix = ['Adam', 'Hinton', 'A.Ng', 'Sheldon', 'Len']
    true_tweets = tweet_generator(true_prefix,data_num=1000000)
    true_batch_json = [generate_batch_data(single_data=true_tweet,index='twitter',type='tweet') for true_tweet in true_tweets]
    es = Elasticsearch()
    for i in range(100):
        bulk(es, true_batch_json)
    exit(0)

    tot = 0
    for tweet in true_tweets:
        if tot % 2 == 0:
            tweet['username'] = 'qwq qaq qwq'
        else:
            tweet['username'] = 'qaq qwq qaq '
    true_batch_json = [generate_batch_data(single_data=true_tweet,index='twitter',type='tweet') for true_tweet in true_tweets]
    bulk(es, true_batch_json)



if __name__ == '__main__':
    _data_generate_and_insert()
