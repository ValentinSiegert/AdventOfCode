
def select_batteries(data: str, battery_amount: int) -> int:
    battery_banks, joltage = list(map(lambda x: list(map(int, list(x))), data.splitlines())), []
    for bank in battery_banks:
        battery_selection = [0] * battery_amount
        for index, battery in enumerate(bank):
            for i in range(battery_amount):
                if battery > battery_selection[i] and index < len(bank) - ((battery_amount - 1) - i):
                    battery_selection = battery_selection[:i] + [battery] + [0] * (battery_amount - i - 1)
                    break
                elif battery > battery_selection[i] and i - 1 < index < len(bank) - ((battery_amount - 1) - i):
                    battery_selection[i] = battery
                    break
        joltage.append(int(''.join(map(str, battery_selection))))
    return sum(joltage)


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return select_batteries(data, 2)
    if part == 2:
        return select_batteries(data, 12)
    return select_batteries(data, 2), select_batteries(data, 12)
