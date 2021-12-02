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
        pre_deque.append(number)


if __name__ == '__main__':
    with open("day9.txt") as data:
        data_sequence = [int(line.split('\n')[0]) for line in data.readlines()]
    find_wrong(data_sequence)
