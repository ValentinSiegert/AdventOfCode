import sys


def get_next_pos(maze: list, pos_x: int, pos_y: int, direction: str, step: int) -> tuple[int, int, str, int]:
    """
    Get the next position of the pipe maze.
    :param maze: The pipe maze.
    :param pos_x: The current x position.
    :param pos_y: The current y position.
    :param direction: The current direction.
    :param step: The current step.
    :return: A tuple of the next position, direction, and step.
    """
    if maze[pos_y][pos_x] == '-':
        if direction == 'w':
            return pos_x - 1, pos_y, direction, step + 1
        elif direction == 'e':
            return pos_x + 1, pos_y, direction, step + 1
        else:
            sys.exit(f"Invalid direction '{direction}' for '-' pipe at position ({pos_x}, {pos_y}).")
    elif maze[pos_y][pos_x] == '|':
        if direction == 'n':
            return pos_x, pos_y - 1, direction, step + 1
        elif direction == 's':
            return pos_x, pos_y + 1, direction, step + 1
        else:
            sys.exit(f"Invalid direction '{direction}' for '|' pipe at position ({pos_x}, {pos_y}).")
    elif maze[pos_y][pos_x] == 'J':
        if direction == 's':
            return pos_x - 1, pos_y, 'w', step + 1
        elif direction == 'e':
            return pos_x, pos_y - 1, 'n', step + 1
        else:
            sys.exit(f"Invalid direction '{direction}' for 'J' pipe at position ({pos_x}, {pos_y}).")
    elif maze[pos_y][pos_x] == 'L':
        if direction == 's':
            return pos_x + 1, pos_y, 'e', step + 1
        elif direction == 'w':
            return pos_x, pos_y - 1, 'n', step + 1
        else:
            sys.exit(f"Invalid direction '{direction}' for 'L' pipe at position ({pos_x}, {pos_y}).")
    elif maze[pos_y][pos_x] == 'F':
        if direction == 'n':
            return pos_x + 1, pos_y, 'e', step + 1
        elif direction == 'w':
            return pos_x, pos_y + 1, 's', step + 1
        else:
            sys.exit(f"Invalid direction '{direction}' for 'F' pipe at position ({pos_x}, {pos_y}).")
    elif maze[pos_y][pos_x] == '7':
        if direction == 'n':
            return pos_x - 1, pos_y, 'w', step + 1
        elif direction == 'e':
            return pos_x, pos_y + 1, 's', step + 1
        else:
            sys.exit(f"Invalid direction '{direction}' for '7' pipe at position ({pos_x}, {pos_y}).")


def find_fill_starting_point(maze: list) -> tuple | None:
    """
    Find the starting point of a fill.
    :param maze: The traced pipe maze.
    :return: Either a tuple of the starting point or None if there is no starting point.
    """
    for y, pipe_row in enumerate(maze):
        for x, pipe in enumerate(pipe_row):
            if '.' in pipe:
                return x, y, pipe.index('.')
    return None


def get_next_to_visit(maze: list, visited_points: list, points_to_visit: list, out: bool, x: int, y: int, index: int) -> tuple[list, bool]:
    """
    Get the next points to visit.
    :param maze: The traced pipe maze.
    :param visited_points: The visited points.
    :param points_to_visit: The points to visit.
    :param out: Whether the fill is outside.
    :param x: The x position.
    :param y: The y position.
    :param index: The index for the 3x3 string at (x, y).
    :return: A list of to visit points.
    """
    pipe = maze[y][x]
    out = out or (index in [0,1,2] and y == 0) or (index in [6,7,8] and y == len(maze)-1) or (index in [0,3,6] and x == 0) or (index in [2,5,8] and x == len(maze[0])-1)
    # all 8 internal points
    if index not in [2,5,8] and pipe[index+1] == '.' and (x, y, index+1) not in visited_points and (x, y, index+1) not in points_to_visit:
        points_to_visit.append((x, y, index+1))
    if index not in [0,3,6] and pipe[index-1] == '.' and (x, y, index-1) not in visited_points and (x, y, index-1) not in points_to_visit:
        points_to_visit.append((x, y, index-1))
    if index not in [0,1,2] and pipe[index-3] == '.' and (x, y, index-3) not in visited_points and (x, y, index-3) not in points_to_visit:
        points_to_visit.append((x, y, index-3))
    if index not in [6,7,8] and pipe[index+3] == '.' and (x, y, index+3) not in visited_points and (x, y, index+3) not in points_to_visit:
        points_to_visit.append((x, y, index+3))
    if index in [4,5,7,8] and pipe[index-4] == '.' and (x, y, index-4) not in visited_points and (x, y, index-4) not in points_to_visit:
        points_to_visit.append((x, y, index-4))
    if index in [3,4,6,7] and pipe[index-2] == '.' and (x, y, index-2) not in visited_points and (x, y, index-2) not in points_to_visit:
        points_to_visit.append((x, y, index-2))
    if index in [1,2,4,5] and pipe[index+2] == '.' and (x, y, index+2) not in visited_points and (x, y, index+2) not in points_to_visit:
        points_to_visit.append((x, y, index+2))
    if index in [0,1,3,4] and pipe[index+4] == '.' and (x, y, index+4) not in visited_points and (x, y, index+4) not in points_to_visit:
        points_to_visit.append((x, y, index+4))
    # all 8 external points
    if index in [0,1,2] and y != 0 and maze[y-1][x][index+6] == '.' and (x, y-1, index+6) not in visited_points and (x, y-1, index+6) not in points_to_visit:
        points_to_visit.append((x, y-1, index+6))
    if index in [6,7,8] and y != len(maze)-1 and maze[y+1][x][index-6] == '.' and (x, y+1, index-6) not in visited_points and (x, y+1, index-6) not in points_to_visit:
        points_to_visit.append((x, y+1, index-6))
    if index in [0,3,6] and x != 0 and maze[y][x-1][index+2] == '.' and (x-1, y, index+2) not in visited_points and (x-1, y, index+2) not in points_to_visit:
        points_to_visit.append((x-1, y, index+2))
    if index in [2,5,8] and x != len(maze[0])-1 and maze[y][x+1][index-2] == '.' and (x+1, y, index-2) not in visited_points and (x+1, y, index-2) not in points_to_visit:
        points_to_visit.append((x+1, y, index-2))
    if index == 0 and x != 0 and y != 0 and maze[y-1][x-1][8] == '.' and (x-1, y-1, 8) not in visited_points and (x-1, y-1, 8) not in points_to_visit:
        points_to_visit.append((x-1, y-1, 8))
    if index == 2 and x != len(maze[0])-1 and y != 0 and maze[y-1][x+1][6] == '.' and (x+1, y-1, 6) not in visited_points and (x+1, y-1, 6) not in points_to_visit:
        points_to_visit.append((x+1, y-1, 6))
    if index == 6 and x != 0 and y != len(maze)-1 and maze[y+1][x-1][2] == '.' and (x-1, y+1, 2) not in visited_points and (x-1, y+1, 2) not in points_to_visit:
        points_to_visit.append((x-1, y+1, 2))
    if index == 8 and x != len(maze[0])-1 and y != len(maze)-1 and maze[y+1][x+1][0] == '.' and (x+1, y+1, 0) not in visited_points and (x+1, y+1, 0) not in points_to_visit:
        points_to_visit.append((x+1, y+1, 0))
    return points_to_visit, out


def print_maze(maze: list, in_3x3: bool = False) -> None:
    """
    Print the maze.
    :param maze: The maze.
    :param in_3x3: Whether to print the maze in 3x3.
    :return: None.
    """
    if in_3x3:
        for p_row in traced_pipes:
            print(''.join(p[:3] for p in p_row))
            print(''.join(p[3:6] for p in p_row))
            print(''.join(p[6:] for p in p_row))
    else:
        for p_row in maze:
            print(''.join(p_row))
    print('//' * len(maze[0]))


if __name__ == '__main__':
    PRINT_MAZE = True
    with open('day10ttt.txt') as log_file:
        pipes = [line for line in log_file.read().splitlines()]
    # find S position
    s_pos = (-1, -1)
    for y, pipe_row in enumerate(pipes):
        if 'S' in pipe_row:
            s_pos = (pipe_row.index('S'), y)
            break
    sys.exit("No 'S' is found in the input to be a starting position.") if s_pos == (-1, -1) else None
    # get both start directions from S
    positions, s_dir = [], ''
    if s_pos[0] != 0 and pipes[(y1 := s_pos[1])][(x1 := s_pos[0] - 1)] in '-LF':
        positions.append((x1, y1, 'w', 1))
        s_dir += 'w'
    if s_pos[0] != len(pipes[0]) - 1 and pipes[(y1 := s_pos[1])][(x1 := s_pos[0] + 1)] in '-J7':
        positions.append((x1, y1, 'e', 1))
        s_dir += 'e'
    if s_pos[1] != 0 and pipes[(y1 := s_pos[1] - 1)][(x1 := s_pos[0])] in '|7F':
        positions.append((x1, y1, 'n', 1))
        s_dir += 'n'
    if s_pos[1] != len(pipes) - 1 and pipes[(y1 := s_pos[1] + 1)][(x1 := s_pos[0])] in '|JL':
        positions.append((x1, y1, 's', 1))
        s_dir += 's'
    # exchange S with correct symbol
    if s_dir == 'we':
        s_dir = '-'
    elif s_dir == 'ns':
        s_dir = '|'
    elif s_dir == 'ws':
        s_dir = '7'
    elif s_dir == 'en':
        s_dir = 'L'
    elif s_dir == 'wn':
        s_dir = 'J'
    elif s_dir == 'es':
        s_dir = 'F'
    pipes[s_pos[1]] = pipes[s_pos[1]][:s_pos[0]] + s_dir + pipes[s_pos[1]][s_pos[0] + 1:]
    sys.exit("There are more than two possible directions adjacent to 'S'.") if len(positions) != 2 else None
    # traverse the maze
    trace = [s_pos]
    while (x1 := positions[0][0]) != (x2 := positions[1][0]) or (y1 := positions[0][1]) != (y2 := positions[1][1]):
        trace.append((x1, positions[0][1]))
        trace.append((x2, positions[1][1]))
        positions = [get_next_pos(pipes, *positions[0]), get_next_pos(pipes, *positions[1])]
    trace.append((x1, y1))
    print(f"The step distance between 'S' and the farthest point is: {positions[0][3]}")
    # create a traced pipe maze
    PRINT_MAZE and print_maze(pipes)
    traced_pipes = [[p if (i, j) in trace else '.' for i, p in enumerate(pipe_row)] for j, pipe_row in enumerate(pipes)]
    PRINT_MAZE and print_maze(traced_pipes)
    # # 2nd solution of part 2 using ray shooting and if crossed odd times, it is inside, yet currently not fully working
    # for y, pipe_row in enumerate(traced_pipes):
    #     currently_outside = True
    #     for x, pipe in enumerate(pipe_row):
    #         if pipe == '.' and currently_outside:
    #             traced_pipes[y][x] = 'O'
    #         elif pipe == '.' and not currently_outside:
    #             traced_pipes[y][x] = 'I'
    #         else:
    #             currently_outside = not currently_outside if pipe not in '-7J' else currently_outside
    #         # ray_pos = min([(d, s) for d, s in zip(['n', 'e', 's', 'w'], [y, len(pipes[0]) - x - 1, len(pipes) - y - 1, x])], key=lambda r: r[1]) if traced_pipes[y][x] == '.' else ('r', 0)
    #         # if ray_pos[0] == 'r':
    #         #     continue
    #         # else:
    #         #     crossed = 0
    #         #     for i in range(1, ray_pos[1] + 1):
    #         #         if traced_pipes[y + (i if ray_pos[0] == 's' else 0) - (i if ray_pos[0] == 'n' else 0)][x + (i if ray_pos[0] == 'e' else 0) - (i if ray_pos[0] == 'w' else 0)] not in '.0I':
    #         #             crossed += 1
    #         #     traced_pipes[y][x] = 'I' if crossed % 2 == 1 else '0'
    # PRINT_MAZE and print_maze(traced_pipes)
    # print(f'Enclosed tiles by the loop: {sum([sum([1 if p == "I" else 0 for p in pipe_row]) for pipe_row in traced_pipes])} (caution: maybe not correct result)')
    # first solution of part 2, using higher zoom of 3x3 per given pipe
    traced_pipes = [[p if (i, j) in trace else '.' for i, p in enumerate(pipe_row)] for j, pipe_row in enumerate(pipes)]
    to3 = {"|": ".#..#..#.",
           "-": "...###...",
           "L": ".#..##...",
           "J": ".#.##....",
           "7": "...##..#.",
           "F": "....##.#.",
           ".": "........."}
    traced_pipes = [[to3[p] for p in pipe_row] for pipe_row in traced_pipes]
    PRINT_MAZE and print_maze(traced_pipes, True)
    while (point := find_fill_starting_point(traced_pipes)) is not None:
        visited, to_visit, outside = [point], [], False
        to_visit, outside = get_next_to_visit(traced_pipes, visited, to_visit, outside, *point)
        while len(to_visit) > 0:
            point = to_visit.pop()
            visited.append(point)
            to_visit, outside = get_next_to_visit(traced_pipes, visited, to_visit, outside, *point)
        filling = ' ' if outside else 'I'
        for x, y, index in visited:
            traced_pipes[y][x] = f"{traced_pipes[y][x][:index]}{filling}{traced_pipes[y][x][index + 1:]}"
    PRINT_MAZE and print_maze(traced_pipes, True)
    print(f'Enclosed tiles by the loop: {sum([sum([1 if p.count("I") == 9 else 0 for p in pipe_row]) for pipe_row in traced_pipes])}')
    traced_pipes = [[p.replace('I', '.').replace(' ', '.') if p.count('I') < 9 else p for p in pipe_row] for pipe_row in traced_pipes]
    PRINT_MAZE and print_maze(traced_pipes, True)
    to2 = {".#..#..#.": "|",
              "...###...": "-",
              ".#..##...": "L",
              ".#.##....": "J",
              "...##..#.": "7",
              "....##.#.": "F",
              ".........": ".",
              "IIIIIIIII": "I"}
    traced_pipes = [[to2[p] for p in pipe_row] for pipe_row in traced_pipes]
    PRINT_MAZE and print_maze(traced_pipes)
