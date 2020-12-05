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

def main() -> None:
  # Get maximum Seat ID
  
  max_seat_id = 0

  for boarding_pass in input():
    seat_info = decode_boarding_pass(boarding_pass)
    if seat_info[2] > max_seat_id:
      max_seat_id = seat_info[2]
  
  print('Max Seat ID:', max_seat_id)

main()
