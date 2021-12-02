
def traverse_tree_map(slope_right, slope_down):
    tree_count = 0
    with open("day3.txt") as environment:
        tree_map = [line[:-1] for line in environment.readlines()]
        end_of_map = False
        position = (0, 0)
        while not end_of_map:
            position = (position[0] + slope_right, position[1] + slope_down)
            if position[1] >= len(tree_map):
                end_of_map = True
                break
            if position[0] >= len(tree_map[position[1]]):
                position = (position[0] % len(tree_map[position[1]]), position[1])
            if tree_map[position[1]][position[0]] == '#':
                tree_count = tree_count + 1
                tree_map[position[1]] = f'{tree_map[position[1]][:position[0]]}X{tree_map[position[1]][position[0] + 1:]}'
            else:
                tree_map[position[1]] = f'{tree_map[position[1]][:position[0]]}O{tree_map[position[1]][position[0] + 1:]}'
    print(f'We encoutered {tree_count} trees with the slope right {slope_right} down {slope_down}.')
    return tree_count


if __name__ == '__main__':
    s1_1 = traverse_tree_map(1, 1)
    s3_1 = traverse_tree_map(3, 1)
    s5_1 = traverse_tree_map(5, 1)
    s7_1 = traverse_tree_map(7, 1)
    s1_2 = traverse_tree_map(1, 2)
    multiplied_count = s1_1 * s3_1 * s5_1 * s7_1 * s1_2
    print(f'Multiplied tree count over all 5 slopes is: {multiplied_count}')
