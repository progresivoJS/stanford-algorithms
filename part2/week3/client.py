import os.path
from median_heap_based import MedianPQ
from binary_search_tree import BinarySearchTree
import time

def pq_client():
    start = time.time()
    mod = 10000
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'data/median.txt')
    result = 0
    pq = MedianPQ()
    with open(filename) as f:
        for line in f.readlines():
            pq.insert(int(line))
            result += pq.peek()
            result %= mod
    print(result)
    end = time.time()
    print(end - start)

def st_client():
    start = time.time()
    mod = 10000
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'data/median.txt')
    result = 0
    st = BinarySearchTree()
    with open(filename) as f:
        for line in f.readlines():
            st[int(line)] = 0
            result += st.select((st.size()+1) // 2)
            result %= mod
    print(result)
    end = time.time()
    print(end - start)
    
if __name__ == '__main__':
    pq_client()
    st_client()