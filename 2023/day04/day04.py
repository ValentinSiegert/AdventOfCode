if __name__ == '__main__':
    worth, cards, holdings = 0, {}, {}
    with open('day04.txt') as log_file:
        for card_number, line in enumerate(log_file, 1):
            winnings, draws = line.strip().split(':')[1].strip().split('|')
            winnings = [int(win) for win in winnings.strip().split()]
            draws = [int(draw) for draw in draws.strip().split()]
            points = sum([1 if draw in winnings else 0 for draw in draws]) - 1
            worth += 2 ** points if points >= 0 else 0
            # part 2
            cards[card_number] = (winnings, draws)
            holdings[card_number] = holdings[card_number] + 1 if card_number in holdings else 1
            copy_amount = holdings[card_number]
            for copy in range(card_number + 1, card_number + points + 2):
                holdings[copy] = holdings[copy] + copy_amount if copy in holdings else copy_amount
    print(f'In total the tickets are worth: {worth}')
    print(f'We end up with a total scratchcards: {sum(holdings.values())}')
