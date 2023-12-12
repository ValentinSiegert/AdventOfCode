from functools import cache


@cache
def count_possible_rows(row: str, groups: tuple, row_id: int = 0, groups_id: int = 0, count: int = 0) -> int:
    """
    Count the possible rows that can be made from the given row and groups.
    :param row: The row to count the possible rows for.
    :param groups: The groups to use.
    :param row_id: The index of the row currently processed.
    :param groups_id: The index of the group currently processed.
    :param count: The amount of how many '#' were counted in the current group.
    :return: The amount of possible rows.
    """
    if row_id == len(row):
        return 1 if groups_id == len(groups) else 0
    elif row[row_id] == '#':
        return count_possible_rows(row, groups, row_id + 1, groups_id, count + 1)
    elif row[row_id] == '.' or groups_id == len(groups):
        if groups_id < len(groups) and count == groups[groups_id]:
            return count_possible_rows(row, groups, row_id + 1, groups_id + 1)
        elif count == 0:
            return count_possible_rows(row, groups, row_id + 1, groups_id)
        else:
            return 0
    else:
        look_ahead = count_possible_rows(row, groups, row_id + 1, groups_id, count + 1)
        if count == 0:
            look_ahead += count_possible_rows(row, groups, row_id + 1, groups_id)
        elif count == groups[groups_id]:
            look_ahead += count_possible_rows(row, groups, row_id + 1, groups_id + 1)
        return look_ahead


if __name__ == '__main__':
    with open('day12.txt') as log_file:
        possibilities_sum, possibilities_sum2 = 0, 0
        for line in log_file:
            springs, defect_groups = line.split()
            defect_groups_map = list(map(int, defect_groups.split(',')))
            possibilities_sum += count_possible_rows(springs + '.', tuple(defect_groups_map))
            possibilities_sum2 += count_possible_rows('?'.join([springs] * 5) + '.', tuple(defect_groups_map * 5))
    print(f'The sum of all possible rows is: {possibilities_sum}')
    print(f'The sum of all possible rows post unfolding is: {possibilities_sum2}')
