# A simple search algorithms in python
import random
import time

''' Naive Search -- Scan an entire list and ask if a value is 
    equal to the target. If true return the index, else return -1
'''
def naive_search(l, target):
  for i in range(len(l)):
    if l[1] == target:
      return i
  return -1

''' Binary Search -- Uses a divide and conquer tactic to quickly find
    the target within the list.
'''
def binary_search(l, target, low=None, high=None):
  # This function uses recursion to quickly accomplish this
  if low is None:
    low = 0
  if high is None:
    high = len(l) - 1
  if high < low:
    return -1
  midpoint = (low + high) // 2


  if l[midpoint] == target:
    return midpoint
  elif target < l[midpoint]:
    return binary_search(l, target, low, midpoint - 1)
  else:
    return binary_search(l, target, midpoint + 1, high)

if __name__ == '__main__':
  length = 10000
  sorted_list = set()
  while len(sorted_list) < length:
    sorted_list.add(random.randint(-3 * length, 3 * length))
  sorted_list = sorted(list(sorted_list))
