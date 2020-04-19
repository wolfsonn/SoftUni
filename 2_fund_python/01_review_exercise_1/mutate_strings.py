text1 = input()
text2 = input()
text_len = len(text1)
index = int(-1)
for i in range(text_len):
    index += 1
    if text1[index] != text2[index]:
        text1_new = text1.replace(text1[index], text2[index], )
        if text1 != text1_new:
            text1 = text1_new
            print(text1_new)
            