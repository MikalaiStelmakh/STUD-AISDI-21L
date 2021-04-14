import json
from matplotlib import pyplot as plt


def read_from_json(path):
    with open(path) as f:
        data = json.load(f)
    info = {
        benchmark['extra_info']['function']: {}
        for benchmark in data['benchmarks']
        }
    for function in ['insertTime', 'searchTime', 'deleteTime']:
        info[function] = {
            benchmark['extra_info']['tree']: {}
            for benchmark in data['benchmarks']
        }
    for benchmark in data['benchmarks']:
        func = benchmark['extra_info']['function']
        size = benchmark['extra_info']['size']
        tree = benchmark['extra_info']['tree']
        time = benchmark['stats']['median']
        info[func][tree][size] = time
    return info


def createCharts():
    pass


if __name__ == '__main__':
    print(read_from_json('lab3/.benchmarks/data.json'))

