def tilt(direction: str, rolls: list[tuple[int, int]], stands: list[tuple[int, int]], max_xy: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Tilts the board in the given direction. All rocks move in the given direction until they hit a standing rock, the
    edge of the board, or another rolling rock.
    :param direction: The direction to tilt the board to. Can be 'north', 'south', 'west', or 'east'.
    :param rolls: The coordinates of the rolling rocks.
    :param stands: The coordinates of the standing rocks.
    :param max_xy: The maximum x and y coordinates of the board.
    :return: The coordinates of the tilted rolling rocks.
    :raises ValueError: If the direction is invalid, thus not 'north', 'south', 'west', or 'east'.
    """
    if direction == 'north':
        rolls, x_inc, y_inc = sorted(rolls, key=lambda r: r[1]), 0, -1
    elif direction == 'south':
        rolls, x_inc, y_inc = sorted(rolls, key=lambda r: r[1], reverse=True), 0, 1
    elif direction == 'west':
        rolls, x_inc, y_inc = sorted(rolls, key=lambda r: r[0]), -1, 0
    elif direction == 'east':
        rolls, x_inc, y_inc = sorted(rolls, key=lambda r: r[0], reverse=True), 1, 0
    else:
        raise ValueError(f"Invalid direction given: {direction}")
    for i, roll in enumerate(rolls):
        while (roll[0] + x_inc, roll[1] + y_inc) not in stands and (roll[0] + x_inc, roll[1] + y_inc) not in rolls and \
                0 <= roll[0] + x_inc <= max_xy[0] and 0 <= roll[1] + y_inc <= max_xy[1]:
            roll = (roll[0] + x_inc, roll[1] + y_inc)
        rolls[i] = roll
    return rolls


def north_load(rolls: list[tuple[int, int]], max_xy: tuple[int, int]) -> int:
    """
    Calculates the load of the given rolling rocks on the north support beams. The load is defined as the sum of
    (y_max + 1) - y coordinate of each rolling rock.
    :param rolls: The coordinates of the rolling rocks.
    :param max_xy: The maximum x and y coordinates of the board.
    :return: The score of the rolling rocks.
    """
    return sum(map(lambda r: max_xy[1] + 1 - r[1], rolls))


def tilt_cycle(cycles_range: range, rolls: list[tuple[int, int]],
               stands: list[tuple[int, int]], max_xy: tuple[int, int]) -> tuple[list[tuple[int, int]], int]:
    """
    Tilt the board for the given number of cycles. If a loop is found, the number of cycles is reduced to the number
    of cycles left after the loop.
    :param cycles_range: The range of cycles to tilt the board for.
    :param rolls: The coordinates of the rolling rocks.
    :param stands: The coordinates of the standing rocks.
    :param max_xy: The maximum x and y coordinates of the board.
    :return: The coordinates of the rolling rocks after the given number of cycles and the number of cycles left after
    the loop if one was found.
    """

    loops = []
    for i in cycles_range:
        rolls = tilt('north', rolls, stands, max_xy)
        print(f'Tilting north once, the north load is: {north_load(rolls, max_xy)}') if i == 0 else None
        rolls = tilt('west', rolls, stands, max_xy)
        rolls = tilt('south', rolls, stands, max_xy)
        rolls = tilt('east', rolls, stands, max_xy)
        if rolls in loops:
            print(f'Found a {(loop_size := i - loops.index(rolls))}-large loop after {i + 1} tilting cycles.')
            return rolls, (divmod(cycles - 1 - i, loop_size)[1] if loop_size > 0 else 0)
        else:
            loops.append(rolls)
    return rolls, 0


def print_board(rolls: list[tuple[int, int]], stands: list[tuple[int, int]], max_xy: tuple[int, int]) -> None:
    """
    Prints the board with the given rolling and standing rocks.
    :param rolls: The coordinates of the rolling rocks.
    :param stands: The coordinates of the standing rocks.
    :param max_xy: The maximum x and y coordinates of the board.
    """
    for y in range(max_xy[1] + 1):
        for x in range(max_xy[0] + 1):
            if (x, y) in rolls:
                print('O', end='')
            elif (x, y) in stands:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
    print()


if __name__ == '__main__':
    rounds, cubes, cycles = [], [], 1000000000
    with open('day14.txt') as log_file:
        y_max = 0
        for line in log_file:
            rounds += [(x, y_max) for x, c in enumerate(line) if c == 'O']
            cubes += [(x, y_max) for x, c in enumerate(line) if c == '#']
            y_max += 1
            x_max = len(line)
        max_xy = (x_max - 1, y_max - 1)
    rounds, rest = tilt_cycle(range(cycles), rounds, cubes, max_xy)
    print(f'Have to tilt {rest} more times.')
    if rest > 0:
        while rest > 0:
            rounds, rest = tilt_cycle(range(cycles - rest, cycles), rounds, cubes, max_xy)
            print(f'Have to tilt {rest} more times.')
    print(f'Past {cycles} tilting cycles the north load is: {north_load(rounds, max_xy)}')
