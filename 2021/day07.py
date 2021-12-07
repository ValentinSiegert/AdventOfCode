

if __name__ == '__main__':
    puzzle_part = 'b'
    crabs = list(map(int, open('day7.txt').read().split(',')))
    crabs_pos = list(map(len, [[c for c in crabs if c == i] for i in range(0, max(crabs)+1)]))
    fuel_costs = {}
    for pos in range(0, len(crabs_pos)):
        fuel = 0
        for pos_index, crab_amount in enumerate(crabs_pos):
            if crab_amount == 0:
                continue
            distance = pos - pos_index if pos >= pos_index else pos_index - pos
            if puzzle_part == 'b':
                distance = sum([i for i in range(1, distance+1)])
            fuel += distance * crab_amount
        fuel_costs[pos] = fuel
    best_pos = min(fuel_costs, key=fuel_costs.get)
    print(f'The best position is {best_pos} with a total fuel consumption of {fuel_costs[best_pos]}.')
