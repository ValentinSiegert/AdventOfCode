

rules = {}


def can_contain(search, color):
    if len(rules[color].keys()) == 0:
        return False
    elif search in rules[color].keys():
        return True
    else:
        return any([can_contain(search, other_color) for other_color in rules[color].keys()])


if __name__ == '__main__':
    with open("day7.txt") as bags_data:
        bags_rules = [line.split('\n')[0] for line in bags_data.readlines()]
    colors_contain_shiny_gold = []
    for rule in bags_rules:
        source, others_str = rule.split(' bags contain ')
        if others_str == 'no other bags.':
            others = {}
        else:
            others_str = others_str.split(', ')
            others_str = [' '.join(o.split()[:-1]) for o in others_str]
            others = {item[2:]: int(item[0]) for item in others_str}
        rule_map = {source: others}
        rules.update(rule_map)
    for color in rules.keys():
        if can_contain('shiny gold', color):
            colors_contain_shiny_gold.append(color)
    print(f'Found {len(colors_contain_shiny_gold)} bags with at least one shiny gold bag.')



