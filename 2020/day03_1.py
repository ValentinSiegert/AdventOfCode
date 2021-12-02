
if __name__ == '__main__':
    with open("day3.txt") as environment:
        tree_map = [line[:-1] for line in environment.readlines()]
        end_of_map = False
        position = (0, 0)
        tree_count = 0
        while not end_of_map:
            position = (position[0] + 3, position[1] + 1)
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
        print(f'We encoutered {tree_count} trees with the slope right 3 down 1.')





