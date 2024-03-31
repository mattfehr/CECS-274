"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return None


def binary_search(a: List, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l+r)//2
        if x == a[m]:
            return m
        elif x < a[m]:
            r = m-1
            print(a[l:r])
        else:
            l = m+1
            print(a[l:r])
    return None

def _merge(a0: List, a1: List, a: List):
    i0 = 0
    i1 = 0
    for i in range(0, len(a)):
        if i0 == len(a0):
           a[i] = a1[i1]
           i1 += 1
        elif i1 == len(a1):
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1

def merge_sort(a: List):
    if len(a) == 0 or len(a) == 1:
        return a
    m = len(a)//2
    a0 = a[0:m]
    a1 = a[m:len(a)]
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0,a1,a)


def _quick_sort_f(a: List, start, end):
    if start < end:
        p = _partition(a,start,end)
        _quick_sort_f(a, start, p-1)
        _quick_sort_f(a,p+1,end)


def _quick_sort_r(a: List, start, end):
    if start < end:
        r_idx = random.randint(start, end)
        swap = a[start]
        a[start] = a[r_idx]
        a[r_idx] = swap
        p = _partition(a,start,end)
        _quick_sort_r(a, start, p-1)
        _quick_sort_r(a,p+1,end)

def _partition(a,start,end):
    pivot = a[start]
    l = start + 1
    r = end
    while l <= r:
        while  l <= r and a[l] <= pivot:
            l += 1
        while r >= l and a[r] > pivot:
            r -= 1
        if l <= r:
            swap = a[l]
            a[l] = a[r]
            a[r] = swap
            #print("Same part", a, l, r)
    swap = a[r]
    a[r] = pivot
    a[start] = swap
    #print("End part",a,l,r)
    return r

def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, len(a) - 1)
    else:
        _quick_sort_f(a, 0, len(a) - 1)

'''
a = [13,8,5,2,4,0,6,9,7,3,12,1,10,11]
merge_sort(a)
print(a)
a = [23,6,53,81,4,78,6,65]
print(a)
quick_sort(a, False)
print(a)
a = [23,6,53,81,4,78,6,65]
quick_sort(a,True)
print(a)
a = [5,6,7,7,30,45,150,653]
binary_search(a,7)
a = [56,10,34,87,41,34,9,3]
print(a)
quick_sort(a, False)
a = [5,6,7,7,30,45,150,653]
print(a)
quick_sort(a, False)
'''