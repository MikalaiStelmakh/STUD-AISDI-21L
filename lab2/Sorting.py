def readText(path, size):
    text = []
    with open(path, 'r') as f:
        for line in f:
            for word in line.split():
                if size > 0:
                    text.append(word)
                    size -= 1
        return text


def bubbleSort(lst):
    sorted = True
    for i in range(len(lst[:-1])):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            sorted = False
    if not sorted:
        lst = bubbleSort(lst)
    return lst


def selectionSort(lst):
    minimum = lst[lst.index(min(lst))]
    lst[lst.index(min(lst))], lst[0] = lst[0], minimum
    if len(lst) > 2:
        lst = [lst[0]] + selectionSort(lst[1:])
    return lst


def mergeSort(lst):
    if len(lst) == 1:
        return lst

    l = lst[:len(lst)//2]
    r = lst[len(lst)//2:]

    l = mergeSort(l)
    r = mergeSort(r)

    return merge(l, r)


def merge(l, r):
    sorted = []
    while l and r:
        greater = True if l[0] > r[0] else False
        sorted.append(r[0] if greater else l[0])
        (r if greater else l).remove(r[0] if greater else l[0])
    while l:
        sorted.append(l[0])
        l.remove(l[0])
    while r:
        sorted.append(r[0])
        r.remove(r[0])
    return sorted
