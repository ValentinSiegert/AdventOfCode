
def read_packet(i, structure, v_sum, create_struct=False):
    packet_version = int(bin_packets[i:i + 3], 2)
    v_sum += packet_version
    packet_type = int(bin_packets[i + 3:i + 6], 2)
    i += 6
    packet = {'version': packet_version, 'type': packet_type}
    if packet_type == 4:
        reading_literal = 1
        literal = ''
        while reading_literal:
            reading_literal = int(bin_packets[i])
            literal += bin_packets[i + 1:i + 5]
            i += 5
        literal = int(literal, 2)
        packet['literal'] = literal
    else:
        length_type = int(bin_packets[i])
        if length_type == 0:
            length = int(bin_packets[i + 1:i + 16], 2)
            i += 16
            sum_length = 0
            sub_struct = []
            while sum_length < length:
                start_i = i
                i, v_sum = read_packet(i, sub_struct, v_sum, create_struct)
                sum_length += i - start_i
            packet['subs'] = sub_struct
        else:
            sum_packs = int(bin_packets[i + 1:i + 12], 2)
            i += 12
            count = 0
            sub_struct = []
            while count < sum_packs:
                i, v_sum = read_packet(i, sub_struct, v_sum, create_struct)
                count += 1
            packet['subs'] = sub_struct
    structure.append(packet)
    return i, v_sum


def calc_transmission(structure):
    sub_ts = []
    if 'subs' in structure.keys():
        sub_ts = [calc_transmission(s) for s in structure['subs']]
    if structure['type'] == 0:
        transmission = sum(sub_ts)
    elif structure['type'] == 1:
        transmission = 1
        for x in sub_ts:
            transmission *= x
    elif structure['type'] == 2:
        transmission = min(sub_ts)
    elif structure['type'] == 3:
        transmission = max(sub_ts)
    elif structure['type'] == 5:
        if sub_ts[0] > sub_ts[1]:
            transmission = 1
        else:
            transmission = 0
    elif structure['type'] == 6:
        if sub_ts[0] < sub_ts[1]:
            transmission = 1
        else:
            transmission = 0
    elif structure['type'] == 7:
        if sub_ts[0] == sub_ts[1]:
            transmission = 1
        else:
            transmission = 0
    else:
        transmission = structure['literal']
    return transmission


if __name__ == '__main__':
    packets = open('day16.txt').read()
    num_of_bits = len(packets) * 4
    bin_packets = bin(int(packets, 16))[2:].zfill(num_of_bits)
    c = 0
    packet_structure = []
    version_sum = 0
    c, version_sum = read_packet(c, packet_structure, version_sum)
    print(f'Sum of Versions: {version_sum}')
    print(f'Actual transmission: {calc_transmission(packet_structure[0])}')
