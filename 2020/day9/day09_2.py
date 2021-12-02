from collections import deque
from itertools import combinations


def find_wrong(data_stream, preamble=25):
    pre_deque = deque(maxlen=preamble)
    for number in data_stream:
        if len(pre_deque) == preamble:
            xmas_valid = False
            for pairs in combinations(pre_deque, 2):
                if sum(pairs) == number:
                    xmas_valid = True
            if not xmas_valid:
                print(f'Number {number} was the first number not xmas valid with a preamble of {preamble}.')
                return number
        pre_deque.append(number)


def get_contiguous_set(data_stream, target):
    numbers = []
    for number in data_stream:
        if len(numbers) < 2 or sum(numbers) + number <= target:
            numbers.append(number)
        elif sum(numbers) + number > target:
            while sum(numbers) + number > target:
                numbers = numbers[1:]
            numbers.append(number)
        if sum(numbers) == target:
            return numbers
    return numbers


if __name__ == '__main__':
    with open("day9.txt") as data:
        data_sequence = [int(line.split('\n')[0]) for line in data.readlines()]
    wrong_number = find_wrong(data_sequence)
    number_set = get_contiguous_set(data_sequence, wrong_number)
    print(f'The sum of the contiguous set first and last element is: {min(number_set) + max(number_set)}')
    print(number_set)
