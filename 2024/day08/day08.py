
def antennas_anti_nodes(data: str):
    antennas, antis, antis2, y_max, x_max = {}, set(), set(), len(data.splitlines()), len(data.splitlines()[0])
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            if char != '.':
                antennas[char] = [(y, x)] if char not in antennas else antennas[char] + [(y, x)]
    for coords in antennas.values():
        for i, coord in enumerate(coords):
            other_cords = coords[:i] + coords[i+1:]
            for other_coord in other_cords:
                antis2.add(coord)
                distance = (coord[0] - other_coord[0], coord[1] - other_coord[1])
                if (0 <= (ny := coord[0] + distance[0]) < y_max and
                        0 <= (nx := coord[1] + distance[1]) < x_max):
                    antis.add((ny, nx))
                    antis2.add((ny, nx))
                while 0 <= (ny := ny + distance[0]) < y_max and 0 <= (nx := nx + distance[1]) < x_max:
                    antis2.add((ny, nx))
    return len(antis), len(antis2)


def solve(data: str, part: int):
    r1, r2 = antennas_anti_nodes(data)
    if part == 1:
        return r1
    if part == 2:
        return r2
    return [r1, r2]
