'''
Quick sort which always select first element as pivot.
'''

import os.path

count = 0

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, lo, hi):
    pivot = A[lo]
    i = lo + 1
    for j in range(lo+1, hi + 1):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    swap(A, i-1, lo)
    return i-1


def sort(array):
    quick_sort(array, 0, len(array)-1)


def quick_sort(array, lo, hi):
    if lo >= hi:
        return
    global count
    count += (hi-lo)
    pivot_index = partition(array, lo, hi)
    quick_sort(array, lo, pivot_index-1)
    quick_sort(array, pivot_index+1, hi)


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/quick-sort.txt')

array = []
with open(filename) as f:
    for line in f.readlines():
        array.append(int(line))

sort(array)
print(array)
print(count)