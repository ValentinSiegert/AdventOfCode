from collections import deque


if __name__ == '__main__':
    with open('day19.txt') as log_file:
        workflows_plain, parts_plain = log_file.read().split('\n\n')
        workflows = {wf[:(wx := wf.index('{'))]: wf[wx+1:-1].split(',') for wf in workflows_plain.split('\n')}
        parts = [p[1:-1].split(',') for p in parts_plain.split('\n')]
    x = m = a = s = part_sum = 0
    for part in parts:
        for e in part:
            exec(e)
        current = next_wf = 'in'
        while current not in ('A', 'R'):
            for wf in workflows[current][:-1]:
                e, next_wf = wf.split(':')
                if eval(e):
                    current = next_wf
                    break
            current = workflows[current][-1] if current != next_wf else current
        part_sum += x + m + a + s if current == 'A' else 0
    print(f'Added rating numbers: {part_sum}')
    q, distinct = deque([('in', range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001))]), 0
    while q:
        state, x_range, m_range, a_range, s_range = q.popleft()
        if state == 'R' or any(len(r) == 0 for r in (x_range, m_range, a_range, s_range)):
            continue
        elif state == 'A':
            distinct += len(x_range) * len(m_range) * len(a_range) * len(s_range)
        else:
            for wf in workflows[state]:
                if ':' not in wf:
                    q.append((wf, x_range, m_range, a_range, s_range))
                else:
                    xr, mr, ar, sr = x_range, m_range, a_range, s_range
                    e, next_wf = wf.split(':')
                    var, op, val = e[0], e[1], int(e[2:])
                    exec(f'{var}r = range({var}r.start, val) if op == "<" else range(val + 1, {var}r.stop)')
                    exec(f'{var}_range = range(val, {var}_range.stop) if op == "<" else range({var}_range.start, val + 1)')
                    q.append((next_wf, xr, mr, ar, sr))
    print(f'Distinct Combinations: {distinct}')





