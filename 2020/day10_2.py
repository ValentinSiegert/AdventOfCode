adapter_tree = {}

def traverse(index):
    if len(adapter_tree[index]) == 3:
        return traverse(adapter_tree[index][0]) + traverse(adapter_tree[index][1]) + traverse(adapter_tree[index][2])
    elif len(adapter_tree[index]) == 2:
        return traverse(adapter_tree[index][0]) + traverse(adapter_tree[index][1])
    elif len(adapter_tree[index]) == 1:
        return traverse(adapter_tree[index][0])
    elif len(adapter_tree[index]) == 0:
        return 1
    else:
        raise RuntimeError(f'The index {index} has too much childs!')


if __name__ == '__main__':
    with open("day10.txt") as data:
        adapters = [int(line.split('\n')[0]) for line in data.readlines()]
    adapters.append(0)
    adapters = sorted(adapters)
    adapters.append(adapters[-1] + 3)
    adapter_tree = {str(adapt): [] for adapt in adapters}
    for idx, key in enumerate(adapters):
        if len(adapters) - 1 >= idx + 1 and adapters[idx + 1] - key <= 3:
            adapter_tree[str(key)].append(str(adapters[idx + 1]))
        if len(adapters) - 1 >= idx + 2 and adapters[idx + 2] - key <= 3:
            adapter_tree[str(key)].append(str(adapters[idx + 2]))
        if len(adapters) - 1 >= idx + 3 and adapters[idx + 3] - key <= 3:
            adapter_tree[str(key)].append(str(adapters[idx + 3]))
    # debug_tree = adapter_tree.copy()
    # unrequired_adapters = []
    # for key, kids in adapter_tree.items():
    #     if len(kids) == 1:
    #         proxy = kids[0]
    #         for key_i, kids_i in adapter_tree.items():
    #             if key in kids_i:
    #                 kids_i.remove(key)
    #                 kids_i.append(proxy)
    #                 adapter_tree[key_i] = kids_i
    #         unrequired_adapters.append(key)
    # for unrequired in unrequired_adapters:
    #     del adapter_tree[unrequired]
    distinct_ways = traverse(min(adapter_tree.keys()))
    print(f'There a {distinct_ways} distinct ways of attaching the adapters.')
