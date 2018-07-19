#!/home/qinglinzhang/anaconda3/envs/esearch/bin/python

import argparse
from util.commands import *
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--index')
    parser.add_argument('--id')
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-d', '--delete', action='store_true')
    parser.add_argument('-s', '--show', action='store_true')
    parser.add_argument('-p', '--port')
    parser.add_argument('--host')
    parser.add_argument('--data')
    args = parser.parse_args()

    if args.show:
        if args.index is None:
            print show_indexes()
        query_url = get_cluster_url() + '/' + args.index + '/_search'
        query_data = {}
        if args.all:
            query_data['query'] = {}
            query_data['match_all'] = {}
        requests.get(query_url,json=query_data)

    if args.delete:
        if args.index is None:
            url = get_cluster_url() + '/*'
            res = requests.delete(url)
            print res.content


if __name__ == '__main__':
    main()
