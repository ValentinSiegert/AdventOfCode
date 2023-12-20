def add_signal(signal: str, lo: int, hi: int) -> tuple[int, int]:
    """
    Adds a signal to the low and high signals.
    :param signal: The signal to add.
    :param lo: The amount of low signals.
    :param hi: The amount of high signals.
    :return: The new amounts of low and high signals.
    """
    if signal == 'low':
        lo += 1
    elif signal == 'high':
        hi += 1
    return lo, hi


def push_button(state: dict[str, list[dict[str, str] | bool | str]], rxp: int, bt: int, conj_set: set[str]) \
        -> tuple[dict[str, list[dict[str, str] | bool | str]], int, int, int, set[str]]:
    """
    Pushes the button and returns the new module configuration and the low and high signals caused by the button.
    :param state: The module configuration state.
    :param rxp: The current number of times button has to be pushed to start the rx module.
    :param bt: The number of times button has been pushed.
    :param conj_set: The set of conjunctions that have not yet been triggered, but are required to be triggered for rx
    to start.
    :return: The new module configuration, number of low and high signals caused by the button push, the number of times
    button has to be pushed to start the rx module so far and the set of conjunctions that have not yet been triggered,
    but are required to be triggered for rx to start.
    """
    q, lo, hi, rx_started = [('low', 'button', 'broadcaster')], 1, 0, False
    while q:
        signal, producer, consumer = q.pop(0)
        to_send = []
        if consumer not in state:
            if not rx_started and consumer == 'rx' and signal == 'low':
                rx_started = True
                break
            continue
        if consumer == 'broadcaster':
            to_send = state[consumer]
        elif type(state[consumer][0]) is bool and signal == 'low':
            state[consumer][0] = not state[consumer][0]
            signal = 'high' if state[consumer][0] else 'low'
            to_send = state[consumer][1:]
        elif type(state[consumer][0]) is dict:
            state[consumer][0][producer] = signal
            signal = 'low' if all(s == 'high' for s in state[consumer][0].values()) else 'high'
            to_send = state[consumer][1:]
        for target in to_send:
            q.append((signal, consumer, target))
            # print(f'{consumer} -{signal}-> {target}')
            lo, hi = add_signal(signal, lo, hi)
        if consumer in conj_set and signal == 'high':
            conj_set.remove(consumer)
            rxp *= bt
    return state, lo, hi, rxp, conj_set


if __name__ == '__main__':
    with open('day20.txt') as log_file:
        module_cfg = {(ls := line.split('->'))[0]: ls[1].split(',') for line in
                      list(map(lambda x: x.strip().replace(' ', ''), log_file.readlines()))}
    for key in (ms := [k for k in module_cfg.keys() if k[0] in '%&']):
        module_cfg[key] = [{i: 'low' for i in [k[1:] for k, v in module_cfg.items() if key[1:] in v]}] + module_cfg[
            key] if key[0] == '&' else [False] + module_cfg[key]
    for key in ms:
        module_cfg[key[1:]] = module_cfg[key]
        del module_cfg[key]
    q, relevant = ['rx'], {}
    while q:
        current = q.pop()
        relevant[current] = [k for k, v in module_cfg.items() if current in v]
        for x in relevant[current]:
            if x not in relevant:
                q.append(x)
    lows, highs, rx_press, button, relevant_conj = 0, 0, 1, 1, {x for x in set(sum(relevant.values(), [])) if type(module_cfg[x][0]) is dict}
    while relevant_conj or button <= 1000:
        module_cfg, low, high, rx_press, relevant_conj = push_button(module_cfg, rx_press, button, relevant_conj)
        if button <= 1000:
            lows += low
            highs += high
            if button == 1000:
                print(f'Low: {lows}, High: {highs}, Total: {lows * highs}')
        button += 1
    print(f'Final state reached after {rx_press} pushes.')
