
def part1(data: str) -> int:
    # Implement part 1 solution here
    return 0


def part2(data: str) -> int:
    # Implement part 2 solution here
    return 0


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return part1(data)
    if part == 2:
        return part2(data)
    return part1(data), part2(data)
