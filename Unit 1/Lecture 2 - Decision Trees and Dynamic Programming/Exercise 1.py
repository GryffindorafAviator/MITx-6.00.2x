# Exercise 1
# 0.0/10.0 points (graded)
# Here is the lecture from 6.00.1x on generators. Additionally, you can also take a look at Chapter 8.3 in the textbook.

# For the following problem, consider the following way to write a power set generator. 
# The number of possible combinations to put n items into one bag is 2^n. Here, items is a Python list. 
# If need be, also check out the docs on bitwise operators (<<, >>, &, |, ~, ^).

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print('i =', i)
        combo = []
        for j in range(N):
            print('j =', j)
            print('i >> j =', (i >> j))
            print('i / 2^j =', i/2**j)
            print('(i >> j) % 2 =', (i >> j) % 2)
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                print('yeah')
                combo.append(items[j])
        yield combo
        print('\n')

li = ['A', 'B', 'C', 'D']

liIteration = powerSet(li)

for i in range(2**len(li)):
    print(liIteration.__next__())
    
# As above, suppose we have a generator that returns every combination of objects in one bag. 
# We can represent this as a list of 1s and 0s denoting whether each item is in the bag or not.

# Write a generator that returns every arrangement of items such that each is in one or none of two different bags. 
# Each combination should be given as a tuple of two lists, the first being the items in bag1, 
# and the second being the items in bag2.

# Note this generator should be pretty similar to the powerSet generator above.

# We mentioned that the number of possible combinations for N items into one bag is 2^n. 
# How many possible combinations exist when there are two bags? 
# Think about this for a few minutes, then click the following hint to confirm if your guess is correct. 
# Remember that a given item can only be in bag1, bag2, 
# or neither bag -- it is not possible for an item to be present in both bags!

import random

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'

def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        print('i =', i)
        bag1 = []
        bag2 = []
        for j in range(N):
            print('j =', j)
            print('i // 3^j =', i >> 3**j)
            print('(i // 3^j) % 3 =', (i >> 3**j) % 3)
            if (i // 3**j) % 3 == 1:
                print('bag1 yeah')
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                print('bag2 yeah')
                bag2.append((items[j]))
        yield bag1, bag2
        print('\n')

li = ['A', 'B', 'C', 'D']

liIteration = yieldAllCombos(li)

for i in range(3**len(li)):
    print(liIteration.__next__())
    
