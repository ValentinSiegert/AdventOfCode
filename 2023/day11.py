from itertools import combinations as comb


def expand_sky(sky: list, columns: list[int], rows: list[int], amount: int) -> list:
    """
    Expand the sky by inserting empty columns and rows at the specified indices.
    :param sky: The sky to expand.
    :param columns: The columns to insert.
    :param rows: The rows to insert.
    :param amount: The amount of rows/columns to have past insertion.
    :return: The expanded sky.
    """
    new_sky = sky.copy()
    for row in rows:
        for _ in range(amount - 1):
            new_sky.insert(row, sky[row])
    for col in columns:
        for i in range(len(new_sky)):
            new_sky[i] = new_sky[i][:col] + '.' * (amount - 1) + new_sky[i][col:]
    return new_sky


def expand_galaxies(galaxies: list[tuple[int, int]], columns: list[int], rows: list[int], amount: int) -> list:
    """
    Expand the galaxies by inserting empty columns and rows at the specified indices.
    :param galaxies: The galaxies to expand.
    :param columns: The columns to insert.
    :param rows: The rows to insert.
    :param amount: The amount of rows/columns to have past insertion.
    :return: The expanded galaxies.
    """
    new_galaxies = galaxies.copy()
    for row in rows:
        new_galaxies = [(gal[0], gal[1] + amount - 1) if gal[1] >= row else gal for gal in new_galaxies]
    for column in columns:
        new_galaxies = [(gal[0] + amount - 1, gal[1]) if gal[0] >= column else gal for gal in new_galaxies]
    return new_galaxies


def print_sky(sky: list) -> None:
    """
    Print the sky.
    :param sky: The sky to print.
    :return: None.
    """
    for s in sky:
        print(''.join(s))
    print('//' * len(sky[0]))


if __name__ == '__main__':
    PRINT_SKY = False
    with open('day11.txt') as log_file:
        night_sky = log_file.read().splitlines()
    PRINT_SKY and print_sky(night_sky)
    # find empty rows and columns
    empty_cols, empty_rows = list(range(len(night_sky[0]))), list(range(len(night_sky)))
    for y, sky_row in enumerate(night_sky):
        if '#' in sky_row:
            empty_rows.remove(y)
            for x, col in enumerate(sky_row):
                if col == '#' and x in empty_cols:
                    empty_cols.remove(x)
    # part 2
    all_galaxies_2 = [(x, y) for y, sky_row in enumerate(night_sky) for x, col in enumerate(sky_row) if col == '#']
    all_galaxies_2 = expand_galaxies(all_galaxies_2, empty_cols[::-1], empty_rows[::-1], 1000000)
    # part 1
    night_sky = expand_sky(night_sky, empty_cols[::-1], empty_rows[::-1], 2)
    PRINT_SKY and print_sky(night_sky)
    all_galaxies = [(x, y) for y, sky_row in enumerate(night_sky) for x, col in enumerate(sky_row) if col == '#']
    print(f'The sum of the distances between all galaxies in part 1 is: '
          f'{sum([abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1]) for gal1 , gal2 in comb(all_galaxies, 2)])}')
    print(f'The sum of the distances between all galaxies in part 2 is: '
          f'{sum([abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1]) for gal1, gal2 in comb(all_galaxies_2, 2)])}')
