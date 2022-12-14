import re


def stoning():
    scan, deep, u, sr = set(), 0, 0, True
    with open('day14t.txt') as f:
        for line in f:
            org_stones = None
            for match in re.finditer(r'(?P<x>\d+),(?P<y>\d+)', line):
                next_stones = (int(match.group('x')), int(match.group('y')))
                if org_stones is not None and org_stones != next_stones:
                    if org_stones[0] == next_stones[0]:
                        range_y = range(org_stones[1], next_stones[1] + 1) if org_stones[1] < next_stones[1] else range(next_stones[1], org_stones[1] + 1)
                        scan.update([(org_stones[0], y) for y in range_y])
                    elif org_stones[1] == next_stones[1]:
                        range_x = range(org_stones[0], next_stones[0] + 1) if org_stones[0] < next_stones[0] else range(next_stones[0], org_stones[0] + 1)
                        scan.update([(x, org_stones[1]) for x in range_x])
                deep = max(deep, next_stones[1])
                org_stones = next_stones
    return scan, deep, u, sr


def sanding(d_, s, ds, part1=True):
    # if (part1 and any(e[0] == d_[0] and e[1] > d_[1] for e in s)) or (not part1):
    y_min = min(s, key=lambda x: x[1] if x[0] == d_[0] and x[1] > d_[1] else ds + 1)
    d = (d_[0], y_min[1] - 1 if y_min[0] == d_[0] else ds + 1)
    if (part1 and d[1] > ds) or ((not part1) and d[1] < 0):
        return False
    elif d[1] + 1 != ds + 2 and ((left := (d[0] - 1, d[1] + 1)) not in s):
        return sanding(left, s, ds, part1)
    elif d[1] + 1 != ds + 2 and ((right := (d[0] + 1, d[1] + 1)) not in s):
        return sanding(right, s, ds, part1)
    else:
        s.add(d)
        return True


if __name__ == '__main__':
    stones, deep_stone, units, sand_rests = stoning()
    while sand_rests:
        sand_rests = sanding((500, 0), stones, deep_stone)
        units += 1 if sand_rests else 0
    print(f"Part 1: {units}")
    stones, deep_stone, units, sand_rests = stoning()
    while sand_rests:
        sand_rests = sanding((500, 0), stones, deep_stone, False)
        units += 1 if sand_rests else 0
    print(f"Part 2: {units}")
