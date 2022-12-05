import re

if __name__ == '__main__':
    stacks1 = {f's{i}': [] for i in range(1, 10)}
    stacks2 = {f's{i}': [] for i in range(1, 10)}
    with open('day5.txt') as log_file:
        for line in log_file:
            rex1 = re.compile(r'(\s{3}|\[(?P<s1>\w)\])\s(\s{3}|\[(?P<s2>\w)\])\s(\s{3}|\[(?P<s3>\w)\])\s(\s{3}|\[(?P<s4>\w)\])\s(\s{3}|\[(?P<s5>\w)\])\s(\s{3}|\[(?P<s6>\w)\])\s(\s{3}|\[(?P<s7>\w)\])\s(\s{3}|\[(?P<s8>\w)\])\s(\s{3}|\[(?P<s9>\w)\])')
            # rex1 = re.compile(r'(\s{3}|\[(?P<s1>\w)\])\s(\s{3}|\[(?P<s2>\w)\])\s(\s{3}|\[(?P<s3>\w)\])')
            rex2 = re.compile(r'move\s(?P<a>\d*)\sfrom\s(?P<t1>\d*)\sto\s(?P<t2>\d*)')
            match1, match2 = rex1.match(line), rex2.match(line)
            if match1:
                for stack, elem in match1.groupdict().items():
                    if elem:
                        stacks1[stack].insert(0, elem)
                        stacks2[stack].insert(0, elem)
            elif match2:
                stacks1[f's{match2.group("t2")}'].extend(stacks1[f's{match2.group("t1")}'][-int(match2.group("a")):][::-1])
                stacks1[f's{match2.group("t1")}'] = stacks1[f's{match2.group("t1")}'][:-int(match2.group("a"))]
                stacks2[f's{match2.group("t2")}'].extend(stacks2[f's{match2.group("t1")}'][-int(match2.group("a")):])
                stacks2[f's{match2.group("t1")}'] = stacks2[f's{match2.group("t1")}'][:-int(match2.group("a"))]
    # print(f"Part1: {stacks['s1'][-1]+stacks['s2'][-1]+stacks['s3'][-1]}")
    print(f"Part1: {stacks1['s1'][-1] + stacks1['s2'][-1] + stacks1['s3'][-1] + stacks1['s4'][-1] + stacks1['s5'][-1] + stacks1['s6'][-1] + stacks1['s7'][-1] + stacks1['s8'][-1] + stacks1['s9'][-1]}")
    print(f"Part2: {stacks2['s1'][-1] + stacks2['s2'][-1] + stacks2['s3'][-1] + stacks2['s4'][-1] + stacks2['s5'][-1] + stacks2['s6'][-1] + stacks2['s7'][-1] + stacks2['s8'][-1] + stacks2['s9'][-1]}")