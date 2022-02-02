import functools
import operator
import math

nums = [1,2,3,4,5]

# returns the cumulative sum of the factorials of ints in nums
print(functools.reduce(operator.add, map(math.factorial, nums)))


