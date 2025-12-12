
def part1(data: str) -> int:
    gifts = list(map(lambda g: sum(l.count('#') for l in g.splitlines()[1:]), (paras := data.split("\n\n"))[:-1]))
    areas = list(map(lambda a: (int((es := a.replace(':', '').replace('x', ' ').split())[0]), int(es[1]),
                                list(map(int, es[2:]))), paras[-1].splitlines()))
    return sum(1 for w, h, amounts in areas if w * h >= sum(gifts[idx] * count for idx, count in enumerate(amounts)))


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return part1(data)
    if part == 2:
        return 0
    return part1(data), 0
