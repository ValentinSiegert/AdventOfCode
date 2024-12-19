from functools import cache


def solve(data: str, part: int):
    towels, patterns = (data := data.split("\n\n"))[0].split(", "), data[1].splitlines()
    @cache
    def displayable(pattern: str) -> bool:
        if pattern in towels: return True
        for i in range(1, len(pattern)):
            if displayable(pattern[:i]) and displayable(pattern[i:]): return True
        return False
    if part == 1: return sum([displayable(pat) for pat in patterns])
    @cache
    def displayable_solutions(pattern: str) -> int:
        if pattern == '': return 1
        return sum(displayable_solutions(pattern[len(t):]) for t in towels if pattern.startswith(t))
    if part == 2: return sum([displayable_solutions(pat) for pat in patterns])
    return [sum([displayable(pat) for pat in patterns]), sum([displayable_solutions(pat) for pat in patterns])]
