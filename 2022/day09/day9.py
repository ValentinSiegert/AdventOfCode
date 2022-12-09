import math


def tailing(hpos, tpos):
    if not (tpos[0] in range(hpos[0] - 1, hpos[0] + 2) and tpos[1] in range(hpos[1] - 1, hpos[1] + 2)):
        if abs(hpos[0] - tpos[0]) == 2 and hpos[1] == tpos[1]:
            tpos = (tpos[0] + int(math.copysign(1, hpos[0] - tpos[0])), tpos[1])
        elif abs(hpos[1] - tpos[1]) == 2 and hpos[0] == tpos[0]:
            tpos = (tpos[0], tpos[1] + int(math.copysign(1, hpos[1] - tpos[1])))
        else:
            tpos = (tpos[0] + int(math.copysign(1, hpos[0] - tpos[0])),
                    tpos[1] + int(math.copysign(1, hpos[1] - tpos[1])))
    return tpos


def snaking(snake_length, file):
    snake = [(0, 0) for _ in range(snake_length)]
    tail_pos = {(0, 0)}
    with open(file) as f:
        for ln in f:
            move, steps = ln.strip().split()
            for i in range(int(steps)):
                match move:
                    case "R":
                        snake[0] = (snake[0][0] + 1, snake[0][1])
                    case "L":
                        snake[0] = (snake[0][0] - 1, snake[0][1])
                    case "U":
                        snake[0] = (snake[0][0], snake[0][1] + 1)
                    case "D":
                        snake[0] = (snake[0][0], snake[0][1] - 1)
                for j in range(len(snake) - 1):
                    snake[j + 1] = tailing(snake[j], snake[j + 1])
                tail_pos.add(snake[-1])
    return len(tail_pos)


if __name__ == "__main__":
    print(f"Part 1: {snaking(2, 'day9.txt')}\nPart 2: {snaking(10, 'day9.txt')}")
