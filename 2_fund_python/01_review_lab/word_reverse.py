word = input()
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    print(word[i], end='')
    reversed_word += word[i]
