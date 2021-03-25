
def bubbleSort(value):
    sorted = True
    for i in range(len(value[:-1])):
        if value[i] > value[i+1]:
            value[i], value[i+1] = value[i+1], value[i]
            sorted = False
    if not sorted:
        value = bubbleSort(value)
    return value

def selectionSort(value):
    minimum = value[value.index(min(value))]
    value[value.index(min(value))], value[0] = value[0], minimum
    if len(value) > 2:
        value = [value[0]] + selectionSort(value[1:])
    return value

def mergeSort(value):
    if len(value) == 1:
        return value

    l = value[:len(value)//2]
    r = value[len(value)//2:]

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
