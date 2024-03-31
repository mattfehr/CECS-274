from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        self.adj[i][j] = True

    def remove_edge(self, i : int, j : int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        if self.adj[i][j] == True:
            self.adj[i][j] = False
            return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        edges = []
        for j in range(self.n):
            if self.adj[i][j] == True:
                edges.append(j)
        return edges

    def in_edges(self, j) -> List:
        edges = []
        for i in range(self.n):
            if self.adj[i][j] == True:
                edges.append(i)
        return edges

    def bfs(self, r : int):
        traversal =[]
        seen = []
        for i in range(self.n):
            seen.append(False)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while q.size() > 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            '''
            neighbors = []
            for jk in range(self.n):
                if self.has_edge(current,jk):
                    neighbors.append(jk)
            '''
            for jk in neighbors:
                if seen[jk] == False:
                    q.add(jk)
                    traversal.append(jk)
                    seen[jk] = True
        return traversal

    def dfs(self, r : int):
        traversal = []
        s = ArrayStack.ArrayStack()
        seen =[]
        s.push(r)
        for i in range(self.n):
            seen.append(False)
        while s.size() > 0:
            current = s.pop()
            if seen[current] == False:
                traversal.append(current)
                seen[current] = True
            neighbors = self.out_edges(current)
            for neighbor in neighbors[::-1]:
                if seen[neighbor] == False:
                    s.push(neighbor)
        return traversal

    def size(self):
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s
    

g = AdjacencyMatrix(6)
g.add_edge(1,2)
g.add_edge(2,1)
g.add_edge(1,0)
g.add_edge(0,1)
g.add_edge(2,3)
g.add_edge(3,2)
g.add_edge(0,3)
g.add_edge(3,0)
g.add_edge(2,5)
g.add_edge(5,2)
g.add_edge(3,4)
g.add_edge(4,3)
g.add_edge(5,4)
g.add_edge(4,5)
print(g.dfs (1))