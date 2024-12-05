INSERTION_SORT = True


def ordered_update_middle(update: list[int], rules: dict[int, set[int]]) -> int:
    if INSERTION_SORT:
        sorted_update = [update[0]]
        for u in update[1:]:
            first_possible = 0
            for idx, su in enumerate(sorted_update):
                if u in rules.get(su, []):
                    first_possible = max(first_possible, idx + 1)
            sorted_update.insert(first_possible, u)
        return sorted_update[len(update) // 2]
    else:
        sorted_indexes, changed_index = {u: i for i, u in enumerate(update)}, True
        while changed_index:
            changed_index = False
            for u in update:
                if u in rules:
                    for r in rules[u]:
                        if r in sorted_indexes and sorted_indexes[r] < sorted_indexes[u]:
                            sorted_indexes[r], sorted_indexes[u] = sorted_indexes[u], sorted_indexes[r]
                            changed_index = True
        update.sort(key=lambda x: sorted_indexes[x])
        return update[len(update) // 2]


def updates_middle_sum(data: str):
    rules_str, updates_str = data.split('\n\n')
    rules, updates = {}, [list(map(int, u.split(','))) for u in updates_str.splitlines()]
    for rule in rules_str.splitlines():
        x, y = rule.split('|')
        rules[int(x)] = {int(y)} if int(x) not in rules else rules[int(x)].union({int(y)})
    del rules_str, updates_str, rule, x, y  # Clean up for debugger past data processing
    sum_ordered_updates = sum_disordered_updates = 0
    for update in updates:
        update_in_order = True
        for i, u in enumerate(update):
            if u in rules and not set(update[:i]).isdisjoint(rules[u]):
                update_in_order = False
                break
        if update_in_order:
            sum_ordered_updates += update[len(update) // 2]
        else:
            sum_disordered_updates += ordered_update_middle(update, rules)
    return sum_ordered_updates, sum_disordered_updates


def solve(data: str, part: int):
    if part == 1:
        return updates_middle_sum(data)[0]
    if part == 2:
        return updates_middle_sum(data)[1]
    return updates_middle_sum(data)
