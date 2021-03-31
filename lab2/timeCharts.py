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


def create_chart(info, fig, axes):
    for axl in axes:
        for sortingAlgorithm, ax in zip(info, axl):
            sizes = []
            times = []
            for size in info[sortingAlgorithm]:
                sizes.append(size)
                times.append(info[sortingAlgorithm][size] * 10**3)
            ax.plot(sizes, times)
            ax.set_title(sortingAlgorithm)
            ax.set_xlabel('Number of words')
            ax.set_ylabel('Time [ms]')
        for counter in range(len(axl)):
            del info[next(iter(info))]


if __name__ == '__main__':
    plt.style.use('seaborn')
    info = read_from_json('lab2/.benchmarks/sortingTime.json')
    fig, axes = plt.subplots(nrows=2, ncols=2)
    create_chart(info, fig, axes)
    plt.tight_layout()
    fig.savefig('lab2/charts.png')
