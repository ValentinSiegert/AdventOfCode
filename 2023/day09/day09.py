def extrapolate(history: list) -> tuple:
    """
    Extrapolate the next and previous values of a list of numbers, based on the differences between all numbers.
    :param history: The list of numbers to extrapolate.
    :return: A tuple of the previous and next extrapolated values.
    """
    diffs = [history[i] - history[i - 1] for i in range(1, len(history))]
    if all(d == 0 for d in diffs):
        return history[0], history[-1]
    else:
        prev_e, next_e = extrapolate(diffs)
        return history[0] - prev_e, next_e + history[-1]


if __name__ == '__main__':
    with open('day09.txt') as log_file:
        histories = [list(map(int, line.split())) for line in log_file.read().splitlines()]
    extrapolates = [extrapolate(history) for history in histories]
    print(f'The sum of all next extrapolated values is: {sum([e[1] for e in extrapolates])}')
    print(f'The sum of all prev extrapolated values is: {sum([e[0] for e in extrapolates])}')
