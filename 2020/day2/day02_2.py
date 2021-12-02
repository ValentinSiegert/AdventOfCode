
if __name__ == '__main__':
    with open("day2.txt") as pwlist:
        count = [(lambda line: True if ((lambda line: line.split())(line)[2][int((lambda line: line.split())(line)[0].split('-')[0])-1] ==
                                        (lambda line: line.split())(line)[1][0] and
                                        (lambda line: line.split())(line)[2][int((lambda line: line.split())(line)[0].split('-')[1])-1] !=
                                        (lambda line: line.split())(line)[1][0]) or
                                       ((lambda line: line.split())(line)[2][int((lambda line: line.split())(line)[0].split('-')[1])-1] ==
                                        (lambda line: line.split())(line)[1][0] and
                                        (lambda line: line.split())(line)[2][int((lambda line: line.split())(line)[0].split('-')[0])-1] !=
                                        (lambda line: line.split())(line)[1][0])
        else False)(line) for line in pwlist.readlines()].count(True)
        print(count)
