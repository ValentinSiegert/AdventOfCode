
if __name__ == '__main__':
    xy = [0, 0]
    xy2 = [0, 0, 0]
    with open('day2.log') as log_file:
        for line in log_file:
            command, slope = line.split()
            if command == 'forward':
                xy[0] = xy[0] + int(slope)
                xy2[0] = xy2[0] + int(slope)
                xy2[1] = xy2[1] + int(slope) * xy2[2]
            elif command == 'down':
                xy[1] = xy[1] + int(slope)
                xy2[2] = xy2[2] + int(slope)
            elif command == 'up':
                xy[1] = xy[1] - int(slope)
                xy2[2] = xy2[2] - int(slope)
    print(f'The final position is {xy} and thus the multiplied value is {xy[0] * xy[1]}.')
    print(f'The final position is {xy2} and thus the multiplied value is {xy2[0] * xy2[1]}.')
