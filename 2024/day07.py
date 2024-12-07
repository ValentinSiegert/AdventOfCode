import itertools
from math import log10


BRUTE_FORCE = False


def calibrate(data: str, operators: list[str]) -> tuple[int, list[int]]:
    calibration, used_lines = 0, []
    for i, equation_data in enumerate(data.splitlines()):
        result, *numbers = equation_data.split()
        result = int(result[:-1])
        for combo in itertools.product(operators, repeat=len(numbers) - 1):
            test = numbers[0] # full equation: ''.join([f'{n}{c}' for n, c in zip(numbers, combo)]) + numbers[-1]
            for n, c in zip(numbers[1:], combo):
                test = int(f'{test}{n}') if c == '||' else eval(f'{test}{c}{n}')
                if test > result:
                    break
            if test == result:
                calibration += result
                used_lines.append(i)
                break
    return calibration, used_lines


def solvable(result: int, numbers: list[int], concat: bool = False) -> bool:
    *numbers, last = numbers
    if not numbers:
        return last == result
    quant, rest = divmod(result, last)
    if rest == 0 and solvable(quant, numbers, concat):
        return True
    if (concat and (result - last) % 10 ** (int(log10(last)) + 1) == 0
        and solvable(result // 10 ** (int(log10(last)) + 1), numbers, concat)):
        return True
    return solvable(result - last, numbers, concat)


def solve(data: str, part: int):
    if BRUTE_FORCE:
        r1, used = calibrate(data, ['+', '*'])
        if part == 1:
            return r1
        data = '\n'.join([line for i, line in enumerate(data.splitlines()) if i not in used])
        r2, _ = calibrate(data, ['+', '*', '||'])
        r2 += r1
        if part == 2:
            return r2
        return [r1, r2]
    else:
        r1 = r2 = 0
        for line in data.splitlines():
            result, *numbers = line.split()
            result, numbers = int(result[:-1]), list(map(int, numbers))
            if solvable(result, numbers):
                r1 += result
            elif solvable(result, numbers, True):
                r2 += result
        r2 += r1
        if part == 1:
            return r1
        if part == 2:
            return r2
        return [r1, r2]
