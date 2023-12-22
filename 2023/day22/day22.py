if __name__ == '__main__':
    with open('day22.txt') as log_file:
        brick_snap = sorted([[list(map(int, c.split(','))) for c in line.strip().split('~')] for line in log_file],
                            key=lambda br: br[0][2])
    max_x = max_y = 0
    for (x1, y1, z1), (x2, y2, z2) in brick_snap:
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
    ground = [[(1, -1) for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    supported_by, supports = [set() for _ in range(len(brick_snap))], [set() for _ in range(len(brick_snap))]
    for bx, ((x1, y1, z1), (x2, y2, z2)) in enumerate(brick_snap):
        y1, y2 = sorted((y1, y2))
        x1, x2 = sorted((x1, x2))
        max_height = 0
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                # get the maximum height for the area of the block from the ground
                if ground[y][x][0] > max_height:
                    supported_by[bx].clear()
                    max_height = ground[y][x][0]
                # check whether block touches a new block
                if ground[y][x][0] == max_height and ground[y][x][1] >= 0:
                    supported_by[bx].add(ground[y][x][1])
        # set supports for the blocks the current block rests upon
        for supporter in supported_by[bx]:
            supports[supporter].add(bx)
        # update max height
        height = z2 - z1 + 1
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                ground[y][x] = (max_height + height, bx)
        # update block coordinates
        brick_snap[bx][0][2] = max_height
        brick_snap[bx][1][2] = max_height + height - 1
    # get the amount of blocks that can be safely disintegrated
    safe_dis = set(range(len(brick_snap)))
    for tx, touch in enumerate(supported_by.copy()):
        if len(touch) == 1:
            safe_dis.discard(touch.pop())
    print(f'Amount of safely chosen blocks to disintegrate: {len(safe_dis)}')
    # get the sum of blocks that would fall at disintegration of any block
    falling_blocks_sum = 0
    for bx in range(len(brick_snap)):
        to_check, falling = [bx], {bx}
        while to_check:
            current_bx = to_check.pop(0)
            # check wether supported blocks would fall, which only fall if they are only supported by blocks already falling)
            for supporti in supports[current_bx]:
                if len(supported_by[supporti] - falling) == 0:
                    falling.add(supporti)
                    to_check.append(supporti)
        falling_blocks_sum += len(falling) - 1
    print(f'Sum of blocks that would fall at disintegration of any block: {falling_blocks_sum}')


