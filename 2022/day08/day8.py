def scenic_dim(t, d):
    sight = 0
    for o in d:
        sight += 1
        if o >= t:
            break
    return sight


if __name__ == "__main__":
    with open("day8.txt") as f:
        trees = [list(map(int, line.strip())) for line in f.readlines()]
    visible = scenic = 0
    alley_t = [0 for i in range(len(trees[0]))]
    for y, street in enumerate(trees):
        street_l = 0
        for x, tree in enumerate(street):
            if y == 0 or x == 0 or y == len(trees) - 1 or x == len(street) - 1 or street_l < tree or alley_t[x] < tree or all(t < tree for t in street[x+1:]) or all(t < tree for t in [ts[x] for ts in trees[y+1:]]):
                visible += 1
            scenic = max(scenic, scenic_dim(tree, street[x-1::-1] if x > 0 else []) * scenic_dim(tree, street[x+1:] if x+1 < len(street) else []) * scenic_dim(tree, [ts[x] for ts in trees[y-1::-1]] if y > 0 else []) * scenic_dim(tree, [ts[x] for ts in trees[y+1:]] if y+1 < len(trees) else []))
            street_l = max(street_l, tree)
        alley_t = list(map(lambda a, s: max(a, s), alley_t, street))
    print(f"Part 1: {visible}")
    print(f"Part 2: {scenic}")
