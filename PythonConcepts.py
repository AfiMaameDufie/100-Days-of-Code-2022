# Python reduce function
# Pure functions do one thing and one thing alone and has no side effects
# reduce is an implementation of mathematical concept fold or reduction
# often used in functional programming
# reduce() follows the SOLID principle

# reduce used for sum()
# first class object
# input for reduce is a function
# timeit package python

from operator import add 

def reduce(func, items):
  
  val = func(items[0], items[1])
  for item in items[2:]:
    val = func(val,item)
  return val


import unittest
class ReduceTestCase(unittest.TestCase):
  def test_reduce_to_sum(self):
    self.assrtEqual(13, reduce(add, [4,2,7]))


