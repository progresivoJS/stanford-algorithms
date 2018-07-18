import random

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(A, lo, hi):
    swap(A, lo, random.randrange(lo, hi + 1))
    pivot_index = lo
    i = lo + 1
    for j in range(lo + 1, hi + 1):
        if A[pivot_index] > A[j]:
            swap(A, i, j)
            i += 1
    swap(A, i-1, pivot_index)
    return i-1


def quick_select(A, rank):
    lo = 0
    hi = len(A) - 1

    while (lo < hi):
        j = partition(A, lo, hi)
        if j == rank:
            return A[rank]
        elif j < rank:
            lo = j+1
        else:
            hi = j-1
    return A[rank]


A = [1, 6, 1, 7, 21]
print(quick_select(A, 2))
