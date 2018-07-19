from util.constants import *
import requests
import random
import string
import datetime


def get_tweet_json(username, postdate, message):
    return {'name': username, 'postdate': postdate, 'message': message}


def generate_date_range(base=None, numdays=10):
    if base is None:
        base = datetime.datetime.today()
    for x in range(numdays):
        yield base - datetime.timedelta(days=x)


def word_generator(size=6, chars=string.lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def random_name_generator(data_num=10):
    for i in range(data_num):
        yield ' '.join(word_generator() for k in range(3))


def real_name_generator(data_num=10, real_name_prefix=['Adam', 'Sr.', 'Bayes']):
    for i in range(data_num):
        yield random.choice(real_name_prefix) + ' ' + ' '.join(word_generator() for k in range(2))


def get_cluster_url(host=HOST, port=PORT):
    return 'http://%s:%s' % (host, port)


def show_indexes(host=HOST, port=PORT):
    res = requests.get(get_cluster_url(host, port) + '/_cat/indices?v')
    return res.content


def fuzzy_query(index=None, query=None):
    full_query = {'query': {'fuzzy': query}}
    res = requests.get(get_cluster_url() + '/%s/_search' % index, json=full_query)
    return res.content


def query(index=None, query=None, method=None):
    full_query = {'query': {method: query}}
    res = requests.get(get_cluster_url() + '/%s/_search' % index, json=full_query)
    return res.content


def generate_batch_data(index=None, id=None, type='doc', single_data=None):
    output = {}
    if id is not None:
        output['_id'] = id
    output['_type'] = type
    output['_source'] = single_data
    output['_index'] = index
    return output


def main():
    while True:
        print 'show indexes:1'

        cmd = raw_input('input command:')

        cmds = cmd.split(' ')
        if len(cmds) == 3:
            index = cmds[0]
            i_from = int(cmds[1])
            i_to = int(cmds[2])
        try:
            cmd = int(cmd)
        except Exception as e:
            continue

        if cmd == 1:
            print show_indexes()
        if cmd == 0:
            break


if __name__ == '__main__':
    main()
