from util.commands import *
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def _generate_batch_datas(index, data_types, data_numbers):
    batch_data = []

    for type_index in range(len(data_types)):
        data_type = data_types[type_index]
        data_number = data_numbers[type_index]
        for i in range(data_number):
            batch_data.append(generate_batch_data(index=index,single_data=data_type))

    return batch_data


def main():
    index_a_number = 10 * 10000
    index_b_number = 100 * 10000

    # index_a_number = 100
    # index_b_number = 100

    data_types = []

    test_data = {'name': 'test'}
    data_types.append(test_data)
    teso_data = {'name': 'teso'}
    data_types.append(teso_data)
    test_a_data = {'name': 'test a'}
    data_types.append(test_a_data)
    teso_a_data = {'name': 'teso a'}
    data_types.append(teso_a_data)
    test_string_data = {'name': 'test_string'}
    data_types.append(test_string_data)

    none_data = {'name': word_generator()}

    index_a_data_numbers = [index_a_number / 10 for i in range(5)]
    index_a_data_numbers.append(index_a_number / 5 * 4)

    index_b_data_numbers = [index_b_number / 10 for i in range(5)]
    index_b_data_numbers.append(index_b_number / 5 * 4)

    a_batch_data = _generate_batch_datas(index='a',data_types=data_types,data_numbers=index_a_data_numbers)
    b_batch_data = _generate_batch_datas(index='b',data_types=data_types,data_numbers=index_b_data_numbers)

    es = Elasticsearch()
    bulk(es,a_batch_data)
    bulk(es,b_batch_data)

if __name__ == '__main__':
    main()