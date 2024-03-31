"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        if j not in self.adj[i]:
            self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        if i < 0 or i >= self.n:
            raise IndexError
        incoming = []
        for k in range(self.n):
            if self.has_edge(k,i):
                incoming.append(k)
        return incoming

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
            '''
            neighbors = []
            for jk in range(self.n):
                if self.has_edge(current,jk):
                    neighbors.append(jk)
            '''
            for neighbor in reversed(neighbors):
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

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

'''
g = AdjacencyList(6)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(0,1)
g.add_edge(1,0)
g.add_edge(2,5)
g.add_edge(2,3)
g.add_edge(3,2)
g.add_edge(3,1)
g.add_edge(3,2)
g.add_edge(4,3)
g.add_edge(5,4)
g.add_edge(5,3)
print(g.out_edges(2))
neighbors = []
for jk in range(g.n):
    if g.has_edge(2,jk):
        neighbors.append(jk)
print(neighbors)
print(g.dfs(2))
'''
'''
g = AdjacencyList(6)
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
print(g.dfs(1))
'''

def isAnagram(s: str, t: str) -> bool:
    s_list = list(s)
    t_list = list(t)
    print(s_list)
    s_list.sort()
    t_list.sort()
    print(s_list)
    print(t_list)
    return s_list == t_list

print(isAnagram("rat", "car"))
