import re


def execute(prog: list[int], reg_a: int, reg_b: int, reg_c: int, outs: list[int] | int) -> list[int] | int:
    combo_ops = ['0', '1', '2', '3', 'reg_a', 'reg_b', 'reg_c',
                 '(lambda: exec("raise ValueError(\\"Combo operand 7 is reserved, but appeared in program.\\")"))()']
    inst = 0
    while 0 <= inst < len(prog):
        match prog[inst]:
            case 0:  # adv
                reg_a >>= eval(combo_ops[prog[inst + 1]])
            case 1:  # bxl
                reg_b ^= prog[inst + 1]
            case 2:  # bst
                reg_b = eval(combo_ops[prog[inst + 1]]) & 7
            case 3:  # jnz
                if reg_a != 0:
                    if type(outs) is list:
                        inst = prog[inst + 1]
                        continue
                    else:
                        raise ValueError('Operation jnz is not handled in non-list mode of part 2.')
            case 4:  # bxc
                reg_b ^= reg_c
            case 5:  # out
                if type(outs) is list:
                    outs.append(eval(combo_ops[prog[inst + 1]]) & 7)
                else:
                    return eval(combo_ops[prog[inst + 1]]) & 7
            case 6:  # bdv
                reg_b = reg_a >> eval(combo_ops[prog[inst + 1]])
            case 7:  # cdv
                reg_c = reg_a >> eval(combo_ops[prog[inst + 1]])
        inst += 2
    return outs


def find_a(prog: list[int], reg_b: int, reg_c: int, prog_point: int, min_a: int) -> tuple[bool, int]:
    out = -1
    if prog_point < 0:
        return True, min_a
    for bit in range(8):
        reg_a = min_a << 3 | bit
        execute(prog, reg_a, reg_b, reg_c, out)
        if out == prog[prog_point]:
            solvable, ma = find_a(prog, reg_b, reg_c, prog_point - 1, min_a << 3 | bit)
            if solvable:
                return True, ma
    return False, min_a


def solve(data: str, part: int):
    ra, rb, rc, prog = re.match(r'Register\sA:\s(?P<A>\d+)\sRegister\sB:\s(?P<B>\d+)\sRegister\sC:\s'
                                r'(?P<C>\d+)\s\sProgram:\s(?P<prog>[\d,]+)', data).groups()
    ra, rb, rc, prog = int(ra), int(rb), int(rc), list(map(int, prog.split(',')))
    if part == 1: return ','.join(map(str, execute(prog, ra, rb, rc, [])))
    if part == 2: return find_a(prog, rb, rc, len(prog) - 1, 0)[1]
    return [','.join(map(str, execute(prog, ra, rb, rc, []))),
            find_a(prog, rb, rc, len(prog) - 1, 0)[1]]
