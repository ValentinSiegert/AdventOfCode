def traverse_field(field: list[str], laser: tuple[int, int, str], visits: list[tuple[int, int, str]] = None,
                   first: bool = False) -> list[tuple[int, int, str]]:
    """
    Traverses the field and returns a list of all coordinates visited including the direction the laser was facing.
    :param field: The field to traverse.
    :param laser: The starting position and direction of the laser.
    :param visits: The list of coordinates visited.
    :param first: Whether this is the first call of the function, since then the cell needs to be checked.
    :return: The list of coordinates visited.
    """
    horizontal_stops, vertical_stops = '\\/|', '\\/-'
    x, y, direction = laser
    visits = visits if visits is not None else []
    if first:
        if field[y][x] == '\\':
            if direction == 'r':
                return traverse_field(field, (x, y, 'd'))
            elif direction == 'l':
                return traverse_field(field, (x, y, 'u'))
            elif direction == 'u':
                return traverse_field(field, (x, y, 'l'))
            elif direction == 'd':
                return traverse_field(field, (x, y, 'r'))
        elif field[y][x] == '/':
            if direction == 'r':
                return traverse_field(field, (x, y, 'u'))
            elif direction == 'l':
                return traverse_field(field, (x, y, 'd'))
            elif direction == 'u':
                return traverse_field(field, (x, y, 'r'))
            elif direction == 'd':
                return traverse_field(field, (x, y, 'l'))
        elif field[y][x] == '|' and direction in 'lr':
            return traverse_field(field, (x, y, 'u')) + traverse_field(field, (x, y, 'd'))
        elif field[y][x] == '-' and direction in 'ud':
            return traverse_field(field, (x, y, 'l')) + traverse_field(field, (x, y, 'r'))
    if laser in visits:
        return visits
    visits.append(laser)
    if direction == 'r':
        while x + 1 < len(field[y]) and field[y][x + 1] not in horizontal_stops:
            x += 1
            visits.append((x, y, direction))
        if x + 1 == len(field[y]):
            return visits
        elif field[y][x + 1] == '\\':
            return traverse_field(field, (x + 1, y, 'd'), visits)
        elif field[y][x + 1] == '/':
            return traverse_field(field, (x + 1, y, 'u'), visits)
        else:
            return traverse_field(field, (x + 1, y, 'u'), visits) + traverse_field(field, (x + 1, y, 'd'), visits)
    elif direction == 'l':
        while x - 1 >= 0 and field[y][x - 1] not in horizontal_stops:
            x -= 1
            visits.append((x, y, direction))
        if x == 0:
            return visits
        elif field[y][x - 1] == '\\':
            return traverse_field(field, (x - 1, y, 'u'), visits)
        elif field[y][x - 1] == '/':
            return traverse_field(field, (x - 1, y, 'd'), visits)
        else:
            return traverse_field(field, (x - 1, y, 'u'), visits) + traverse_field(field, (x - 1, y, 'd'), visits)
    elif direction == 'u':
        while y - 1 >= 0 and field[y - 1][x] not in vertical_stops:
            y -= 1
            visits.append((x, y, direction))
        if y == 0:
            return visits
        elif field[y - 1][x] == '\\':
            return traverse_field(field, (x, y - 1, 'l'), visits)
        elif field[y - 1][x] == '/':
            return traverse_field(field, (x, y - 1, 'r'), visits)
        else:
            return traverse_field(field, (x, y - 1, 'l'), visits) + traverse_field(field, (x, y - 1, 'r'), visits)
    elif direction == 'd':
        while y + 1 < len(field) and field[y + 1][x] not in vertical_stops:
            y += 1
            visits.append((x, y, direction))
        if y + 1 == len(field):
            return visits
        elif field[y + 1][x] == '\\':
            return traverse_field(field, (x, y + 1, 'r'), visits)
        elif field[y + 1][x] == '/':
            return traverse_field(field, (x, y + 1, 'l'), visits)
        else:
            return traverse_field(field, (x, y + 1, 'r'), visits) + traverse_field(field, (x, y + 1, 'l'), visits)


if __name__ == '__main__':
    with open('day16.txt') as log_file:
        field = log_file.read().splitlines()
    print(f'Energized tiles for init: '
          f'{(first_init := len(set((x, y) for x, y, d in traverse_field(field, (0, 0, "r"), first=True))))}')
    all_inits = ([(0, y, 'r') for y in range(1, len(field))] + [(len(field[0]) - 1, y, 'l') for y in range(len(field))]
                 + [(x, 0, 'd') for x in range(len(field[0]))] +
                 [(x, len(field) - 1, 'u') for x in range(len(field[0]))])
    most_energized = max([len(set((x, y) for x, y, d in traverse_field(field, init, first=True))) for init in all_inits]
                         + [first_init])
    print(f'Most energized tiles: {most_energized}')

