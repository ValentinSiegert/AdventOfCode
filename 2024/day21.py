from functools import cache

NUMPAD = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    'X': (0, 3),
    '0': (1, 3),
    'A': (2, 3),
}
CONPAD = {
    'X': (0, 0),
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}


@cache
def move_arm(arm: tuple[int,int], next_arm: tuple[int,int], bad_pos: tuple[int,int]) -> str:
    dx, dy = next_arm[0] - arm[0], next_arm[1] - arm[1]
    my, mx = 'v' * dy if dy >= 0 else '^' * -dy, '>' * dx if dx >= 0 else '<' * -dx
    if dx == 0: move_instructions = my + 'A'
    elif dy == 0: move_instructions = mx + 'A'
    else:
        ways = []
        if (next_arm[0], arm[1]) != bad_pos: ways.append(mx + my)
        if (arm[0], next_arm[1]) != bad_pos: ways.append(my + mx)
        # < is the slowest to come back to A and v is slower than ^
        move_instructions = (ways[0] if len(ways) == 1 or dx < 0 else ways[1]) + 'A'
    return move_instructions


@cache
def control_sequence_len(code: str, num_conpads: int, use_numpad: bool = False) -> int:
    if num_conpads == 0: return len(code)
    pad, code_len = NUMPAD if use_numpad else CONPAD, 0
    for button, next_button in zip('A' + code, code):
        code_len += control_sequence_len(move_arm(pad[button], pad[next_button], pad['X']), num_conpads - 1)
    return code_len


def solve(data: str, part: int):
    r1 = sum(control_sequence_len(code, 3, True) * int(code[:-1]) for code in data.splitlines())
    r2 = sum(control_sequence_len(code, 26, True) * int(code[:-1]) for code in data.splitlines())
    if part == 1: return r1
    if part == 2: return r2
    return [r1, r2]
