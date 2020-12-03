import sys
sys.path.insert(0, '..')

from library import input

# Part 1
# Count trees encountered traversing right 3, down 1, beginning at [0, 0]
# On each line, the current position is the line index times 3. Modulo by the length of the line to simulate the infinite repetitions to the right
# Trees are indicated by '#'

print('Part 1 trees:', sum(1 for index, line in enumerate(input()) if line[(index * 3) % len(line)] == '#'))