import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        if self.n < 1:
            raise IndexError
        randomi = random.randint(0,self.n-1)
        randome = self.a[(self.j+randomi)%len(self.a)]
        self.a[(self.j+randomi)%len(self.a)] = self.a[self.j]
        self.a[self.j] = randome
        return super().remove()

'''
r = RandomQueue()
for num in range(5):
    r.add(num)
    print(r)
for num in range(5):
    r.remove()
    print(r)
'''

