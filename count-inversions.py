def solution(array):
    n = len(array)
    aux = [None] * n
    return sort_and_count_inversions(array, aux, 0, n-1)

def sort_and_count_inversions(array, aux, lo, hi):
    '''
    return the number of inversion in array from lo to hi.
    '''
    if lo >= hi:
        return 0
    mid = lo + (hi - lo) // 2
    x = sort_and_count_inversions(array, aux, lo, mid)
    y = sort_and_count_inversions(array, aux, mid + 1, hi)
    z = merge_and_count_split_inversions(array, aux, lo, mid, hi)
    return x + y + z

def merge_and_count_split_inversions(array, aux, lo, mid, hi):
    for i in range(len(array)):
        aux[i] = array[i]
    
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

array = [6, 5, 4, 3, 2, 1]
print(solution(array))