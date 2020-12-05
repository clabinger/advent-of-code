import re
import sys
sys.path.insert(0, '..')

from library import input

fields = [
  'byr', # Birth Year
  'iyr', # Issue Year
  'eyr', # Expiration Year
  'hgt', # Height
  'hcl', # Hair Color
  'ecl', # Eye Color
  'pid' # Passport ID
  # 'cid' # Country ID - cid not required for a passport to be considered valid
]

def get_passports() -> list:
  # Iterate over input file and read passports (each passport is spread across an arbitrary number of consecutive lines)
  # Return passports as lists of attributes

  fields = []
  for line in input():
    if line == '':
      # Line is empty, return fields for current passport and reset field list for next passport
      yield fields
      fields = []
    else:
      # Line has fields, split them (by space) and add them to field list for current passport
      fields += line.split()
  # Return last passport (no new line at end of input)
  yield fields

def format_passport(passport: list) -> dict:
  # Parse list of fields into a dict with field names as keys
  # Example: 'byr: 2000' -> {'byr': '2000'}

  formatted_passport = {}
  for field in passport:
    m = re.match(r'([a-z]{3}):(.+)', field)
    formatted_passport[m.group(1)] = m.group(2)
  return formatted_passport

def is_valid(passport: dict) -> bool:
  # Passport is valid if all required fields are included

  for field in fields:
    if not passport.get(field):
      return False
  return True

def main() -> None:
  # Count number of valid passports
  print('Valid passports:', sum(1 for passport in get_passports() if is_valid(format_passport(passport))))

main()
