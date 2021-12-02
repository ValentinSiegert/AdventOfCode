import re

if __name__ == '__main__':
    with open("day4.txt") as passports_data:
        passports_list = [line[:-1] for line in passports_data.readlines()]
        passports_list.append('')
    requested_data = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
    valid_passports = 0
    for line in passports_list:
        if line != '':
            for key_value in line.split():
                key, value = key_value.split(':')
                if key == 'byr':
                    if len(value) == 4 and 1920 <= int(value) <= 2002:
                        requested_data[key] = True
                elif key == 'iyr':
                    if len(value) == 4 and 2010 <= int(value) <= 2020:
                        requested_data[key] = True
                elif key == 'eyr':
                    if len(value) == 4 and 2020 <= int(value) <= 2030:
                        requested_data[key] = True
                elif key == 'hgt':
                    if value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193:
                        requested_data[key] = True
                    elif value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76:
                        requested_data[key] = True
                elif key == 'hcl':
                    regex = re.compile(r'^#[a-f0-9]{6}$')
                    if regex.match(value):
                        requested_data[key] = True
                elif key == 'ecl':
                    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        requested_data[key] = True
                elif key == 'pid':
                    if value.isdigit() and len(value) == 9:
                        requested_data[key] = True
        else:
            if all(requested_data.values()):
                valid_passports = valid_passports + 1
            requested_data = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False,
                              'pid': False}
    print(f'{valid_passports} passports were validated correctly with a check on the values but with no matter if they'
          f' included a cid or not.')











