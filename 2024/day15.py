
def warehousing(data: str, part2: bool = False) -> int:
    store, program = data.split('\n\n')
    if part2:
        store = store.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    for y, row in enumerate(store := [list(row) for row in store.splitlines()]):
        if '@' in row:
            x = row.index('@')
            break
    # print(f'Initial state:\n{'\n'.join(''.join(row) for row in store)}\n')
    for move in program:
        if move == '<':
            if (next_place := store[y][x - 1]) == '#':
                continue
            elif next_place == '.':
                store[y][x], store[y][x - 1], x = '.', '@', x - 1
            else:
                dmap = [store[y][x0] for x0 in range(x, -1, -1)]
                if (next_free := dmap.index('.') if '.' in dmap else -1) == -1 or dmap.index('#') < next_free:
                    continue
                if not part2:
                    store[y][x], store[y][x - 1], store[y][x - next_free], x = '.', '@', 'O', x - 1
                else:
                    for x0 in range(x - next_free + 1, x):
                        store[y][x0] = '[' if store[y][x0] == ']' else ']'
                    store[y][x], store[y][x - 1], store[y][x - next_free], x = '.', '@', '[', x - 1
        elif move == '>':
            if (next_place := store[y][x + 1]) == '#':
                continue
            elif next_place == '.':
                store[y][x], store[y][x + 1], x = '.', '@', x + 1
            else:
                dmap = [store[y][x0] for x0 in range(x, len(store[y]))]
                if (next_free := dmap.index('.') if '.' in dmap else -1) == -1 or dmap.index('#') < next_free:
                    continue
                if not part2:
                    store[y][x], store[y][x + 1], store[y][x + next_free], x = '.', '@', 'O', x + 1
                else:
                    for x0 in range(x + 1, x + next_free):
                        store[y][x0] = '[' if store[y][x0] == ']' else ']'
                    store[y][x], store[y][x + 1], store[y][x + next_free], x = '.', '@', ']', x + 1
        elif move == '^':
            if (next_place := store[y - 1][x]) == '#':
                continue
            elif next_place == '.':
                store[y][x], store[y - 1][x], y = '.', '@', y - 1
            else:
                if not part2:
                    dmap = [store[y0][x] for y0 in range(y, -1, -1)]
                    if (next_free := dmap.index('.') if '.' in dmap else -1) == -1 or dmap.index('#') < next_free:
                        continue
                    store[y][x], store[y - 1][x], store[y - next_free][x], y = '.', '@', 'O', y - 1
                else:
                    to_check, pushable, to_push = [(x, y - 1)], True, set()
                    while pushable and len(to_check) > 0:
                        x0, y0 = to_check.pop()
                        if store[y0][x0] == '#':
                            pushable = False
                        elif store[y0][x0] == '[':
                            to_push.add((x0, y0))
                            to_check.append((x0, y0 - 1))
                            to_check.append((x0 + 1, y0 - 1))
                        elif store[y0][x0] == ']':
                            to_push.add((x0 - 1, y0))
                            to_check.append((x0, y0 - 1))
                            to_check.append((x0 - 1, y0 - 1))
                    if pushable:
                        for x0, y0 in sorted(sorted(to_push), key=lambda p: p[1]):
                            store[y0][x0], store[y0][x0 + 1], store[y0 - 1][x0], store[y0 - 1][x0 + 1] = '.', '.', '[', ']'
                        store[y][x], store[y - 1][x], y = '.', '@', y - 1
        elif move == 'v':
            if (next_place := store[y + 1][x]) == '#':
                continue
            elif next_place == '.':
                store[y][x], store[y + 1][x], y = '.', '@', y + 1
            else:
                if not part2:
                    dmap = [store[y0][x] for y0 in range(y, len(store))]
                    if (next_free := dmap.index('.') if '.' in dmap else -1 ) == -1 or dmap.index('#') < next_free:
                        continue
                    store[y][x], store[y + 1][x], store[y + next_free][x], y = '.', '@', 'O', y + 1
                else:
                    to_check, pushable, to_push = [(x, y + 1)], True, set()
                    while pushable and len(to_check) > 0:
                        x0, y0 = to_check.pop()
                        if store[y0][x0] == '#':
                            pushable = False
                        elif store[y0][x0] == '[':
                            to_push.add((x0, y0))
                            to_check.append((x0, y0 + 1))
                            to_check.append((x0 + 1, y0 + 1))
                        elif store[y0][x0] == ']':
                            to_push.add((x0 - 1, y0))
                            to_check.append((x0, y0 + 1))
                            to_check.append((x0 - 1, y0 + 1))
                    if pushable:
                        for x0, y0 in sorted(sorted(to_push), key=lambda p: p[1], reverse=True):
                            store[y0][x0], store[y0][x0 + 1], store[y0 + 1][x0], store[y0 + 1][x0 + 1] = '.', '.', '[', ']'
                        store[y][x], store[y + 1][x], y = '.', '@', y + 1
        # if move in '<>^v':
        #     print(f'Move {move}:\n{'\n'.join(''.join(row) for row in store)}\n')
    gps_sum, box_char = 0, 'O' if not part2 else '['
    for y, row in enumerate(store):
        for x, place in enumerate(row):
            if place == box_char:
                gps_sum += 100 * y + x
    # print(gps_sum)
    return gps_sum


def solve(data: str, part: int):
    # data = '########\n#..O.O.#\n##@.O..#\n#...O..#\n#.#.O..#\n#...O..#\n#......#\n########\n\n<^^>>>vv<v>>v<<'  ## 2nd example part 1
    # data = '#######\n#...#.#\n#.....#\n#..OO@#\n#..O..#\n#.....#\n#######\n\n<vv<<^^<<^^'  ## 2nd example part 2
    if part == 1:
        return warehousing(data)
    if part == 2:
        return warehousing(data, True)
    return [warehousing(data), warehousing(data, True)]
