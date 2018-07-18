import os.path

def solution(array):
    n = len(array)
    return sort_and_count_inversions(array, 0, n-1)

def sort_and_count_inversions(array, lo, hi):
    '''
    return the number of inversion in array from lo to hi.
    '''
    if lo >= hi:
        return 0
    mid = lo + (hi - lo) // 2
    x = sort_and_count_inversions(array, lo, mid)
    y = sort_and_count_inversions(array, mid + 1, hi)
    z = merge_and_count_split_inversions(array, lo, mid, hi)
    return x + y + z

def merge_and_count_split_inversions(array, lo, mid, hi):
    aux = list(array)
    inversion = 0
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            array[k] = aux[j]
            j += 1
        elif j > hi:
            array[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            array[k] = aux[i]
            i += 1
        else: # aux[i] > aux[j]
            array[k] = aux[j]
            j += 1
            inversion += (mid - i + 1)

    return inversion

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'integer.txt')

array = []
with open(filename) as f:
    for line in f.readlines():
        array.append(int(line))
print(solution(array))