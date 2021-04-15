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


def createCharts(info, figs, axes):
    for function, fig, ax in zip(info, figs, axes):
        for tree in info[function]:
            sizes = []
            times = []
            for size in info[function][tree]:
                sizes.append(size)
                times.append(info[function][tree][size] * 10**3)
            ax.plot(sizes, times, label=tree)
        ax.set_title(function)
        ax.set_xlabel('Number of elements')
        ax.set_ylabel('Time [ms]')
        ax.legend()
        fig.savefig('lab3/charts/' + function)


if __name__ == '__main__':
    plt.style.use('seaborn')
    info = read_from_json('lab3/.benchmarks/data.json')
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    createCharts(info, [fig1, fig2, fig3], [ax1, ax2, ax3])
