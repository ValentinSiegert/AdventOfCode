def make_steps(point: tuple[int, int], step: int, edge: tuple[int, int], inf: bool = False) -> int:
    """
    Makes the amount steps from the given point inside the field bounded by edge.
    :param point: The point to start from.
    :param step: The amount of steps to make.
    :param edge: The maximum coordinate of the field.
    :param inf: Whether the field is seen as infinite repeating itself.
    :return: The set of points that can be reached from the given point in the given amount of steps.
    """
    points = {point}
    for s in range(step):
        q = points.copy()
        points.clear()
        for point in q:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_point = ((x := point[0] + dx), (y := point[1] + dy))
                if ((not inf and 0 <= x <= edge[0] and 0 <= y <= edge[1] and Garden[y][x] != '#') or
                        (Garden[y % (edge[1] + 1)][x % (edge[0] + 1)] != '#')):
                    points.add(new_point)
    return len(points)


if __name__ == '__main__':
    with open('day21.txt') as log_file:
        Garden = [line.strip() for line in log_file]
    max_c = (len(Garden[0]) - 1, len(Garden) - 1)
    start = next((x, y) for y, row in enumerate(Garden) for x, c in enumerate(row) if c == 'S')
    # first idea
    reaches = make_steps(start, (max_steps := 64), max_c)
    print(f'Past {max_steps} steps, the elf can reach {reaches} points.')
    # part 2 with some math from https://www.reddit.com/r/adventofcode/comments/18nevo3/2023_day_21_solutions/
    overall = 26501365
    repeats, rest = divmod(overall, square_garden := (len(Garden[0]) + len(Garden)))
    reaches_sr = make_steps(start, square_garden + rest, max_c, True)
    reaches_sr2 = make_steps(start, 2 * square_garden + rest, max_c, True)
    reaches_sr3 = make_steps(start, 3 * square_garden + rest, max_c, True)
    a = reaches_sr2
    b = reaches_sr2 - reaches_sr
    c = reaches_sr3 - 2 * reaches_sr2 + reaches_sr
    full_plot_count = a + b * (repeats - 2) + c * ((repeats - 2) * (repeats - 1) // 2)
    print(f'Past {overall} steps, the elf can reach {full_plot_count} points in the infinite garden.')


