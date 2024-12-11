from functools import cache

def blinking_stones(stones: list[int], blinks: int) -> int:
    """
    Iterative solution which is obviously  not work for part 2.
    :param stones: The list of stones at the beginning.
    :param blinks: How many times we will blink.
    :return: The amount of stones after all blinks.
    """
    for b in range(blinks):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            elif len(stone_str := str(stones[i])) % 2 == 0:
                first, second = stone_str[:len(stone_str) // 2], stone_str[len(stone_str) // 2:]
                stones.insert(i, int(first))
                stones[i + 1] = int(second)
                i += 1
            else:
                stones[i] *= 2024
            i += 1
    return len(stones)

@cache
def blink(stone: int, blinks: int) -> int:
    """
    Recursive solution for blinking each stone.
    :param stone: The stone at the beginning.
    :param blinks: How many times we will blink.
    :return: The amount of stones after all blinks.
    """
    if blinks == 0:
        return 1
    if stone == 0:
        return blink(1, blinks - 1)
    if len(stone_str := str(stone)) % 2 == 0:
        first, second = stone_str[:len(stone_str) // 2], stone_str[len(stone_str) // 2:]
        return blink(int(first), blinks - 1) + blink(int(second), blinks - 1)
    return blink(stone * 2024, blinks - 1)


def solve(data: str, part: int):
    stones = list(map(int, data.split()))
    r1 = blinking_stones(stones.copy(), 25)
    if part == 1:
        return r1
    r2 = sum([blink(s, 75) for s in stones])
    if part == 2:
        return r2
    return [r1, r2]
