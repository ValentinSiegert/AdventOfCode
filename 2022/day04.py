import re

if __name__ == '__main__':
    with open('day4.txt') as log_file:
        sub = overlap = 0
        for line in log_file:
            min1, max1, min2, max2 = map(int, re.search(r'(\d*)-(\d*),(\d*)-(\d*)', line).groups())
            sub += 1 if (min1 <= min2 and max1 >= max2) or (min2 <= min1 and max2 >= max1) else 0
            overlap += 1 if min1 <= max2 and min2 <= max1 else 0
    print(f"Part1: {sub}")
    print(f"Part2: {overlap}")

