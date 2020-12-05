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

def validate_field(field_name: str, value: str) -> bool:
  # Test if the a given field value meets the requirements for that field

  # Birth Year - four digits; at least 1920 and at most 2002.
  if field_name == 'byr':
    return re.match(r'^\d{4}$', value) and 1920 <= int(value) <= 2002
  
  # Issue Year - four digits; at least 2010 and at most 2020.
  elif field_name == 'iyr':
    return re.match(r'^\d{4}$', value) and 2010 <= int(value) <= 2020
  
  # Expiration Year - four digits; at least 2020 and at most 2030.
  elif field_name == 'eyr':
    return re.match(r'^\d{4}$', value) and 2020 <= int(value) <= 2030
  
  # Height - a number followed by either cm or in: If cm, the number must be at least 150 and at most 193. If in, the number must be at least 59 and at most 76.
  elif field_name == 'hgt':
    m = re.match(r'^(\d+)(in|cm)$', value)
    return m and (
      (m.group(2) == 'cm' and 150 <= int(m.group(1)) <= 193) 
        or 
      (m.group(2) == 'in' and 59 <= int(m.group(1)) <= 76)
    )
  
  # Hair Color - a # followed by exactly six characters 0-9 or a-f.
  elif field_name == 'hcl':
    return re.match(r'^#[0-9a-f]{6}$', value)
  
  # Eye Color - exactly one of: amb blu brn gry grn hzl oth.
  elif field_name == 'ecl':
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  
  # Passport ID - a nine-digit number, including leading zeroes.
  elif field_name == 'pid':
    return re.match(r'^\d{9}$', value)
  
  # Presence of other fields (including 'cid') does not invalidate passport  
  else:
    return True

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

def is_valid(passport: dict, validate_fields: bool = False) -> bool:
  # Passport is valid if all required fields are included
  # If validate_fields is True, field values will also be evaluated (for part 2)

  for field in fields:
    if not passport.get(field):
      return False
    if validate_fields and not validate_field(field, passport.get(field)):
      return False
  return True

def main() -> None:
  # Count number of valid passports
  
  valid_part_1 = 0
  valid_part_2 = 0

  for passport in get_passports():
    formatted_passport = format_passport(passport)
    if is_valid(formatted_passport):
      valid_part_1 += 1
    if is_valid(formatted_passport, validate_fields=True):
      valid_part_2 += 1

  print('Valid passports (part 1):', valid_part_1)
  print('Valid passports (part 2):', valid_part_2)

main()
