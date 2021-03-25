
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




