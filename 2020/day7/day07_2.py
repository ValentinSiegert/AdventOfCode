

rules = {}


def count_bags(color):
    if len(rules[color].keys()) == 0:
        return 1
    else:
        count = 1
        for other_color, contain_quantity in rules[color].items():
            count = count + contain_quantity * count_bags(other_color)
        return count


if __name__ == '__main__':
    with open("day7.txt") as bags_data:
        bags_rules = [line.split('\n')[0] for line in bags_data.readlines()]
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
    bags_in_shiny_gold = 0
    for color, quantity in rules['shiny gold'].items():
        bags_in_shiny_gold = bags_in_shiny_gold + quantity * count_bags(color)
    print(f'You need {bags_in_shiny_gold} other bags in a single shiny gold bag.')



