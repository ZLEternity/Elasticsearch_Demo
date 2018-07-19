import random
import string
from util.commands import *
import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk,scan

def main():
    real_name_headers = ['Adam', 'Sr.', 'Bayes']

    # generate random names

    dates = [str(date) for date in generate_date_range(numdays=10)]

    data_num = 1000000

    random_names = [random_name for random_name in random_name_generator(data_num)]

    random_messages = [' '.join([word_generator() for k in range(6)]) for i in range(data_num)]

    random_dates = [random.choice(dates) for i in range(data_num)]

    random_tweet_jsons = [get_tweet_json(username=random_names[i], postdate=random_dates[i], message=random_messages[i])
                          for i in range(data_num)]

    data_num = 10000

    real_names = [(random.choice(real_name_headers) + ' ' + ' '.join([word_generator() for i in range(2)])) for k in
                  range(data_num)]

    random_messages = [' '.join([word_generator() for k in range(6)]) for i in range(data_num)]

    random_dates = [random.choice(dates) for i in range(data_num)]

    real_tweet_jsons = [get_tweet_json(username=real_names[i], postdate=random_dates[i], message=random_messages[i]) for
                        i in range(data_num)]


    random_batch_jsons = [generate_batch_data(index='twitter',type='tweet',single_data=json_data) for json_data in random_tweet_jsons]
    real_batch_jsons = [generate_batch_data(index='twitter',type='tweet',single_data=json_data) for json_data in real_tweet_jsons]

    es = Elasticsearch()

    bulk(es,random_batch_jsons)
    bulk(es,real_batch_jsons)

if __name__ == '__main__':
    main()
