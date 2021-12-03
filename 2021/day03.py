

def report(bit_strings, bit_criteria):
    index_bit = 0
    while len(bit_strings) > 1:
        n0 = [n for n in bit_strings if n[index_bit] == '0']
        n1 = [n for n in bit_strings if n[index_bit] == '1']
        bit_strings = bit_criteria(n0, n1)
        index_bit += 1
    return int(bit_strings[0], 2)


if __name__ == '__main__':
    count = {index: [0, 0] for index in range(11, -1, -1)}
    with open('day3.log') as log_file:
        for line in log_file:
            for index, bit in enumerate(line.strip()[::-1]):
                count[index][int(bit)] = count[index][int(bit)] + 1
        log_file.seek(0)
        o2_list = [line[:-1] for line in log_file.readlines()]
        co2_list = o2_list.copy()
    gamma_bit = epsilon_bit = ''
    for c in count.values():
        if c[0] > c[1]:
            gamma_bit += '0'
            epsilon_bit += '1'
        elif c[0] < c[1]:
            gamma_bit += '1'
            epsilon_bit += '0'
        else:
            print('There is one bit equal!')
            exit(0)
    gamma = int(gamma_bit, 2)
    epsilon = int(epsilon_bit, 2)
    o2 = report(o2_list, lambda n0, n1: n1 if len(n1) >= len(n0) else n0)
    co2 = report(co2_list, lambda n0, n1: n0 if len(n1) >= len(n0) else n1)
    print(f'gamma value = {gamma}\nepsilon value = {epsilon}\npower consumption = {gamma * epsilon}')
    print(f'\noxygen generator rating = {o2}\nCO2 scrubber rating = {co2}\nlife support rating = {o2 * co2}')
