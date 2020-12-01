import sys
sys.path.insert(0, '..')

from library import input

target_sum = 2020

# Part 1: find 2 numbers that sum to target number

# O(n) time, O(n) space
def find_double_sum(target_sum):
  # Find 2 numbers in the input that sum to `target_sum`

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

result_nums_part_1 = find_double_sum(target_sum)
print('Matching numbers:', result_nums_part_1)

# Part 1 solution is the product of the matching numbers
if len(result_nums_part_1) == 2:
  print('Product:', result_nums_part_1[0] * result_nums_part_1[1])

print('')

# Part 2: find 3 numbers that sum to target number

# O(n^2) time, O(n) space
def find_triple_sum(target_sum):
  # Find 3 numbers in the input that sum to `target_sum`

  # Sort the input list, then iterate over the list. At each iteration, initialize 
  # two pointers at each end of the remaining range (one at the number after the 
  # current number, and one at the end of the list). Move the pointers towards each
  # other, comparing the sum at each step. Once the pointers meet, move on to the 
  # next overall iteration.
  
  # Load input numbers into a sorted array
  nums = list(input(is_ints=True))
  nums.sort()

  # Overall iteration
  for pointer_main in range(len(nums) - 2):
    pointer_left = pointer_main + 1
    pointer_right = len(nums) - 1

    # Stay on the current step of the overall iteration until the left and right pointers meet
    while pointer_left < pointer_right:
      test_sum = nums[pointer_main] + nums[pointer_left] + nums[pointer_right]
      
      if test_sum == target_sum:
        # Match found
        return [nums[pointer_main], nums[pointer_left], nums[pointer_right]]
      elif test_sum > target_sum:
        # Too large, move right pointer to the previous (smaller) number
        pointer_right -= 1
      elif test_sum < target_sum:
        # Too small, move left pointer to the next (larger) number
        pointer_left += 1

  # No matches found in input
  return []  

result_nums_part_2 = find_triple_sum(target_sum)
print('Matching numbers:', result_nums_part_2)

# Part 2 solution is the product of the matching numbers
if len(result_nums_part_2) == 3:
  print('Product:', result_nums_part_2[0] * result_nums_part_2[1] * result_nums_part_2[2])