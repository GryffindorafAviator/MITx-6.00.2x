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


    
