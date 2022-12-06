def find_start(step, stream):
    start = step
    for head in [stream[i:i + step] for i in range(0, len(stream))]:
        if any(head.count(c) > 1 for c in head):
            start += 1
        else:
            return start


if __name__ == '__main__':
    with open('day6.txt') as log_file:
        s = log_file.read()
        print(f"Part1: {find_start(4, s)}")
        print(f"Part2: {find_start(14, s)}")
