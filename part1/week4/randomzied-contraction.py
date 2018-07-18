import os.path
import random

class KargerContraction():
    def __init__(self, file):
        self.graph = dict()
        self.total_edge_count = 0

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file)
        with open(filename) as f:
            for line in f:
                nums = list(map(int, line.split()))
                self.graph[nums[0]] = nums[1:]
                self.total_edge_count += len(nums[1:])
    
    def pick_verticies(self):
        random_edge = random.randint(0, self.total_edge_count - 1)
        for vertex, vertex_edges in self.graph.items():
            if random_edge >= len(vertex_edges):
                random_edge -= len(vertex_edges)
            else:
                v1 = vertex
                v2 = vertex_edges[random_edge]
                return v1, v2
        
    
    def find_min_cut(self):
        '''
        process randomized contraction algorithm.
        return the number of edges in cut.
        '''
        while len(self.graph) > 2:
            v1, v2 = self.pick_verticies()
            self.graph[v1].extend(self.graph[v2])
            self.total_edge_count -= len(self.graph[v1])

            for vertex in self.graph[v2]:
                self.graph[vertex].remove(v2)
                self.graph[vertex].append(v1)
            
            self.graph[v1] = [x for x in self.graph[v1] if x != v1]
            self.total_edge_count += len(self.graph[v1])
            self.graph.pop(v2)

        min_cut = 0
        for key in self.graph:
            min_cut += len(self.graph[key])
        
        return min_cut // 2

min_cut = 987654321
file = 'data/karger.txt'
for i in range(100):
    min_cutter = KargerContraction(file)
    min_cut = min(min_cut, min_cutter.find_min_cut())
print(min_cut)