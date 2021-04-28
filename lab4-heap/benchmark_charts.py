import json
from matplotlib import pyplot as plt


def read_from_json(path):
    with open(path) as f:
        data = json.load(f)
    info = {
        benchmark['extra_info']['function']: {}
        for benchmark in data['benchmarks']
        }
    for function in ['push', 'pop']:
        info[function] = {
            benchmark['extra_info']['dimension']: {}
            for benchmark in data['benchmarks']
        }
    for benchmark in data['benchmarks']:
        func = benchmark['extra_info']['function']
        size = benchmark['extra_info']['size']
        dimension = benchmark['extra_info']['dimension']
        time = benchmark['stats']['median']
        info[func][dimension][size] = time
    return info


def createCharts(info, figs, axes):
    for function, fig, ax in zip(info, figs, axes):
        for dimension in info[function]:
            sizes = []
            times = []
            for size in info[function][dimension]:
                sizes.append(size)
                times.append(info[function][dimension][size] * 10**3)
            ax.plot(sizes, times, label=str(dimension)+"-ary heap")
        ax.set_title(function)
        ax.set_xlabel('Number of elements')
        ax.set_ylabel('Time [ms]')
        ax.legend()
        ax.set_yscale('log')
        ax.set_xticks([1000, 2000, 4000, 6000, 8000, 10000])
        fig.savefig('lab4-heap/' + function)


if __name__ == '__main__':
    plt.style.use('seaborn')
    info = read_from_json("lab4-heap/.benchmarks/data.json")
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    createCharts(info, [fig1, fig2], [ax1, ax2])
