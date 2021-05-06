import json
from matplotlib import pyplot as plt


def read_from_json(path):
    with open(path) as f:
        data = json.load(f)
    info = {
        benchmark['extra_info']['function']: {}
        for benchmark in data['benchmarks']
        }
    for benchmark in data['benchmarks']:
        func = benchmark['extra_info']['function']
        size = benchmark['extra_info']['size']
        time = benchmark['stats']['median']
        info[func][size] = time
    return info


def createCharts(info, fig, ax):
    for function in info:
        sizes = []
        times = []
        for size in info[function]:
            sizes.append(size)
            times.append(info[function][size] * 10**3)
        ax.plot(sizes, times, label=str(function))
    ax.set_title("Pattern search algorithm")
    ax.set_xlabel('Number of words')
    ax.set_ylabel('Time [ms]')
    ax.legend()
    ax.set_yscale('log')
    fig.savefig("lab5-pattern_search/Chart")


if __name__ == '__main__':
    plt.style.use('seaborn')
    info = read_from_json("lab5-pattern_search/.benchmarks/data.json")
    fig, ax = plt.subplots()
    createCharts(info, fig, ax)
