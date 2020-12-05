import sys
sys.path.insert(0, '..')

from library import input

def get_row(boarding_pass: str) -> int:
  # Extract row and convert from binary to decimal, where 'F' represents 0 and 'B' represents 1

  # Row is stored in first 7 characters
  row_encoded = boarding_pass[0:7]
  row = row_encoded.replace('F', '0').replace('B', '1')
  return int(row, 2)

def get_column(boarding_pass: str) -> int:
  # Extract column and convert from binary to decimal, where 'L' represents 0 and 'R' represents 1

  # Column is stored in last 3 characters
  column_encoded = boarding_pass[7:10]
  column = column_encoded.replace('L', '0').replace('R', '1')
  return int(column, 2)

def decode_boarding_pass(boarding_pass: str) -> tuple:
  # Return row, column, and seat ID of an encoded boarding pass
  # Example: FBFBBFFRLR -> (44, 5, 357)

  row = get_row(boarding_pass)
  column = get_column(boarding_pass)
  seat_id = row * 8 + column

  return (row, column, seat_id)

def get_seat_ids() -> list:
  seat_ids = []

  for boarding_pass in input():
    seat_info = decode_boarding_pass(boarding_pass)
    seat_ids.append(seat_info[2])
  
  seat_ids.sort()

  return seat_ids

def main() -> None:
  seat_ids = get_seat_ids()

  # Part 1: find the max seat ID
  print('Part 1 - Max seat ID:', seat_ids[-1])

  # Part 2: find the first missing seat ID
  last_id = None
  for id in seat_ids:
    if last_id and id - last_id != 1:
      print('Part 2 - Missing seat ID:', id - 1)
      break
    else:
      last_id = id

main()
