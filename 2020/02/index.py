import re
import sys
sys.path.insert(0, '..')

from library import input

# Check that passwords meet their respective policies. The policies are different in Part 1 and Part 2.

def check_policy_part_1(indicator: tuple, test_letter: str, password: str):
  # Return True if the number of instances of `test_letter` in `password` is within the range (inclusive) given by `indicator`
  occurences = password.count(test_letter)
  return indicator[0] <= occurences <= indicator[1]

def check_policy_part_2(indicator: tuple, test_letter: str, password: str):
  # Return True if `test_letter` appears in `password` in exactly one of the two positions indicated by `indicator` (1-indexed)
  position_matches = sum(1 for position in range(2) if password[indicator[position] - 1] == test_letter)
  return position_matches == 1

def parse_line(input: str):
  # Extract `indicator`, `test_letter`, and `password` from a line
  # `indicator` is always a pair of numbers, the usage of which is different in parts 1 and 2

  # Example: 
    # Raw: 1-3 a: abcde
    # indicator: (1, 3)
    # test_letter: 'a'
    # password: 'abcde'

  m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', input)
  return {
    'password': m.group(4),
    'test_letter': m.group(3),
    'indicator': tuple(map(int, m.group(1, 2)))
  }
  
print('Part 1 matches:',
  sum(1 for line in input() if check_policy_part_1(**parse_line(line)))
)

print('Part 2 matches:',
  sum(1 for line in input() if check_policy_part_2(**parse_line(line)))
)