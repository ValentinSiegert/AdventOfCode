

if __name__ == '__main__':
    with open("day6.txt") as customs_data:
        customs_list = [line[:-1] for line in customs_data.readlines()]
        customs_list.append('')
    yes_count = 0
    groups_yes = {}
    group_size = 0
    for line in customs_list:
        if line != '':
            group_size = group_size + 1
            for char in line:
                groups_yes[char] = groups_yes[char] + 1 if char in groups_yes.keys() else 1
        else:
            for count in groups_yes.values():
                if count == group_size:
                    yes_count = yes_count + 1
            groups_yes = {}
            group_size = 0
    print(f'The flight gave you {yes_count} distinct yes answers at their customs declaration forms.')



