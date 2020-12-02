def input(is_ints:bool=False):
  # Use generator
  for line in open('input.txt'):
    raw = line.rstrip('\n')
    yield int(raw) if is_ints else raw
