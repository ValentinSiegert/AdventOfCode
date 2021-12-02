

def decode(code, possible_numbers):
    if len(possible_numbers) == 1:
        return possible_numbers[0]
    elif code[0] in ['F', 'L']:
        return decode(code[1:], possible_numbers[:len(possible_numbers)//2])
    elif code[0] in ['B', 'R']:
        return decode(code[1:], possible_numbers[len(possible_numbers)//2:])
    else:
        raise KeyError

if __name__ == '__main__':
    with open("day5.txt") as boarding_data:
        boarding_list = [line[:-1] for line in boarding_data.readlines()]
    seats = []
    for seat in boarding_list:
        row = decode(seat[:7], [i for i in range(0, 128)])
        column = decode(seat[-3:], [i for i in range(0, 8)])
        seat_id = row * 8 + column
        seats.append(seat_id)
    seats = sorted(seats)
    for seat_id in range(seats[0], seats[-1]):
        if seat_id not in seats:
            print(f'Found an empty seat with seat ID: {seat_id}')

