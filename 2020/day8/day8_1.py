

if __name__ == '__main__':
    with open("day8.txt") as boot_data:
        boot_sequence = [line.split('\n')[0] for line in boot_data.readlines()]
    executed_lines = []
    loop_detected = False
    next_line = 0
    acc = 0
    while not loop_detected:
        line = boot_sequence[next_line]
        current = next_line
        if f'{current + 1}: {line}' in executed_lines:
            loop_detected = True
            continue
        command, value = line.split()
        value = int(value)
        if command == 'nop':
            next_line = next_line + 1
        elif command == 'acc':
            acc = acc + value
            next_line = next_line + 1
        elif command == 'jmp':
            next_line = next_line + value
        else:
            raise KeyError(f'Unknown command at line {current + 1} in boot sequence: {line}')
        executed_lines.append(f'{current + 1}: {line}')
    print(f'Execution stopped at line {next_line + 1} with an accumulator value of {acc}.')
