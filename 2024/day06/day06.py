import numpy as np


def guard_pathing(data: str) -> tuple[int, int]:
    replace_dict = {'\n': ';', '.': '0', '#': '1', '^': '2'}
    field = np.rot90(np.matrix(",".join([replace_dict.get(c, c) for c in data]).replace(',;,', ';')), k=-1)
    y, x = np.where(field == 2)
    field[y, x] = 0
    guard_in_field, unique_places = True, set()
    while guard_in_field:
        x += 1
        if x[0] >= field.shape[0]:
            guard_in_field = False
            continue
        if field[y, x] == 0:
            unique_places.add((y[0], x[0]))
        elif field[y, x] == 1:
            x -= 1
            field = np.rot90(field, k=1)
            y, x = field.shape[0] - x - 1, y
            unique_places = {(field.shape[0] - x1 - 1, y1) for y1, x1 in unique_places}
    return len(unique_places), 0


def solve(data: str, part: int):
    if part == 1:
        return guard_pathing(data)[0]
    if part == 2:
        return guard_pathing(data)[1]
    return guard_pathing(data)
