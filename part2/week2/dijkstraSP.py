import os.path
import heapq

class dijkstraSP():

    def __init__(self, file):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file)

        self.graph = dict()
        with open(filename) as f:
            for line in f:
                parse_data = line.split()
                vertex = int(parse_data[0])

                edges = []
                for edge in parse_data[1:]:
                    edges.append(tuple(map(int, edge.split(','))))
                self.graph[vertex] = edges
    
    def find_SP(self):
        self.dist = dict.fromkeys(self.graph, float('infinity'))
        s = 1
        self.dist[s] = 0
        
        self.q = []
        heapq.heappush(self.q, (0, s))
        while len(self.q) != 0:
            cost, v = heapq.heappop(self.q)
            if self.dist[v] < cost:
                continue
            for edge in self.graph[v]:
                self.relax(v, edge)
        
        targets = [7,37,59,82,99,115,133,165,188,197]
        for target in targets:
            print(self.dist[target], end=',')
    
    def relax(self, v, edge):
        w = edge[0]
        cost = edge[1]

        if self.dist[w] >= self.dist[v] + cost:
            self.dist[w] = self.dist[v] + cost
            heapq.heappush(self.q, (self.dist[w], w))
        
    

sol = dijkstraSP('data/dijkstra.txt')
sol.find_SP()