import re

EYE_COLOURS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def convert_to_dict(fields):
    field_dict = {}
    for field in fields:
        field_dict[field[0:3]] = field[4:]
    return field_dict


def validate_hgt(height):
    if 'in' in height:
        return 59 <= int(height[:-2]) <= 76
    elif 'cm' in height:
        return 150 <= int(height[:-2]) <= 193
    else:
        return False


def validate(field_dict,
             check_additional_constaints=False):
    if (REQUIRED_FIELDS - set(field_dict.keys())) != set():
        return False
    else:
        if check_additional_constaints:
            return all([(1920 <= int(field_dict['byr']) <= 2002),
                        (2010 <= int(field_dict['iyr']) <= 2020),
                        (2020 <= int(field_dict['eyr']) <= 2030),
                        (validate_hgt(field_dict['hgt'])),
                        (bool(re.search(r"^[#][0-9a-f]{6}$", field_dict['hcl']))),
                        (field_dict['ecl'] in EYE_COLOURS),
                        (bool(re.search(r"^[0-9]{9}$", field_dict['pid'])))])
        else:
            return True


passports = open('2020/data/4.txt').read().split('\n\n')
passport_fields = [convert_to_dict(re.split(' |\n', passport)) for passport in passports]
print('Puzzle 1 : ', sum([validate(x) for x in passport_fields]))
print('Puzzle 2 : ', sum([validate(x, True) for x in passport_fields]))

# Puzzle 1 :  256
# Puzzle 2 :  198
