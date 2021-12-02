

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
                requested_data[key] = True
        else:
            if all(requested_data.values()):
                valid_passports = valid_passports + 1
            requested_data = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False,
                              'pid': False}
    print(f'{valid_passports} passports were validated correctly but with no matter if they included a cid or not.')











