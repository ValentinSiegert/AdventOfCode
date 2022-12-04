import re

if __name__ == '__main__':
    with open('day4.txt') as log_file:
        sub = overlap = 0
        for line in log_file:
            sec1, sec2, sec3, sec4 = map(int, re.search(r'(\d*)-(\d*),(\d*)-(\d*)', line).groups())
            sub += 1 if (sec1 <= sec3 and sec2 >= sec4) or (sec3 <= sec1 and sec4 >= sec2) else 0
            overlap += 1 if sec1 <= sec4 and sec3 <= sec2 else 0
    print(f"Part1: {sub}")
    print(f"Part2: {overlap}")

