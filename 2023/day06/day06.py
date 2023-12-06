import math, re

if __name__ == '__main__':
    with open('day06.txt') as log_file: 
        file_content = log_file.read().split('\n')
    times, distances = list(map(lambda line: map(int, re.findall(r'\d+', line)), file_content))
    winning_spans = []
    for time, distance in list(zip(times, distances)):
        possible_mins = list(range(math.ceil(time/2)))
        min_crack = min([n for n in possible_mins if (time - n) * n > distance])
        winning_spans.append(range(min_crack, time - min_crack + 1))
    print(f'The multiplied numbers of ways are: {math.prod([len(span) for span in winning_spans])}')
    time, distance = list(map(lambda line: int(line.split(':')[1].replace(' ', '')), file_content))
    possible_mins = list(range(math.ceil(time/2)))
    min_crack = min([n for n in possible_mins if (time - n) * n > distance])
    print(f'You can beat the race in this many ways: {len(range(min_crack, time - min_crack + 1))}')
