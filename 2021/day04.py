import re

if __name__ == '__main__':
    lines = open('day4.txt').read()
    reg_ex = re.compile('.+?\n\n', re.DOTALL)
    board_scores = draws = []
    for index, match in enumerate(re.findall(reg_ex, lines)):
        if index == 0:
            draws = match.strip().split(',')
        else:
            board = [[[cell, False] for cell in row.split()] for row in match.strip().split('\n')]
            for draw_no, draw in enumerate(draws, 1):
                board = [[[cell[0], True] if cell[0] == draw or cell[1] else [cell[0], False] for cell in row] for row in board]
                board_t = [list(x) for x in zip(*board)]
                if any([all([cell[1] for cell in row]) for row in board]) or any([all([cell[1] for cell in column]) for column in board_t]):
                    score = sum([sum([int(cell[0]) if not cell[1] else 0 for cell in row]) for row in board]) * int(draw)
                    board_scores.append((draw_no, score, index))
                    break
    board_scores.sort(key=lambda e: e[1], reverse=True)
    board_scores.sort(key=lambda e: e[0])
    print(f'The best board is board number {board_scores[0][2]}, which wins in {board_scores[0][0]} draws with a score of {board_scores[0][1]}.')
    print(f'The last board to win is board number {board_scores[-1][2]}, which wins in {board_scores[-1][0]} draws with a score of {board_scores[-1][1]}.')
        