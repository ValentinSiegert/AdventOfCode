
def part1(data: str, p2: bool = False) -> int:
    beams, splitter, new_beams = {((lines:=data.splitlines())[0].index('S'), 1): 1}, 0, {}
    for index in range(1, len(lines)):
        for point in beams:
            if lines[index][point[0]] == '^':
                splitter += 1
                new_beams[(point[0] - 1, index + 1)] = new_beams[(point[0] - 1, index + 1)] + beams[point] if (point[0] - 1, index + 1) in new_beams else beams[point]
                new_beams[(point[0] + 1, index + 1)] = new_beams[(point[0] + 1, index + 1)] + beams[point] if (point[0] + 1, index + 1) in new_beams else beams[point]
            else:
                new_beams[(point[0], index + 1)] = new_beams[(point[0], index + 1)] + beams[point] if (point[0], index + 1) in new_beams else beams[point]
        beams, new_beams = new_beams.copy(), {}
    return splitter if not p2 else sum(beams.values())


def solve(data: str, part: int):
    if part == 1:
        return part1(data)
    if part == 2:
        return part1(data, True)
    return [part1(data), part1(data, True)]
