import os.path


class KosarajuSCC():
    def __init__(self, file):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file)
        self.graph = dict()
        with open(filename) as f:
            for line in f:
                start, end = map(int, line.split())
                if self.graph.get(start):
                    self.graph[start].append(end)
                else:
                    self.graph[start] = [end]

    def find_scc(self):
        magical_order = self.find_magical_order()
        self.marked = [False] * (875714+1)
        self.sid = [0] * (875714+1)

        self.count = 0
        for v in magical_order:
            if not self.marked[v]:
                self.count += 1
                self.dfs_scc(self.graph, v)
        
        scc_size = dict()
        for cid in self.sid[1:]:
            if scc_size.get(cid):
                scc_size[cid] += 1
            else:
                scc_size[cid] = 1
        
        return sorted(scc_size.values(), reverse=True)[:5]


    def dfs_scc(self, graph, s):
        stack = [s]

        while len(stack) != 0:
            v = stack.pop()
            self.marked[v] = True
            self.sid[v] = self.count
            
            for w in graph.get(v, []):
                if not self.marked[w]:
                    stack.append(w)


    def find_magical_order(self):
        reverse_graph = self.get_reverse_graph()
        self.reverse_post_order = []
        self.marked = [False] * (875714+1)

        for vertex in reverse_graph:
            if not self.marked[vertex]:
                self.dfs(reverse_graph, vertex)

        return list(reversed(self.reverse_post_order))

    def dfs(self, graph, s):
        stack = [s]
        while len(stack) != 0:
            v = stack.pop()
            if self.marked[v]:
                self.reverse_post_order.append(v)
            else:
                self.marked[v] = True
                stack.append(v)
                for w in graph.get(v, []):
                    if not self.marked[w]:
                        stack.append(w)
                        

    def get_reverse_graph(self):
        reverse_graph = dict()
        for start in self.graph:
            for end in self.graph[start]:
                if reverse_graph.get(end):
                    reverse_graph[end].append(start)
                else:
                    reverse_graph[end] = [start]
        return reverse_graph


if __name__ == '__main__':
    file = 'data/scc.txt'
    kosaraju = KosarajuSCC(file)
    scc = kosaraju.find_scc()
    print(scc)
