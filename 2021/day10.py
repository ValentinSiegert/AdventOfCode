
if __name__ == '__main__':
    opening_brackets = '([{<'
    tr = str.maketrans('()[]{}<>', ')(][}{><')
    syn_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    auto_points = {')': 1, ']': 2, '}': 3, '>': 4}
    syn_score = 0
    auto_score = []
    with open('day10.txt') as logfile:
        for line in logfile:
            stack = []
            con = False
            for bracket in line.strip():
                if bracket in opening_brackets:
                    stack.append(bracket)
                else:
                    b = stack.pop()
                    if bracket == b.translate(tr):
                        continue
                    print(f'Expected {b.translate(tr)}, but found {bracket} instead.')
                    syn_score += syn_points[bracket]
                    con = True
            if con:
                continue
            completion = 0
            try:
                while p := stack.pop():
                    p_tr = p.translate(tr)
                    completion *= 5
                    completion += auto_points[p_tr]
            except IndexError:
                pass
            finally:
                auto_score.append(completion)
    auto_score.sort()
    print(f'The total syntax error score is {syn_score}.')
    print(f'The middle score is {auto_score[int((len(auto_score) - 1) / 2)]}.')
