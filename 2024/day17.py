import re

COMBO_OPS = ['0', '1', '2', '3', 'reg_a', 'reg_b', 'reg_c',
                 '(lambda: exec("raise ValueError(\\"Combo operand 7 is reserved, but appeared in program.\\")"))()']


def execute(prog: list[int], reg_a: int, reg_b: int, reg_c: int, outs: list[int], inst: int = 0) -> list[int]:
    while 0 <= inst < len(prog):
        lit, com = prog[inst + 1], eval(COMBO_OPS[prog[inst + 1]])
        match prog[inst]:
            case 0:  # adv
                reg_a = int(reg_a / 2 ** com)
            case 1:  # bxl
                reg_b ^= lit
            case 2:  # bst
                reg_b = com % 8
            case 3:  # jnz
                if reg_a != 0:
                    inst = lit
                    continue
            case 4:  # bxc
                reg_b ^= reg_c
            case 5:  # out
                outs.append(com % 8)
            case 6:  # bdv
                reg_b = int(reg_a / 2 ** com)
            case 7:  # cdv
                reg_c = int(reg_a / 2 ** com)
        inst += 2
    return outs


def back_execute(prog: list[int], reg_a: int, reg_b: int, reg_c: int, prog_point: int, min_a: int) -> tuple[bool, int]:
    out = -1
    if prog_point < 0:
        return True, min_a
    for bit in range(8):
        reg_a, inst = min_a << 3 | bit, 0
        while 0 <= inst < len(prog):
            lit, com = prog[inst + 1], eval(COMBO_OPS[prog[inst + 1]])
            match prog[inst]:
                case 0:  # -adv
                    reg_a >>= com
                case 1:  # -bxl
                    reg_b ^= lit
                case 2:  # -bst
                    reg_b = com & 7
                case 3:  # -jnz
                    inst = lit - 2 if reg_a != 0 else inst
                case 4:  # -bxc
                    reg_b ^= reg_c
                case 5:  # -out
                    out = com & 7
                    break
                case 6:  # -bdv
                    reg_b = reg_a >> com
                case 7:  # -cdv
                    reg_c = reg_a >> com
            inst += 2
        if out == prog[prog_point]:
            solvable, ma = back_execute(prog, reg_a, reg_b, reg_c, prog_point - 1, min_a << 3 | bit)
            if solvable:
                return True, ma
    return False, min_a


def solve(data: str, part: int):
    ra, rb, rc, prog = re.match(r'Register\sA:\s(?P<A>\d+)\sRegister\sB:\s(?P<B>\d+)\sRegister\sC:\s'
                                r'(?P<C>\d+)\s\sProgram:\s(?P<prog>[\d,]+)', data).groups()
    ra, rb, rc, prog = int(ra), int(rb), int(rc), list(map(int, prog.split(',')))
    if part == 1: return ','.join(map(str, execute(prog, ra, rb, rc, [])))
    if part == 2: return back_execute(prog, ra, rb, rc, len(prog) - 1, 0)[1]
    return [','.join(map(str, execute(prog, ra, rb, rc, []))),
            back_execute(prog, ra, rb, rc, len(prog) - 1, 0)[1]]
