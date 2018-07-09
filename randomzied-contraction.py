import os.path
import random

def contraction(adj):
    '''
    process randomized contraction algorithm.
    return the number of edges in cut.
    '''
    while len(adj) > 2:
        v1 = random.choice(list(adj.keys()))
        v2 = random.choice(adj[v1])

        adj[v1].extend(adj[v2])

        for vertex in adj[v2]:
            adj[vertex].remove(v2)
            adj[vertex].append(v1)
        
        adj[v1] = [x for x in adj[v1] if x != v1]
        adj.pop(v2)

    min_cut = 0
    for key in adj:
        min_cut += len(adj[key])
    
    return min_cut // 2

def simuation():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'data/karger.txt')

    adj = dict()
    with open(filename) as f:
        for line in f:
            nums = list(map(int, line.split()))
            adj[nums[0]] = nums[1:]

    return contraction(adj)

min_cut = 987654321
for i in range(100):
    min_cut = min(min_cut, simuation())
print(min_cut)