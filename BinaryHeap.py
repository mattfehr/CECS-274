import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2*i+1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2*(i+1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i-1)//2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True 

    def remove(self):
        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n -= 1
        self._trickle_down_root()
        if 3*self.n < len(self.a):
            self._resize()
        return x

    def depth(self, u) -> int:
        u_idx = 0
        while self.a[u_idx] != u:
            u_idx += 1
            if u_idx == self.n:
                raise ValueError(f"{u} is not found in the binary tree.")
        current = self.a[u_idx]
        count = 0
        while current != self.a[0]:
            u_idx = parent(u_idx)
            current = self.a[u_idx]
            count += 1
        return count


    def height(self) -> int:
        return int(math.log2(self.n))

    def bf_order(self) -> list:
        return self.a[0:self.n]

    def in_order(self) -> list:
        return self._in_order(0)

    def _in_order(self, u):
        nums = []
        if left(u) < self.n:
            nums.extend(self._in_order(left(u)))
        nums.append(self.a[u])
        if right(u) < self.n:
            nums.extend(self._in_order(right(u)))
        return nums

    def post_order(self) -> list:
        return self._post_order(0)

    def _post_order(self, u):
        nums = []
        if left(u) < self.n:
            nums.extend(self._post_order(left(u)))
        if right(u) < self.n:
            nums.extend(self._post_order(right(u)))
        nums.append(self.a[u])
        return nums

    def pre_order(self) -> list:
        return self._pre_order(0)

    def _pre_order(self,u):
        nums = []
        nums.append(self.a[u])
        if left(u) < self.n:
            nums.extend(self._pre_order(left(u)))
        if right(u) < self.n:
            nums.extend(self._pre_order(right(u)))
        return nums

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n -1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            swap = self.a[i]
            self.a[i] = self.a[p_idx]
            self.a[p_idx] = swap
            i = p_idx
            p_idx = parent(i)

    def _resize(self):
        self.b = _new_array(max(1,2*self.n))
        for i in range(0,self.n):
            self.b[i] = self.a[i]
        self.a = self.b

    def _trickle_down_root(self):
        i = 0
        l_idx = left(i)
        r_idx = right(i)
        #print(self.n, l_idx, r_idx)
        while (i <= self.n and l_idx <= self.n and r_idx <= self.n) and (self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
            #print("go")
            if self.a[l_idx] <= self.a[r_idx]:
                min_idx = l_idx
            else:
                min_idx = r_idx
            swap = self.a[i]
            self.a[i] = self.a[min_idx]
            self.a[min_idx] = swap
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)


    def __str__(self):
        return str(self.a[0:self.n])
    
'''
heap = BinaryHeap()
heap.add(5)
heap.add(20)
heap.add(30)
heap.add(38)
heap.add(35)
heap.add(37)
heap.add(52)
heap.add(40)
heap.add(42)
print(list(heap.bf_order()))
print(heap.height())
print(heap.depth(35))
print(heap.in_order())
print(heap.bf_order())
for i in range(9):
    print(heap.remove(), heap.bf_order())
'''
