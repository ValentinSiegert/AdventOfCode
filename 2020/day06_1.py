

if __name__ == '__main__':
    with open("day6.txt") as customs_data:
        customs_list = [line[:-1] for line in customs_data.readlines()]
        customs_list.append('')
    yes_count = 0
    groups_yes = set()
    for line in customs_list:
        if line != '':
            for char in line:
                groups_yes.add(char)
        else:
            yes_count = yes_count + len(groups_yes)
            groups_yes = set()
    print(f'The flight gave you {yes_count} yes answers at their customs declaration forms.')



