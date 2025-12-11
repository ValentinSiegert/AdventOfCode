from math import prod


def cephalopod_math(data: str, p2: bool = False) -> int:
    if not p2:
        math_probs = list(map(list, zip(*list(map(lambda args: list(map(int, args[1].split())) if args[0] < len(split) - 1 else args[1].split(), enumerate(split:=data.splitlines()))))))
    else:
        for i in range(len(split:=data.splitlines()) - 1):
            for j in range(len(split[0])):
                if split[i][j] == ' ' and any(split[k][j].isdigit() for k in range(len(split))):
                    split[i] = f'{split[i][:j]}o{split[i][j + 1:]}'
        math_probs = list(map(lambda p: list(map(lambda s: int(s.replace('o','')), [''.join(col) for col in zip(*p[:-1])])) + [p[-1]], list(map(list, zip(*list(map(lambda s: s.split(), split)))))))
    return sum(map(lambda p: prod(p[:-1]) if p[-1] == '*' else sum(p[:-1]), math_probs))


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return cephalopod_math(data)
    if part == 2:
        return cephalopod_math(data, True)
    return cephalopod_math(data), cephalopod_math(data, True)
