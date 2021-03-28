import json
from matplotlib import pyplot as plt


def read_from_json(path):
    with open(path) as f:
        data = json.load(f)
    info = {
        benchmark['extra_info']['func']: {}
        for benchmark in data['benchmarks']
        }
    for benchmark in data['benchmarks']:
        func = benchmark['extra_info']['func']
        size = benchmark['extra_info']['size']
        time = benchmark['stats']['median']
        info[func][size] = time
    return info


def create_chart(info):
    fig, axes = plt.subplots(nrows=len(info))
    for sortingAlgorithm, ax in zip(info, axes):
        sizes = []
        times = []
        for size in info[sortingAlgorithm]:
            sizes.append(size)
            times.append(info[sortingAlgorithm][size] * 10**3)
        ax.plot(sizes, times)
        ax.set_title(sortingAlgorithm)
        ax.set_xlabel('Number of words')
        ax.set_ylabel('Time [ms]')


if __name__ == '__main__':
    plt.style.use('seaborn')
    info = read_from_json('lab2/.benchmarks/sortingTime.json')
    create_chart(info)
    plt.tight_layout()
    plt.show()
