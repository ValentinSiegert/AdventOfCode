import re

SAND_START = 500


def stoning():
    scan, deep, u, sr = set(), 0, 0, True
    with open('day14.txt') as f:
        for line in f:
            org_stones = None
            for match in re.finditer(r'(?P<x>\d+),(?P<y>\d+)', line):
                next_stones = (int(match.group('x')), int(match.group('y')))
                if org_stones is not None and org_stones != next_stones:
                    if org_stones[0] == next_stones[0]:
                        range_y = range(org_stones[1], next_stones[1] + 1) if org_stones[1] < next_stones[1] else range(next_stones[1], org_stones[1] + 1)
                        scan.update([org_stones[0] + y * 1j for y in range_y])
                    elif org_stones[1] == next_stones[1]:
                        range_x = range(org_stones[0], next_stones[0] + 1) if org_stones[0] < next_stones[0] else range(next_stones[0], org_stones[0] + 1)
                        scan.update([x + org_stones[1] * 1j for x in range_x])
                deep = max(deep, next_stones[1])
                org_stones = next_stones
    return scan, deep, u, sr


if __name__ == '__main__':
    stones, deep_stone, units, sand_rests = stoning()
    while sand_rests:
        s = SAND_START
        while True:
            if s.imag > deep_stone:
                print(f"Part 1: {units}")
                sand_rests = False
                break
            if s + 1j not in stones:
                s += 1j
                continue
            if s + 1j - 1 not in stones:
                s += 1j - 1
                continue
            if s + 1j + 1 not in stones:
                s += 1j + 1
                continue
            stones.add(s)
            units += 1
            break
    stones, deep_stone, units, sand_rests = stoning()
    while SAND_START not in stones:
        s = SAND_START
        while True:
            if s.imag > deep_stone:
                break
            if s + 1j not in stones:
                s += 1j
                continue
            if s + 1j - 1 not in stones:
                s += 1j - 1
                continue
            if s + 1j + 1 not in stones:
                s += 1j + 1
                continue
            break
        stones.add(s)
        units += 1
    print(f"Part 2: {units}")
