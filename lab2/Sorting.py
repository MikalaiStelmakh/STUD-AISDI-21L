
def bubbleSort(value):
    sorted = True
    for i in range(len(value[:-1])):
        if value[i] > value[i+1]:
            value[i], value[i+1] = value[i+1], value[i]
            sorted = False
    if not sorted:
        value = bubbleSort(value)
    return value






