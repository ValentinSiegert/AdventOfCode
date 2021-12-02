
if __name__ == '__main__':
    with open("day2.txt") as pwlist:
        count = [(lambda line: True if int((lambda line: (lambda line: line.split())(line)[0].split('-'))(line)[0]) <=
                                       (lambda line: line.split())(line)[2].count((lambda line: line.split())(line)[1][0])
                                       <= int((lambda line: (lambda line: line.split())(line)[0].split('-'))(line)[1])
        else False)(line) for line in pwlist.readlines()].count(True)
        print(count)
