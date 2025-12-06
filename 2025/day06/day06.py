from math import prod


def cephalopod_math(data: str, p2: bool = False) -> int:
    if not p2:
        math_probs = list(map(list, zip(*list(map(lambda args: list(map(int, args[1].split())) if args[0] < len(split) - 1 else args[1].split(), enumerate(split:=data.splitlines()))))))
    else:
        data = data.splitlines()
        for i in range(len(data) - 1):
            for j in range(len(data[0])):
                if data[i][j] == ' ' and any(data[k][j].isdigit() for k in range(len(data))):
                    data[i] = f'{data[i][:j]}o{data[i][j + 1:]}'
        math_probs = list(map(lambda p: list(map(lambda s: int(s.replace('o','')), [''.join(col) for col in zip(*p[:-1])])) + [p[-1]], list(map(list, zip(*list(map(lambda s: s.split(), data)))))))
    return sum(map(lambda p: prod(p[:-1]) if p[-1] == '*' else sum(p[:-1]), math_probs))


def solve(data: str, part: int):
    if part == 1:
        return cephalopod_math(data)
    if part == 2:
        return cephalopod_math(data, True)
    return [cephalopod_math(data), cephalopod_math(data, True)]
