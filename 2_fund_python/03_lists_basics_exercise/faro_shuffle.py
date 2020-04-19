deck = str(input())
turns = int(input())
deck_list = deck.split()
for _ in range(turns):
    length = int(len(deck_list))
    mid_length = int(length / 2)
    shuffled_deck = []
    for i in range(mid_length):
        shuffled_deck.append(deck_list[i])
        shuffled_deck.append(deck_list[mid_length + i])
    deck_list = shuffled_deck
print(deck_list)