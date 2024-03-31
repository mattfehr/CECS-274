from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x : object):
        """
        adds an element to the end of this max queue
        INPUT: x the element to add
        """
        super().add(x)
        if self.max_deque.n == 0:
            self.max_deque.add_first(x)
        elif x < self.max_deque.dummy.prev.x:
            self.max_deque.add_last(x)
        else: 
            next_node = self.max_deque.dummy.next
            for i in range(0,self.max_deque.n):
                if x > next_node.x:
                    new_node = self.max_deque.add(i,x)
                    self.max_deque.dummy.prev = new_node
                    new_node.next = self.max_deque.dummy
                    self.max_deque.n = i + 1 #n = n - not iterated, not iterated = n-(i+1)
                    break
                next_node = next_node.next


    def remove(self) -> object:
        """
        removes and returns the element at the head of the max queue
        """
        removed = super().remove()
        if removed == self.max_deque.dummy.next.x:
            self.max_deque.remove_first()
        return removed 

    def max(self):
        """
        returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)
    


'''    
# TESTER
mq = MaxQueue()
mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(2)
print("Added:", 2)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")
'''

'''
max = MaxQueue()
max.add(3)
print("SLL", max, "DLL", max.max_deque)
max.add(4)
print("SLL", max, "DLL", max.max_deque)
max.add(1)
print("SLL", max, "DLL", max.max_deque)
max.add(2)
print("SLL", max, "DLL", max.max_deque)
max.remove()
print("SLL", max, "DLL", max.max_deque)
max.remove()
print("SLL", max, "DLL", max.max_deque)
max.add(8)
print("SLL", max, "DLL", max.max_deque)
max.add(6)
print("SLL", max, "DLL", max.max_deque)
max.add(5)
print("SLL", max, "DLL", max.max_deque)
max.add(7)
print("SLL", max, "DLL", max.max_deque)
'''

