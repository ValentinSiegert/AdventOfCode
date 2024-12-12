def periarea(region: set[tuple[int, int]], pos: tuple[int, int], corners: set[tuple[int, int]],
             garden: list[str]) -> tuple[int, set[tuple[int, int]], set[tuple[int, int]], set[tuple[int, int]]]:
    (y0, x0), perimeter, others, rest = pos, 0, set(), set()
    for y, x in ((y0-1, x0), (y0+1, x0), (y0, x0-1), (y0, x0+1)):
        if 0 <= x < len(garden[0]) and 0 <= y < len(garden) and garden[y][x] == garden[y0][x0]:
            if (y, x) not in region:
                region.add((y, x))
                subperi, subreg, subcor, subrest = periarea(region, (y, x), corners, garden)
                perimeter, region, corners, rest = perimeter + subperi, region | subreg, corners | subcor, rest | subrest
        else:
            perimeter += 1
            others.add((y - y0, x - x0))
    if len(others) == 4:
        corners.add((y0, x0))
        corners.add((y0 + 1, x0))
        corners.add((y0 + 1, x0 - 1))
        corners.add((y0, x0 - 1))
    elif len(others) == 3:
        if others == {(0, -1), (-1, 0), (0, 1)}:  # l, u, r
            corners.add((y0, x0 - 1))
            corners.add((y0, x0))
        elif others == {(0, -1), (1, 0), (0, 1)}:  # l, d, r
            corners.add((y0 + 1, x0 - 1))
            corners.add((y0 + 1, x0))
        elif others == {(-1, 0), (1, 0), (0, 1)}: # u, d, r
            corners.add((y0, x0))
            corners.add((y0 + 1, x0))
        else:  # l, u, d
            corners.add((y0, x0 - 1))
            corners.add((y0 + 1, x0 - 1))
    elif len(others) == 2:
        if others == {(0, -1), (-1, 0)}:  # l, u
            corners.add((y0, x0 - 1))
        elif others == {(0, -1), (1, 0)}:  # l, d
            corners.add((y0 + 1, x0 - 1))
        elif others == {(-1, 0), (0, 1)}:  # u, r
            corners.add((y0, x0))
        elif others == {(1, 0), (0, 1)}:  # d, r
            corners.add((y0 + 1, x0))
    if (0 <= x0 - 1 and 0 <= y0 - 1
            and garden[y0 - 1][x0 - 1] == garden[y0][x0] == garden[y0 - 1][x0] != garden[y0][x0 - 1]):  # inner corner down left
        corners.add((y0, x0 - 1))
    if (0 <= y0 - 1 and x0 + 1 < len(garden[0]) and
            (garden[y0 - 1][x0] == garden[y0][x0] == garden[y0 - 1][x0 + 1] != garden[y0][x0 + 1] or
             garden[y0][x0] == garden[y0 - 1][x0] == garden[y0][x0 + 1] != garden[y0 - 1][x0 + 1] or
             garden[y0][x0] == garden[y0][x0 + 1] == garden[y0 - 1][x0 + 1] != garden[y0 - 1][x0])):  # inner corner down right, up right, up left
        corners.add((y0, x0))
    if (0 <= y0 - 1 and 0 <= x0 - 1 and garden[y0 - 1][x0 - 1] == garden[y0][x0] and
            garden[y0][x0] != garden[y0][x0 - 1] and garden[y0][x0] != garden[y0 - 1][x0]): # overlapping corner up left
        rest.add((y0 - 1, x0 - 1))
    if (0 <= x0 - 1 and y0 + 1 < len(garden) and garden[y0 + 1][x0 - 1] == garden[y0][x0] and
            garden[y0][x0] != garden[y0][x0 - 1] and garden[y0][x0] != garden[y0 + 1][x0]): # overlapping corner down left
        rest.add((y0 + 1, x0 - 1))
    return perimeter, region, corners, rest


def solve(data: str, part: int):
    regions, garden = [], data.splitlines()
    for y, row in enumerate(garden):
        for x, c in enumerate(row):
            if not any((y, x) in region[1] for region in regions):
                regions.append(periarea({(y, x)}, (y, x), set(), garden))
    r1 = sum(region[0] * len(region[1]) for region in regions)
    for  idr, (_, _, _, rests) in enumerate(regions):  # remove overlapping corners which are in actually in other regions and thus not overlapping
        new_rests = []
        for rest in rests:
            y1, x1 = rest
            if not any((y1, x1) in region[1] for region in regions[:idr] + regions[idr+1:]):
                new_rests.append(rest)
        regions[idr] = (regions[idr][0], regions[idr][1], regions[idr][2], new_rests)
    r2 = sum(len(region[1]) * (len(region[2]) + len(region[3])) for region in regions)
    if part == 1:
        return r1
    if part == 2:
        return r2
    return [r1, r2]
