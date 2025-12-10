import numpy as np
import time
from itertools import combinations
from math import inf
from scipy.optimize import milp, LinearConstraint, Bounds


def start_machines(data: str, parts: int = 0, own_code = True, print_out: bool = False) -> int | tuple[int, int]:
    start_t = jolt_t = printer_count = 0
    for line in data.splitlines():
        if own_code and printer_count in [4, 13, 48, 59]:
            printer_count += 1
            print_out and print(f'{time.strftime("%H:%M:%S")} - Skipping line {printer_count} for being too hard')
            continue
        startup, buttons, target = (splits:= line.split())[0][1:-1], list(map(lambda b: tuple(map(int, b[1:-1].split(',') if ',' in b[1:-1] else b[1:-1])), splits[1:-1])), list(map(int, splits[-1][1:-1].split(',')))
        if parts in (0, 1):
            best = -1
            for presses in range(len(buttons) + 1):
                for combo in combinations(buttons, presses):
                    indicators = [0] * len(startup)
                    for i in range(len(startup)):
                        for button in combo:
                            indicators[i] += button.count(i)
                    if startup == ''.join(map(lambda c: '.' if c % 2 == 0 else '#', indicators)):
                        best = presses
                        break
                if best >= 0:
                    break
            start_t += best
        if parts in (0, 2) and not own_code:
            #matrix with (len(target), len(buttons))
            matrix = np.zeros((len(target), len(buttons)), dtype=float)
            for j, b in enumerate(buttons):
                for d in b:
                    matrix[d, j] += 1.0  # each press adds 1 to those dimensions
            res = milp(c=np.ones(len(buttons), dtype=float), # it is the objective to minimize sum x_i
                       integrality=np.ones(len(buttons), dtype=int), # all integer
                       constraints=LinearConstraint(matrix, lb=target, ub=target)) # constraints matrix @ x == target
            if res.success:
                jolt_t += int(res.x.round().astype(int).sum())
                printer_count += 1
                print_out and print(f'{time.strftime("%H:%M:%S")} - Line {printer_count} done, current jolt is {jolt_t}, presses: {int(res.x.round().astype(int).sum())}')
        if parts in (0, 2) and own_code:
            # sort buttons by "strength" (touch more dims first)
            buttons = sorted(buttons, key=lambda b: -len(b))
            # greedy solution to get initial upper bound
            remaining, greedy_presses = target[:], 0
            while any(r > 0 for r in remaining):
                # choose button that reduces the largest total remaining deficit
                best_btn, best_gain = None, 0
                for idx, b in enumerate(buttons):
                    gain = sum(1 for d in b if remaining[d] > 0)
                    if gain > best_gain:
                        best_btn, best_gain = idx, gain
                if best_gain == 0 or best_btn is None:
                    # no button can help further, so greedy cannot solve this instance
                    greedy_presses = inf
                    break
                # press button once
                for d in buttons[best_btn]:
                    remaining[d] = max(0, remaining[d] - 1)
                greedy_presses += 1
            best = greedy_presses
            # Precompute, for each dimension, how many buttons touch it
            # dim_coverage = [x + y for x, y in zip([0] * len(target), [1 if d in b else 0 for b in buttons for d in range(len(target))])]
            stack, seen = [(0, target, 0)], {}
            while stack:
                button_idx, remaining, presses = stack.pop()
                # fully satisfied
                if all(r == 0 for r in remaining):
                    if presses < best:
                        best = presses
                    continue
                # prune if already worse than best found or no more buttons to consider, or seen better state already
                if presses >= best or button_idx >= len(buttons) or ((prev := seen.get(key := (button_idx, tuple(remaining)))) is not None and presses >= prev):
                    continue
                seen[key] = presses
                # feasibility: some dimension needs remaining but no future button can affect it
                infeasible = False
                for d, rem in enumerate(remaining):
                    if rem > 0:
                        future_cover = 0
                        for i in range(button_idx, len(buttons)):
                            if d in buttons[i]:
                                future_cover += 1
                        if future_cover == 0:
                            infeasible = True
                            break
                if infeasible:
                    continue
                # per-dimension best gain among remaining buttons
                best_dim_gain = [0] * len(target)
                for i in range(button_idx, len(buttons)):
                    for d in set(buttons[i]):
                        # each press of button i reduces dim d by at most 1
                        if best_dim_gain[d] < 1:
                            best_dim_gain[d] = 1
                # lower bound: need at least max_d ceil(remaining[d] / best_dim_gain[d]) presses
                lb_extra = 0
                for d, rem in enumerate(remaining):
                    if rem <= 0:
                        continue
                    gain = best_dim_gain[d]
                    if gain == 0:
                        lb_extra = inf
                        break
                    need = (rem + gain - 1) // gain
                    if need > lb_extra:
                        lb_extra = need
                if presses + lb_extra >= best:
                    continue
                # 1) option: skip this button and move to next
                stack.append((button_idx + 1, remaining, presses))
                # 2) option: use this button between 1 and max_use times in one shot
                # max_use per dimension it touches, capped by current best
                max_use = inf
                b = buttons[button_idx]
                for d in set(b):
                    rem = remaining[d]
                    if rem == 0:
                        continue
                    if rem < max_use:
                        max_use = rem
                if max_use is inf:
                    max_use = int(0)
                if best < inf and max_use > best - presses:
                    max_use = best - presses
                # additional heuristic cap: do not allow a single button to be used more than max_use times
                max_use = int(min(50, max_use))
                for use in range(max_use, 0, -1):
                    new_remaining, changed = remaining[:], False
                    for d in b:
                        if new_remaining[d] > 0:
                            new_remaining[d] = max(0, new_remaining[d] - use)
                            changed = True
                    if not changed:
                        continue
                    if (new_presses := presses + use) >= best or new_remaining == remaining:
                        continue
                    stack.append((button_idx + 1, new_remaining, new_presses))
            jolt_t += int(best)
            printer_count += 1
            print_out and print(f'{time.strftime("%H:%M:%S")} - Line {printer_count} done, current jolt is {jolt_t}, best presses: {best}')
    if parts == 1:
        print_out and print(f'{time.strftime("%H:%M:%S")} - All lines done, final start is {start_t}')
        return start_t
    elif parts == 2:
        print_out and print(f'{time.strftime("%H:%M:%S")} - All lines done, final jolt is {jolt_t}')
        return jolt_t
    return start_t, jolt_t


def solve(data: str, part: int) -> int | tuple[int, int]:
    if part == 1:
        return start_machines(data, 1)
    if part == 2:
        return start_machines(data, 2, own_code=False)
    return start_machines(data, own_code=False)