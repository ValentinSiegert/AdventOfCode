import re

if __name__ == '__main__':
    with open('day4.txt') as log_file:
        lines = log_file.read()
    reg_ex = re.compile('.+?\n\n', re.DOTALL)
    board_scores = draws = []
    for index, match in enumerate(re.findall(reg_ex, lines)):
        match = match.strip()
        if index == 0:
            draws = match.split(',')
        else:
            board = [[[cell, False] for cell in row.split()] for row in match.split('\n')]
            winning = False
            for draw_no, draw in enumerate(draws, 1):
                board = [[[cell[0], True] if cell[0] == draw or cell[1] else [cell[0], False] for cell in row] for row in board]
                for row in board:
                    if all([cell[1] for cell in row]):
                        winning = True
                board_t = [list(x) for x in zip(*board)]
                for column in board_t:
                    if all([cell[1] for cell in column]):
                        winning = True
                if winning:
                    score = sum([sum([int(cell[0]) if not cell[1] else 0 for cell in row]) for row in board]) * int(draw)
                    board_scores.append((draw_no, score, index))
                    break
    board_scores.sort(key=lambda e: e[1], reverse=True)
    board_scores.sort(key=lambda e: e[0])
    print(f'The best board is board number {board_scores[0][2]}, which wins in {board_scores[0][0]}'
          f' draws with a score of {board_scores[0][1]}.')
    board_scores.sort(key=lambda e: e[1])
    board_scores.sort(key=lambda e: e[0], reverse=True)
    print(f'The last board to win is board number {board_scores[0][2]}, which wins in {board_scores[0][0]}'
          f' draws with a score of {board_scores[0][1]}.')
        