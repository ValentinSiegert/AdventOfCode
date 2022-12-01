

if __name__ == '__main__':
    with open('day1.txt') as log_file:
        bags = [sum(list(map(int, block.split('\n')))) for block in log_file.read().split('\n\n')]
        print(f"The max calories in one bag are: {max(bags)}")
        print(f"The sum of the top3 max calories is: {sum(sorted(bags)[-3:])}")
