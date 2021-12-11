from collections import deque


def get_adjacent_points(structure, y_pos, x_pos):
    adjacents = [structure[y_pos - 1][x_pos] if y_pos - 1 >= 0 else 10,
                 structure[y_pos + 1][x_pos] if y_pos + 1 < len(structure) else 10,
                 structure[y_pos][x_pos - 1] if x_pos - 1 >= 0 else 10,
                 structure[y_pos][x_pos + 1] if x_pos + 1 < len(structure[y_pos]) else 10]
    return adjacents


def calc_basin_size_rec(hmap, y1, x1):
    up1, down1, left1, right1 = get_adjacent_points(hmap, y1, x1)
    up1 = calc_basin_size_rec(hmap, y1 - 1, x1) if hmap[y1][x1] < up1 < 9 else {tuple([-1, -1])}
    down1 = calc_basin_size_rec(hmap, y1 + 1, x1) if hmap[y1][x1] < down1 < 9 else {tuple([-1, -1])}
    left1 = calc_basin_size_rec(hmap, y1, x1 - 1) if hmap[y1][x1] < left1 < 9 else {tuple([-1, -1])}
    right1 = calc_basin_size_rec(hmap, y1, x1 + 1) if hmap[y1][x1] < right1 < 9 else {tuple([-1, -1])}
    return set.union({tuple([y1, x1])}, up1, down1, left1, right1)


def calc_basin_size(hmap, y2, x2):
    return len(calc_basin_size_rec(hmap, y2, x2)) - 1


if __name__ == '__main__':
    risk_level_sum = 0
    heightmap = [[i for i in map(int, line.strip())] for line in open('day9.txt').readlines()]
    basins = deque(maxlen=3)
    for y, line in enumerate(heightmap):
        for x, elem in enumerate(line):
            up, down, left, right = get_adjacent_points(heightmap, y, x)
            if elem < up and elem < down and elem < left and elem < right:
                risk_level_sum += 1 + elem
                basin_size = calc_basin_size(heightmap, y, x)
                # print(f'Found min at ({x},{y}) with {elem}, with basin size of {basin_size}.')
                if len(basins) < 3:
                    basins.append(basin_size)
                elif basins[0] < basin_size:
                    basins.append(basin_size)
                else:
                    continue
                basins = deque(sorted(basins), maxlen=3)
    print(f'The sum of the risk levels of all low points is {risk_level_sum}.')
    print(f'Multiplying together the sizes of the three largest basins is {basins[0] * basins[1] * basins[2]}.')
