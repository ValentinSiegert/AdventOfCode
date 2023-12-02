import re

if __name__ == '__main__':
    with open('day01.txt') as log_file:
        part1, part2 = 0, 0
        for line in log_file:
            # part 1
            numbers = re.findall(r'\d', line)
            part1 += int(f'{numbers[0]}{numbers[-1]}')
            # part 2
            words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            numbers = re.findall(f'(?=(\d|{"|".join(words)}))', line)
            get_num = lambda n: n if n.isdigit() else words.index(n) + 1
            part2 += int(f'{get_num(numbers[0])}{get_num(numbers[-1])}')
    print(f"All numbers summed in part1 is: {part1}")
    print(f"All numbers summed in part2 is: {part2}")
