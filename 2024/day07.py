import itertools


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


def solve(data: str, part: int):
    r1, used = calibrate(data, ['+', '*'])
    if part == 1:
        return r1
    data = '\n'.join([line for i, line in enumerate(data.splitlines()) if i not in used])
    r2, _ = calibrate(data, ['+', '*', '||'])
    r2 += r1
    if part == 2:
        return r2
    return [r1, r2]
