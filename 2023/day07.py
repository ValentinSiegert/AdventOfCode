from functools import cmp_to_key

CARD_RANKS = '23456789TJQKA'
TYPE_RANKS = ['high card', 'one pair', 'two pair', 'three of a kind', 'full house', 'four of a kind', 'five of a kind']
JOKERS = False
CARD_RANKS_JOKERS = 'J23456789TQKA'


def determine_hand_type(cards: str) -> str:
    counts = {c: cards.count(c) for c in cards}
    if JOKERS and 'J' in cards and cards.count('J') != 5:
        cards = cards.replace('J', max({k: v for k, v in counts.items() if k != 'J'}, key=counts.get))
        counts = {c: cards.count(c) for c in cards}
    if 5 in counts.values():
        return 'five of a kind'
    elif 4 in counts.values():
        return 'four of a kind'
    elif 3 in counts.values() and 2 in counts.values():
        return 'full house'
    elif 3 in counts.values():
        return 'three of a kind'
    elif list(counts.values()).count(2) == 2:
        return 'two pair'
    elif 2 in counts.values():
        return 'one pair'
    else:
        return 'high card'


def sort_hands(hand1: tuple, hand2: tuple) -> int:
    cards1, cards2 = hand1[0], hand2[0]
    type1 = determine_hand_type(cards1)
    type2 = determine_hand_type(cards2)
    if TYPE_RANKS.index(type1) < TYPE_RANKS.index(type2):
        return -1
    elif TYPE_RANKS.index(type1) > TYPE_RANKS.index(type2):
        return 1
    else:
        card_ranks = CARD_RANKS_JOKERS if JOKERS else CARD_RANKS
        for i in range(5):
            if card_ranks.index(cards1[i]) < card_ranks.index(cards2[i]):
                return -1
            elif card_ranks.index(cards1[i]) > card_ranks.index(cards2[i]):
                return 1
        return 0


if __name__ == '__main__':
    with open('day07.txt') as log_file:
        hands = {line.split()[0]: int(line.split()[1]) for line in log_file.readlines()}
    hands = dict(sorted(hands.items(), key=cmp_to_key(sort_hands)))
    print(f'The total winnings are: {sum([i * b for i, b in enumerate(hands.values(), 1)])}')
    JOKERS = True
    hands = dict(sorted(hands.items(), key=cmp_to_key(sort_hands)))
    print(f'The total winnings with jokers are: {sum([i * b for i, b in enumerate(hands.values(), 1)])}')
