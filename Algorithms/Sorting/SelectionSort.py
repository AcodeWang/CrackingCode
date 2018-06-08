
def less(a: object, b: object):
    if a < b:
        return True
    else:
        return False


def exchange(obj, i, j):
    temp = obj[i]
    obj[i] = obj[j]
    obj[j] = temp


def selection_sort(obj):

    for i in range(len(obj)):
        min_index = i
        for j in range(i, len(obj)):
            if less(obj[j], obj[min_index]):
                min_index = j

        exchange(obj, i, min_index)
        print(obj)
    return obj


def insertion_sort(obj):

    for i in reversed(range(0, len(obj)-1)):
        for j in range(i, len(obj)):
            if j+1 < len(obj) and less(obj[j+1], obj[j]):
                exchange(obj, j, j+1)
            else:
                continue
        print(obj)

    # for i in range(1, len(obj)):
    #     for j in reversed(range(0, i+1)):
    #         if j > 0 and less(obj[j], obj[j-1]):
    #             exchange(obj, j, j-1)
    #         else:
    #             continue
    #     print(obj)
    # return obj


insertion_sort(list('987654321'))
