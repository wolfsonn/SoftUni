text = input()
chars = "".join([i for i in text if i != " "])
occurrences = {}
for char in chars:
    if char not in occurrences:
        occurrences[char] = 0
    occurrences[char] += 1
for (char, occurrence) in occurrences.items():
    print(f"{char} -> {occurrences[char]}")
