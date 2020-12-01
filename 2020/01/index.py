import sys
sys.path.insert(0, '..')

from library import input

# Part 1: find 2 numbers that sum to target number

# O(n) time, O(n) space
def find_sum(target_sum):
  # For each number in the input, calculate the theoretical matching number 
  # and check if it is in the input, tracked through the `seen_nums` dictionary
  
  # Tracking dictionary
  seen_nums = {}
  
  # Read ints from input
  for num in input(is_ints=True):
    needed_number = target_sum - num
    if needed_number in seen_nums:
      # Matching number found in dictionary
      return [num, needed_number]
    else:
      # Add number to dictionary so it can be found if its match is later in the input
      seen_nums[num] = True
  
  # No matches found in input
  return []

target_sum = 2020

result_nums = find_sum(target_sum)
print('Matching numbers:', result_nums)

# Puzzle solution is the product of the matching numbers
if len(result_nums) == 2:
  print('Product:', result_nums[0] * result_nums[1])
