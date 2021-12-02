

if __name__ == '__main__':
    with open("day10.txt") as data:
        adapters = [int(line.split('\n')[0]) for line in data.readlines()]
    adapters = sorted(adapters)
    adapters.append(adapters[-1] + 3)
    last_adapter = 0
    jolt_diffs = {'1': 0, '2': 0, '3': 0}
    for adapter in adapters:
        diff = adapter - last_adapter
        jolt_diffs[f'{diff}'] = jolt_diffs[f'{diff}'] + 1
        last_adapter = adapter
    print(f'The result of joilt diffs in the input: {jolt_diffs}')
    print(f'The multiplication of 1-jolt differences by 3-jolt differences is {jolt_diffs["1"] * jolt_diffs["3"]}.')
