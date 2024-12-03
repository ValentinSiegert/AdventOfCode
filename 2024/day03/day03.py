import re

def mul(a: int, b: int):
    return a * b


def part1(data: str):
    return sum([eval(match) for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)])

def part2(data: str):
    active, muls = True, []
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", data):
        if match == "don't()":
            active = False
        elif match == "do()":
            active = True
        elif active:
            muls.append(eval(match))
    return sum(muls)

def solve(data: str, part: int):
    if part == 1:
        return part1(data)
    if part == 2:
        print(part2(data))
        return part2(data)
    return [part1(data), part2(data)]
