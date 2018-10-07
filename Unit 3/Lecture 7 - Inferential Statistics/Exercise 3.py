# Exercise 3
# 5/5 points (graded)
# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, 
# and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.

# Recall that the standard deviation is computed by this equation:

# where:

# is the mean of the elements in X.

# means the sum of the quantity  for t in X.

# That is, for each element (that we name t) in the set X, we compute the quantity . 
# We then sum up all those computed quantities.

# N is the number of elements in X.

# Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.

# Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.

# If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')

    else:
        N = len(L)
        len_list = []
        summary = 0
        sum_of_square = 0

        for string in L:
            len_list.append(len(string))

        summary = sum(len_list)
        mean = summary/N

        for i in len_list:
            sum_of_square += (i-mean)**2

        return (sum_of_square/N)**0.5


L1 = ['a', 'z', 'p']
print(stdDevOfLengths(L1))
L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L2))
L3 = []
print(stdDevOfLengths(L3))
