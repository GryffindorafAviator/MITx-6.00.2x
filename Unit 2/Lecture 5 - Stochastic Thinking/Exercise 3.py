# Exercise 3-1
# 0.0/5.0 points (graded)
# Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.
import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    return 10

# Exercise 3-2
# 0.0/5.0 points (graded)
# Write a uniformly distributed stochastic program, stochasticNumber, that returns an even number between 9 and 21.
import random

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    a = random.randint(5, 10)

    return 2 * a
