from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i >= self.n:
            return self.dummy
        if i < self.n/2:
            p = self.dummy.next
            for k in range(i):
                p = p.next
        else:
            p = self.dummy.prev
            for k in range(self.n-i-1):
                p = p.prev
        return p

    def get(self, i) -> object:
        if i < 0 or i >= self.n:
            raise IndexError
        u = self.get_node(i)
        return u.x 


    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise IndexError
        node = self.get_node(i)
        old = node.x
        node.x = x
        return old

    def add_before(self, w: Node, x: object) -> Node:
        if w == None:
            return IndexError
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u 
        u.prev.next = u
        self.n += 1
        return u 

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError
        return self.add_before(self.get_node(i),x)

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n:  
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        front = self.dummy.next
        back = self.dummy.prev
        for i in range(self.n//2):
            if front.x != back.x:
                return False
            front = front.next
            back = back.prev
        return True

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
    
    def reverse(self):
        current_node = self.dummy
        for k in range(self.n+1):
            next_node = current_node.next
            current_node.next = current_node.prev
            current_node.prev = next_node
            current_node = next_node


'''
l = DLList()
l.add(0,4)
l.add(0,1)
l.add(1,3)
l.add(1,2)
l.add(4,5)
print(l)
l.reverse()
print(l)
l.reverse()
print(l.get(1))
l.remove(2)
print(l)
l.remove(3)
print(l)
'''
'''
p = DLList()
word = "hannah"
for letter in word:
    p.add(0,letter)
print(DLList.isPalindrome(p))'''

'''
class Solution:
    def trap(self, height):
        l = 0
        r = 1
        total = 0
        while r < len(height):
            print(f"l is {l}, r is {r}")
            while (height[l] > height[r]) and (r+1 < len(height)):
                r += 1
                print(l, r)
                if r == len(height)-1 and height[r] < height[l] and l+1 < r-1:
                    l += 1
                    r = l + 1
            print(f"l is {l}, r is {r}")
            total += (r-(l+1))*(min(height[l], height[r]))-sum(height[l+1:r])
            print(f"total is {total}")
            l = r
            r = l + 1
        if total < 0:
            return 0
        return total
'''

class Solution:
    def isSameTree(self, p, q):
        queueq = []
        queuep = []
        if p == q and p != None:
            queuep.append(p)
            queueq.append(q)
        while len(queuep) > 0 or len(queueq) > 0:
            up = queuep.pop(0)
            uq = queueq.pop(0)
            if up != uq:
                return False
            queuep.append(up.left)
            queuep.append(up.right)
            queueq.append(uq.left)
            queueq.append(uq.right)
            print(queueq, queuep)
        return True
                    
Sol = Solution()
print(Sol.merge([1,2,3,0,0,0], [2,5,6], 3, 3))