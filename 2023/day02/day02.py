if __name__ == '__main__':
    with open('day02.txt') as log_file:
        games = {int(line.split(':')[0].split()[1]): [
            {(draw := subset.strip().split())[1]: int(draw[0]) for subset in subsets.strip().split(',')} for subsets in
            line.strip().split(':')[1].split(';')] for line in log_file}
    game_id_sum = games_power = 0
    for game, subsets in games.items():
        add_up = True
        max_red = max_green = max_blue = 0
        for subset in subsets:
            if ('red' in subset and subset['red'] > 12) or ('green' in subset and subset['green'] > 13) or (
                    'blue' in subset and subset['blue'] > 14):
                add_up = False
            max_red = max(max_red, subset.get('red', 0))
            max_green = max(max_green, subset.get('green', 0))
            max_blue = max(max_blue, subset.get('blue', 0))
        game_id_sum += game if add_up else 0
        games_power += max_red * max_green * max_blue
    print(f'The sum of the IDs is: {game_id_sum}')
    print(f'The power of the games is: {games_power}')
