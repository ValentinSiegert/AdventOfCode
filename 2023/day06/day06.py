import math, re


def find_race_range(time, distance):
    possible_mins = list(range(math.ceil(time/2)))
    min_crack = min([n for n in possible_mins if (time - n) * n > distance])
    return range(min_crack, time - min_crack + 1)


if __name__ == '__main__':
    with open('day06.txt') as log_file: 
        file_content = log_file.read().split('\n')
    times, distances = list(map(lambda line: map(int, re.findall(r'\d+', line)), file_content))
    winning_spans = []
    for time, distance in list(zip(times, distances)):
        winning_spans.append(find_race_range(time, distance))
    print(f'The multiplied numbers of ways are: {math.prod([len(span) for span in winning_spans])}')
    time, distance = list(map(lambda line: int(line.split(':')[1].replace(' ', '')), file_content))
    print(f'You can beat the race in this many ways: {len(find_race_range(time, distance))}')
