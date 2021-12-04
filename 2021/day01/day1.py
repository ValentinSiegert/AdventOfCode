from collections import deque

if __name__ == '__main__':
    slope = []
    last = 0
    deq = deque(maxlen=3)
    windows_slope = []
    with open('day1.txt') as log_file:
        for line in log_file:
            current = int(line)
            if last == 0:
                last = current
            else:
                if current - last > 0:
                    slope.append(1)
                else:
                    slope.append(0)
                last = current
            # part 2 from here
            for window in deq:
                if len(window) < 3:
                    window.append(current)
            if len(deq) == 3:
                if sum(deq[1]) - sum(deq[0]) > 0:
                    windows_slope.append(1)
                else:
                    windows_slope.append(0)
            deq.append([current])
    print(f'The amount of increased depth is: {sum(slope)}')
    print(f'The amount of increased depth at sliding window comparison is: {sum(windows_slope)}')
