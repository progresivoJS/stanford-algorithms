'''
Quick sort which always select approximately median element(among first and middle and last) as pivot.
'''

import os.path

count = 0

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def sort(A):
    quick_sort(A, 0, len(A)-1)

def quick_sort(A, lo, hi):
    if lo >= hi:
        return
    global count
    count += (hi - lo)
    pivot_index = partition(A, lo, hi)
    quick_sort(A, lo, pivot_index - 1)
    quick_sort(A, pivot_index + 1, hi)

def partition(A, lo, hi):
    m = median_of_3(A, lo, (lo + hi)//2, hi)
    swap(A, m, lo)
    pivot = A[lo]
    i = lo + 1
    for j in range(lo + 1, hi + 1):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    swap(A, lo, i - 1)
    return i-1

def median_of_3(A, lo, mid, hi):
    if A[lo] < A[mid]:
        if A[mid] < A[hi]:
            return mid
        else:
            if A[lo] < A[hi]:
                return hi
            else:
                return lo
    else:
        if A[lo] < A[hi]:
            return lo
        else:
            if A[mid] < A[hi]:
                return hi
            else:
                return mid


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/quick-sort.txt')

array = []
with open(filename) as f:
    for line in f.readlines():
        array.append(int(line))

sort(array)
print(array)
print(count)