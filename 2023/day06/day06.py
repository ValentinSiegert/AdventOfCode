import math, re


def find_race_range(t: int, d: int) -> range:
    """
    First solution searching for the minimum holding true on (time-x) * x > distance.
    Due to the symmetry of the problem we can then find the  maximum by subtracting the offset of the found minimum to 
    zero from the maximal time.
    :param t: The time for the race.
    :param d: The distance to be covered. Thus, the record to break.
    :return: The range of possible times holding the boat's button to beat the record.
    """
    possible_minimums = list(range(math.ceil(t / 2)))  # The minimum is always smaller than half the race time.
    min_crack = min([n for n in possible_minimums if (t - n) * n > d])
    return range(min_crack, t - min_crack + 1)


def find_race_range_by_zeros(t: int, d: int) -> range:
    """
    Second solution creates the range of possible times holding the boat's button by making use of the midnight formula.
    The quadratic formula to solve is -x**2 + t*x - d = 0.
    :param t: The time for the race.
    :param d: The distance to be covered. Thus, the record to break.
    :return: The range of possible times holding the boat's button to beat the record.
    """
    midnight_positive = int(math.floor((-t + math.sqrt(t ** 2 - 4 * d)) / -2)) + 1
    midnight_negative = int(math.floor((-t - math.sqrt(t ** 2 - 4 * d)) / -2))
    return range(midnight_positive, midnight_negative + 1)


if __name__ == '__main__':
    ZEROS = True  # Set to False for first solution and True for second solution.
    with open('day06.txt') as log_file:
        file_content = log_file.read().split('\n')
    times, distances = list(map(lambda line: map(int, re.findall(r'\d+', line)), file_content))
    winning_spans = []
    for time, distance in list(zip(times, distances)):
        not ZEROS and winning_spans.append(find_race_range(time, distance))
        ZEROS and winning_spans.append(find_race_range_by_zeros(time, distance))
    print(f'The multiplied numbers of ways are: {math.prod([len(span) for span in winning_spans])}')
    time, distance = list(map(lambda line: int(line.split(':')[1].replace(' ', '')), file_content))
    not ZEROS and print(f'You can beat the race in this many ways: {len(find_race_range(time, distance))}')
    ZEROS and print(f'You can beat the race in this many ways: {len(find_race_range_by_zeros(time, distance))}')
