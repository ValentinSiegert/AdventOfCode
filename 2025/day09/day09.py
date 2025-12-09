from itertools import combinations


def point_inside(x, y, reds):
    inside = False
    for i in range(reds_amount:= len(reds)):
        (x1, y1), (x2, y2) = reds[i], reds[(i + 1) % reds_amount]
        dx, dy = x2 - x1, y2 - y1
        if dx == 0 and dy == 0:
            continue
        if ((x - x1) * dy - (y - y1) * dx) == 0 and min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            return True
        if (y1 > y) != (y2 > y):
            x_int = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            inside = not inside if x_int >= x else inside
    return inside

def rect_inside(p1, p2, poly):
    for cx, cy in (corners := [((x_min:=min(p1[0], p2[0])), (y_min:=min(p1[1], p2[1]))), ((x_max:=max(p1[0], p2[0])), y_min), (x_max, (y_max:=max(p1[1], p2[1]))), (x_min, y_max)]):
        if not point_inside(cx, cy, poly):
            return False
    for i in range(red_amounts:= len(poly)):
        e1, e2 = poly[i], poly[(i + 1) % red_amounts]
        for r1, r2 in [(corners[0], corners[1]), (corners[1], corners[2]), (corners[2], corners[3]), (corners[3], corners[0])]:
            if ((((r2[0] - r1[0]) * (e1[1] - r1[1]) - (r2[1] - r1[1]) * (e1[0] - r1[0])) * ((r2[0] - r1[0]) * (e2[1] - r1[1]) - (r2[1] - r1[1]) * (e2[0] - r1[0])) < 0) and
                    (((e2[0] - e1[0]) * (r1[1] - e1[1]) - (e2[1] - e1[1]) * (r1[0] - e1[0])) * ((e2[0] - e1[0]) * (r2[1] - e1[1]) - (e2[1] - e1[1]) * (r2[0] - e1[0])) < 0) and
                    r1 not in (e1, e2) and r2 not in (e1, e2)):
                return False
    return True


def largest_square(data: str, p2: bool = False) -> int:
    reds, largest = [tuple(int(n) for n in line.split(',')) for line in data.splitlines()], 0
    largest = 0
    for p1, p2 in combinations(reds, 2):
        if p2 and not rect_inside(p1, p2, reds):
            continue
        largest = max(largest, (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1))
    return largest


def solve(data: str, part: int):
    if part == 1:
        return largest_square(data)
    if part == 2:
        return largest_square(data, True)
    return [largest_square(data), largest_square(data, True)]
