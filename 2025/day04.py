
def paper_stacks(data: str, p2: bool = False) -> int:
    max_y, max_x, removed_papers, loop = len(grid := data.splitlines()), len(grid[0]), 0, True
    while loop:
        loop, accessible_papers = False, []
        for lin_nr, line in enumerate(grid):
            for col_nr in range(len(line)):
                pos, adjacent_papers = (col_nr, lin_nr), 0
                if grid[lin_nr][col_nr] != '@': continue
                for adjacent in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    if 0 <= pos[0] + adjacent[0] < max_x and 0 <= pos[1] + adjacent[1] < max_y and \
                       grid[pos[1] + adjacent[1]][pos[0] + adjacent[0]] == '@':
                        adjacent_papers += 1
                if adjacent_papers < 4:
                    accessible_papers.append(pos)
        if not p2:
            return len(accessible_papers)
        for paper in accessible_papers:
            grid[paper[1]] = grid[paper[1]][:paper[0]] + '.' + grid[paper[1]][paper[0]+1:]
            removed_papers += 1
            loop = True
    return removed_papers


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return paper_stacks(data)
    if part == 2:
        return paper_stacks(data, True)
    return paper_stacks(data), paper_stacks(data, True)
