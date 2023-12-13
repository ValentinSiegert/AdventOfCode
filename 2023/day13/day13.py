def match(row_a: str, row_b: str, smudged: bool = False) -> tuple[bool, bool]:
    """
    Checks if two rows match. If smudged is set to True, it will return False if the rows don't match and True if they
    do. The smudged value is returned as well.
    :param row_a: The first row to compare
    :param row_b: The second row to compare
    :param smudged: Whether rows before were smudged to return True of their match
    :return: Tuple of whether the rows match and whether they are smudged to do so
    """
    for row_a, row_b in zip(row_a, row_b):
        if row_a != row_b:
            if smudged:
                return False, smudged
            else:
                smudged = True
    return True, smudged


def check_mirror(pattern: list[str], transposed: bool = False, smudge: bool = False) -> int:
    """
    Calculates the mirror value within the pattern. The value is defined as either the number of columns left to
    a vertical line or the number of rows above a horizontal line multiplied by 100. Method always only searches for
    horizontal lines, if transposed is set to True, it searches for vertical lines instead.
    :param pattern: The pattern to search in
    :param transposed: If the pattern should be transposed before searching and values should be calculated vertically
    :param smudge: If the mirror has a smudge
    :return: The mirror value if found, 0 otherwise
    """
    pattern = list(map(lambda line: ''.join(line), zip(*pattern))) if transposed else pattern
    for i, row in enumerate(pattern):
        if i + 1 < len(pattern) and (match_and_smudge := match(row, pattern[i + 1]))[0]:
            until, past = pattern[:i + 1][::-1], pattern[i + 1:]
            mirror, smudge_found = [], match_and_smudge[1]
            for j in range(1, min(len(until), len(past))):
                matched, smudge_found = match(until[j], past[j], smudge_found)
                mirror.append(matched)
            if all(mirror) and smudge_found if smudge else all(mirror) and not smudge_found:
                return (i + 1) if transposed else (i + 1) * 100
    return 0


if __name__ == '__main__':
    with open('day13.txt') as log_file:
        patterns = list(map(lambda pat: pat.splitlines(), log_file.read().split('\n\n')))
    print(f"Summarizing all mirror values: "
          f"{sum(map(lambda pt: mv if (mv := check_mirror(pt)) > 0 else check_mirror(pt, True), patterns))}")
    print(f"Summarizing all mirror values with smudge: "
          f"{sum(map(lambda pt: mv if (mv := check_mirror(pt, smudge=True)) > 0 else check_mirror(pt, True, True), patterns))}")
