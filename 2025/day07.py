
def tachyon(data: str) -> tuple[int, int]:
    beams, new_beams, splitter = {((lines:=data.splitlines())[0].index('S'), 1): 1}, {}, 0
    for index in range(1, len(lines)):
        for point in beams:
            if lines[index][point[0]] == '^':
                splitter += 1
                new_beams[(point[0] - 1, index + 1)] = new_beams[(point[0] - 1, index + 1)] + beams[point] if (point[0] - 1, index + 1) in new_beams else beams[point]
                new_beams[(point[0] + 1, index + 1)] = new_beams[(point[0] + 1, index + 1)] + beams[point] if (point[0] + 1, index + 1) in new_beams else beams[point]
            else:
                new_beams[(point[0], index + 1)] = new_beams[(point[0], index + 1)] + beams[point] if (point[0], index + 1) in new_beams else beams[point]
        beams, new_beams = new_beams.copy(), {}
    return splitter, sum(beams.values())


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return tachyon(data)[0]
    if part == 2:
        return tachyon(data)[1]
    return tachyon(data)
