def hash_str(string: str) -> int:
    """
    Hashes the given string.
    :param string: The string to hash.
    :return: The hash of the given string.
    """
    value = 0
    for character in string:
        value = ((value + ord(character)) * 17) % 256
    return value


if __name__ == '__main__':
    with open('day15.txt') as log_file:
        inits = log_file.read().split(',')
    print(f"The sum of the inits is: {sum(map(hash_str, inits))}")
    boxes = {}
    for sequence in inits:
        if '=' in sequence:
            if (box_label := hash_str((lens := sequence[:sequence.index('=')]))) in boxes:
                boxes[box_label][lens] = int(sequence[-1])
            else:
                boxes[box_label] = {lens: int(sequence[-1])}
        else:
            if (box_label := hash_str((lens := sequence[:sequence.index('-')]))) in boxes:
                if len(boxes[box_label]) > 1 and lens in boxes[box_label]:
                    boxes[box_label].pop(sequence[:sequence.index('-')])
                elif lens in boxes[box_label]:
                    boxes.pop(box_label)
        # print boxes
        #print(f'After "{sequence}":')
        #for label, box in boxes.items():
        #    print(f'Box {label}: ', end='')
        #    for lens, focal in box.items():
        #        print(f'[{lens} {focal}] ', end='')
        #    print()
        #print()
    print(f'The focusing power is: {sum((label + 1) * (slot + 1) * focal for label, box in boxes.items() for slot, focal in enumerate(box.values()))}')
