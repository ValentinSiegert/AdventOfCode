def part1(lefts, rights):
    return sum([abs(left - right) for left, right in zip(sorted(lefts), sorted(rights))])

def part2(lefts, rights):
    return sum([left * rights.count(left) for left in lefts])

def solve(data, part):
    lefts, rights = [], []
    for line in data.splitlines():
        left, right = line.split()
        lefts.append(int(left))
        rights.append(int(right))
    if part == 1:
        return part1(lefts, rights)
    if part == 2:
        return part2(lefts, rights)
    return [part1(lefts, rights), part2(lefts, rights)]
