import os.path

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def less(l, i, j):
    '''
    key type is interger.
    return Is l[i] less than l[j]?
    '''
    return l[i] < l[j]


class MinPQ():
    def __init__(self):
        self.size = 0
        self.pq = [-1] # dummy head

    def isEmpty(self):
        return self.size == 0
    
    def delMin(self):
        if self.isEmpty():
            return None
        result = self.pq[1]
        swap(self.pq, 1, self.size)
        self.size -= 1
        self.pq.pop()
        self.sink(1)
        return result
    
    def insert(self, key):
        self.size += 1
        self.pq.append(key)
        self.swim(self.size)

    def peek(self):
        if self.isEmpty():
            return None
        return self.pq[1]
    
    def swim(self, k):
        while k > 1 and less(self.pq, k, k//2):
            swap(self.pq, k//2, k)
            k = k//2
                

    def sink(self, k):
        while 2*k <= self.size:
            j = 2*k
            if j < self.size and less(self.pq, j+1, j):
                j += 1
            if less(self.pq, k, j):
                break
            swap(self.pq, k, j)
            k = j



class MaxPQ():
    def __init__(self):
        self.size = 0
        self.pq = [-1] # dummy head

    def isEmpty(self):
        return self.size == 0
    
    def delMax(self):
        if self.isEmpty():
            return None
        result = self.pq[1]
        swap(self.pq, 1, self.size)
        self.pq.pop()
        self.size -= 1
        self.sink(1)
        return result
    
    def insert(self, key):
        self.size += 1
        self.pq.append(key)
        self.swim(self.size)
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.pq[1]

    def swim(self, k):
        while k > 1 and less(self.pq, k//2, k):
            swap(self.pq, k, k//2)
            k = k // 2
    
    def sink(self, k):
        while 2 * k <= self.size:
            j = 2 * k
            if j < self.size and less(self.pq, j, j+1):
                j += 1
            if less(self.pq, j, k):
                break
            swap(self.pq, k, j)
            k = j


class MedianPQ():
    def __init__(self):
        self.minPQ = MinPQ()
        self.maxPQ = MaxPQ()
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def delMedian(self):
        if self.isEmpty():
            return None
        
        result = 0
        # odd
        if self.size % 2:
            result = self.minPQ.delMin()
        # even
        else:
            result = self.maxPQ.delMax()
        
        self.size -= 1
        return result
    
    def insert(self, key):
        if self.isEmpty():
            self.minPQ.insert(key)
            self.size += 1
            return
        
        target = self.delMedian()
        if key < target:
            self.maxPQ.insert(key)
            self.minPQ.insert(target)
        else:
            self.maxPQ.insert(target)
            self.minPQ.insert(key)
        self.size += 2

    def peek(self):
        if self.isEmpty():
            return None

        # odd
        if self.size % 2:
            return self.minPQ.peek()
        # even
        else:
            return self.maxPQ.peek()



def main():
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
    
if __name__ == '__main__':
    main()