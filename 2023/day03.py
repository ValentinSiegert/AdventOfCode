import math, re

if __name__ == '__main__':
    re_numbers, re_symbols, numbers, symbols = r'(\d+)', r'([^\d\.])', {}, {}
    with open('day03.txt') as log_file:
        for row, line in enumerate(log_file):
            numbers = numbers | {(m.span(), row): int(m.group()) for m in re.finditer(re_numbers, line)}
            symbols = symbols | {(m.start(), row): m.group() for m in re.finditer(re_symbols, line.strip())}
    adjacent = 0
    gears = {}
    for ((x1, x2), y), number in numbers.items():
        adjacent_points = [(xt, yt) for xt in range(x1 - 1, x2 + 1) for yt in range(y - 1, y + 2) if
                           not xt < 0 and not yt < 0 and not (xt in range(x1, x2) and yt == y)]
        for point in adjacent_points:
            if point in symbols:
                adjacent += number
                if symbols[point] == '*':
                    gears[point] = gears[point] + [number] if point in gears else [number]
                break
    print(f'The sum of the adjacent numbers to symbols is: {adjacent}')
    print(f'The sum of the gear ratios is: {sum([math.prod(gear_numbers) for gear_numbers in gears.values() if len(gear_numbers) == 2])}')

