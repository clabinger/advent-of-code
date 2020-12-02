import re
import sys
sys.path.insert(0, '..')

from library import input

# Part 1: check that passwords meet their respective policies

def check_policy(indicator: tuple, test_letter: str, password: str):
  # Return True if the number of instances of `test_letter` in `password` is within the range (inclusive) given by `indicator`
  occurences = password.count(test_letter)
  return indicator[0] <= occurences <= indicator[1]

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
  
# Part 1 solution is the number of input lines that meet their respective policies
print('Part 1 matches:',
  sum(1 for line in input() if check_policy(**parse_line(line)))
)