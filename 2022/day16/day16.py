import re
from itertools import combinations as comb

if __name__ == "__main__":
    valves = {}
    with open("day16.txt") as f:
        for line in f:
            vl = re.findall(r"[A-Z]{2}", line)
            valves[vl[0]] = {'p': int(re.findall(r"\d+", line)[0]), 'to': vl[1:]}
    for v in valves.keys():
        valves[v]['map'] = {k: None for k in valves.keys() if k != v}
        visited, nodes = {v}, [(v, 0)]
        while any([m is None for m in valves[v]['map'].values()]):
            new_nodes = []
            for n, d in nodes:
                for m in valves[n]['to']:
                    if m not in visited:
                        valves[v]['map'][m] = d + 1
                        visited.add(m)
                        new_nodes.append((m, d + 1))
            nodes = new_nodes
    traces = [[0, 30, 'AA']]
    finals = []
    while traces:
        new_traces = []
        for t in traces:
            nexts = [k for k, v in valves.items() if v['p'] > 0 and k not in t[2:]]
            added_trace = False
            for n in nexts:
                new_time = t[1] - valves[t[-1]]['map'][n] - 1
                if new_time > 0:
                    new_traces.append([t[0] + new_time * valves[n]['p'], new_time, *t[2:], n])
                    added_trace = True
            if not added_trace:
                finals.append(t)
        traces = new_traces
    print(f"Part 1: {max(finals, key=lambda x: x[0])[0]}")
    # runners = 2
    # start = [0, 26, 'AA']
    # t, s = [start[1]] * runners, [start[2]] * runners
    # traces = [[start[0], *t, *s]]
    # del t, s
    # finals = []
    # while traces:
    #     new_traces = []
    #     for t in traces:
    #         nexti = [k for k, v in valves.items() if v['p'] > 0 and k not in t[1 + runners:]]
    #         nexts = list(comb(nexti, runners)) if not 0 < len(nexti) < 2 else [nexti + ['' for _ in range(runners - len(nexti))]]
    #         added_trace = False
    #         for n in nexts:
    #             n_ = n if (t[1] - valves[t[-2]]['map'][n[0]] - 1) * valves[n[0]]['p'] > (t[2] - valves[t[-1]]['map'][n[0]] - 1) * valves[n[0]]['p'] else [n[1], n[0]]
    #             new_times = [t[1 + i] - valves[t[-1 - (len(n_) - 1 - i)]]['map'][x] - 1 for i, x in enumerate(n_) if x]
    #             if all([times > 0 for times in new_times]):
    #                 new_traces.append([t[0] + sum([time * valves[n_[idx]]['p'] for idx, time in enumerate(new_times) if n_[idx]]), *new_times, *t[1 + len(n_):], *n_])
    #                 added_trace = True
    #         if not added_trace:
    #             finals.append(t)
    #     traces = new_traces
    # traces = [[0, 26, 26, 'AA', 'AA']]
    # finals = []
    # while traces:
    #     new_traces = []
    #     for t in traces:
    #         nexti = [k for k, v in valves.items() if v['p'] > 0 and k not in t[1 + 2:]]
    #         nexts = list(comb(nexti, 2)) if not 0 < len(nexti) < 2 else [nexti + ['' for _ in range(2 - len(nexti))]]
    #         added_trace = False
    #         for n in nexts:
    #             n_ = n if n[1] and (t[1] - valves[t[-2]]['map'][n[0]] - 1) * valves[n[0]]['p'] + (t[2] - valves[t[-1]]['map'][n[1]] - 1) * valves[n[1]]['p'] > (t[1] - valves[t[-2]]['map'][n[1]] - 1) * valves[n[1]]['p'] + (t[2] - valves[t[-1]]['map'][n[0]] - 1) * valves[n[0]]['p'] else [n[1], n[0]]
    #             new_times = [t[1 + i] - valves[t[-1 - (len(n_) - 1 - i)]]['map'][x] - 1 if x else t[1 + i] for i, x in enumerate(n_)]
    #             if all([times > 0 for times in new_times]):
    #                 new_traces.append([t[0] + sum([time * valves[n_[idx]]['p'] for idx, time in enumerate(new_times) if n_[idx]]), *new_times, *t[1 + len(n_):], *n_])
    #                 added_trace = True
    #         if not added_trace:
    #             finals.append(t)
    #     traces = new_traces
    traces = [[0, 26, 'AA']]
    finals = []
    while traces:
        new_traces = []
        for t in traces:
            nexts = [k for k, v in valves.items() if v['p'] > 0 and k not in t[2:]]
            added_trace = False
            for n in nexts:
                new_time = t[1] - valves[t[-1]]['map'][n] - 1
                if new_time > 0:
                    new_traces.append([t[0] + new_time * valves[n]['p'], new_time, *t[2:], n])
                    added_trace = True
            if not added_trace:
                finals.append(t)
        traces = new_traces
    print(f"Part 2: {max(f1[0] + f2[0] for i1, f1 in enumerate(finals) for i2, f2 in enumerate(finals)if i1 != i2)}")
