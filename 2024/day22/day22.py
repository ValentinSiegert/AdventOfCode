
def monkey_business(data: str) -> tuple[int, int]:
    numbers, n2000s, all_seqs = list(map(int, data.splitlines())), 0, {}
    for n in numbers:
        q, seqs = (10,10,10,10), set()
        for _ in range(2000):
            old_prize = n % 10
            n = (((two := (((one := ((n * 64) ^ n) % 16777216) // 32) ^ one) % 16777216) * 2048) ^ two) % 16777216
            q = q[1:] + ((new_prize := n % 10) - old_prize,)
            if q not in seqs:
                seqs.add(q)
                all_seqs[q] = all_seqs.get(q, 0) + new_prize
        n2000s += n
    return n2000s, max(all_seqs.values())


def solve(data: str, part: int):
    if part == 1:
        return monkey_business(data)[0]
    if part == 2:
        return monkey_business(data)[1]
    return monkey_business(data)
