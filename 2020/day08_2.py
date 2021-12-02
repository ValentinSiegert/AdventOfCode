

def execute(sequence):
    executed_lines = []
    program_finished = False
    loop_detected = False
    next_line = 0
    acc = 0
    while not (loop_detected or program_finished):
        line = sequence[next_line]
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
        if next_line >= len(sequence):
            program_finished = True
    if loop_detected:
        print(f'Execution stopped at line {next_line + 1} with an accumulator value of {acc}.')
        return executed_lines, False
    elif program_finished:
        print(f'##########################################################\n')
        print(f'Program finished fully with an accumulator value of {acc}.')
        return executed_lines, True


if __name__ == '__main__':
    with open("day8.txt") as boot_data:
        boot_sequence = [line.split('\n')[0] for line in boot_data.readlines()]
    executed_lines, success = execute(boot_sequence)
    potential_bugs = {}
    for line in executed_lines:
        index, command, value = line.split()
        index = int(index.split(':')[0]) - 1
        if command == 'jmp':
            potential_bugs[f'{index}'] = f'nop {value}'
        elif command == 'nop':
            potential_bugs[f'{index}'] = f'jmp {value}'
    for key, changed_line in potential_bugs.items():
        org_line = boot_sequence[int(key)]
        boot_sequence[int(key)] = changed_line
        executed_lines, success = execute(boot_sequence)
        if success:
            print(f'Finished the program with changing line {int(key) + 1}.')
            break
        else:
            boot_sequence[int(key)] = org_line




