import math
import sys
sys.path.insert(0, '..')

from library import input

# Part 1 alone
# Count trees encountered traversing right 3, down 1, beginning at [0, 0]
# On each line, the current position is the line index times 3. Modulo by the length of the line to simulate the infinite repetitions to the right
# Trees are indicated by '#'

# print('Part 1 trees:', sum(1 for index, line in enumerate(input()) if line[(index * 3) % len(line)] == '#'))

# Part 2
# Count trees at 5 different angles, and multiply the result

angles = [
  # (right, down)
  (1, 1),
  (3, 1), # Angle for part 1
  (5, 1),
  (7, 1),
  (1, 2)
]

# Initialize results array
results = [0] * len(angles)

for line_index, line in enumerate(input()):
  for angle_index, angle in enumerate(angles):
    if (
      line_index % angle[1] == 0 # Only consider every nth line, indicated by the "down" component of the angle
        and 
      # On each line, the current position is the "real" line index (found by dividing the line index by the "down" component of the angle)
      # times the "right" component of the angle. Modulo by the length of the line to simulate the infinite repetitions to the right.
      # Trees are indicated by '#'
      line[int(line_index / angle[1] * angle[0]) % len(line)] == '#'
    ):
        results[angle_index] += 1


print('Part 1 trees:', results[1])

print('Part 2 trees for each angle:', results)

print('Part 2 product:', math.prod(results))