

def unlock(data: str, p2: bool = False, lock_position: int = 50) -> int:
    zero_count, at_zero = 0, lock_position == 0
    for i,line in enumerate(data.splitlines()):
        line = line.replace('R', '+').replace('L', '-')
        zero_count += overs if p2 and (overs := int(line[1:-2] or 0)) else 0
        over = lock_position + int(f'{line[0]}{line[-2:]}' if len(line) > 2 else line)
        lock_position = (lock_position + int(line)) % 100
        zero_count += 1 if (p2 and not at_zero and (100 < over or over < 0)) or (at_zero := lock_position == 0) else 0
    return zero_count


def solve(data: str, part: int) -> int | tuple[int,int]:
    if part == 1:
        return unlock(data)
    if part == 2:
        return unlock(data,True)
    return unlock(data), unlock(data,True)
