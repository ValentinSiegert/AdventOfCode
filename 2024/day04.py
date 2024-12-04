def find_xmas_rec(field: list[str], x: int, y: int, xmas_counter, next_letters: str = "MAS", direction: str = "") -> int:
    next_l = next_letters[0]
    if direction in ['r', ''] and x + 1 < len(field[y]) and field[y][x + 1] == next_l:
        if next_l == next_letters[-1]:
            xmas_counter += 1
        else:
            xmas_counter = find_xmas_rec(field, x + 1, y, xmas_counter, next_letters[1:], "r")
    if direction in ['d', ''] and y + 1 < len(field) and field[y + 1][x] == next_l:
        if next_l == next_letters[-1]:
            xmas_counter += 1
        else:
            xmas_counter = find_xmas_rec(field, x, y + 1, xmas_counter, next_letters[1:], "d")
    if direction in ['l', ''] and x - 1 >= 0 and field[y][x - 1] == next_l:
        if next_l == next_letters[-1]:
            xmas_counter += 1
        else:
            xmas_counter = find_xmas_rec(field, x - 1, y, xmas_counter, next_letters[1:], "l")
    if direction in ['u', ''] and y - 1 >= 0 and field[y - 1][x] == next_l:
        if next_l == next_letters[-1]:
            xmas_counter += 1
        else:
            xmas_counter = find_xmas_rec(field, x, y - 1, xmas_counter, next_letters[1:], "u")
    if direction in ['rd', ''] and x + 1 < len(field[y]) and y + 1 < len(field) and field[y + 1][x + 1] == next_l:
        if next_l == next_letters[-1]:
            xmas_counter += 1
        else:
            xmas_counter = find_xmas_rec(field, x + 1, y + 1, xmas_counter, next_letters[1:], "rd")
    if direction in ['ld', ''] and x - 1 >= 0 and y + 1 < len(field) and field[y + 1][x - 1] == next_l:
        if next_l == next_letters[-1]:
            xmas_counter += 1
        else:
            xmas_counter = find_xmas_rec(field, x - 1, y + 1, xmas_counter, next_letters[1:], "ld")
    if direction in ['lu', ''] and x - 1 >= 0 and y - 1 >= 0 and field[y - 1][x - 1] == next_l:
        if next_l == next_letters[-1]:
            xmas_counter += 1
        else:
            xmas_counter = find_xmas_rec(field, x - 1, y - 1, xmas_counter, next_letters[1:], "lu")
    if direction in ['ru', ''] and x + 1 < len(field[y]) and y - 1 >= 0 and field[y - 1][x + 1] == next_l:
        if next_l == next_letters[-1]:
            xmas_counter += 1
        else:
            xmas_counter = find_xmas_rec(field, x + 1, y - 1, xmas_counter, next_letters[1:], "ru")
    return xmas_counter


def find_xmas(field: list[str], x: int, y: int) -> int:
    counter = 0
    if x > 2 and "".join(field[y][x-3:x]) == "SAM":
        counter += 1
    if x < len(field[y]) - 3 and "".join(field[y][x+1:x+4]) == "MAS":
        counter += 1
    if y > 2 and "".join([field[y-1][x], field[y-2][x], field[y-3][x]]) == "MAS":
        counter += 1
    if y < len(field) - 3 and "".join([field[y+1][x], field[y+2][x], field[y+3][x]]) == "MAS":
        counter += 1
    if x > 2 and y > 2 and "".join([field[y-1][x-1], field[y-2][x-2], field[y-3][x-3]]) == "MAS":
        counter += 1
    if x < len(field[y]) - 3 and y < len(field) - 3 and "".join([field[y+1][x+1], field[y+2][x+2], field[y+3][x+3]]) == "MAS":
        counter += 1
    if x > 2 and y < len(field) - 3 and "".join([field[y+1][x-1], field[y+2][x-2], field[y+3][x-3]]) == "MAS":
        counter += 1
    if x < len(field[y]) - 3 and y > 2 and "".join([field[y-1][x+1], field[y-2][x+2], field[y-3][x+3]]) == "MAS":
        counter += 1
    return counter


def part1(field: list[str]):
    xmas_counter = xmas_counter_rec = 0
    for idy, line in enumerate(field):
        for idx, char in enumerate(line):
            if char == "X":
                xmas_counter_rec = find_xmas_rec(field, idx, idy, xmas_counter_rec)
                xmas_counter += find_xmas(field, idx, idy)
    if xmas_counter_rec != xmas_counter:
        raise ValueError(f"Recursion: {xmas_counter_rec}, Iteration: {xmas_counter}")
    return xmas_counter


def part2(field: list[str]):
    x_mas_counter = 0
    for idy, line in enumerate(field):
        for idx, char in enumerate(line):
            if (char == "A" and idx - 1 >= 0 and idy - 1 >= 0 and idx + 1 < len(field[idy]) and idy + 1 < len(field) and
                    {field[idy-1][idx-1], field[idy+1][idx+1]} == {field[idy-1][idx+1], field[idy+1][idx-1]} == {'M', 'S'}):
                x_mas_counter += 1
    return x_mas_counter


def solve(data: str, part: int):
    field = data.splitlines()
    if part == 1:
        return part1(field)
    if part == 2:
        return part2(field)
    return [part1(field), part2(field)]
