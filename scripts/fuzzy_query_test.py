from performance_test import *


# generate some titles from dictionary

def generate_titles_from_dict(n_titles=10, dict=None):
    titles = [' '.join(random.choice(dict) for _ in range(3)) for i in range(n_titles)]
    return titles


def main():
    from elasticsearch import Elasticsearch
    from elasticsearch.helpers import bulk, scan

    from util.commands import fuzzy_query

    true_headers = ['ada', 'alg', 'argo', 'unique', 'St.']

    tot = 0
    import time

    t1 = time.time()
    for hit in scan(es, query={"query": {"prefix": {"name": "adi"}}}, index='brands'):
        print hit
        tot += 1
        if tot == 3:
            break
    t2 = time.time()
    print t2 - t1
    print tot

    return

    dict = ['output', 'Sr', 'Adidas', 'Nike', 'Noke', 'Nake', 'Adadas', 'Adivon', 'King', 'Burger']
    titles = generate_titles_from_dict(1000000, dict)

    datas = [{'name': title} for title in titles]

    brand_batch_data = [generate_batch_data(index='brands', single_data=data) for data in datas]
    # print brand_batch_data[0]
    bulk(es, brand_batch_data)
    # test_batch_scan_time(index='brands',display=True)


if __name__ == '__main__':
    main()
