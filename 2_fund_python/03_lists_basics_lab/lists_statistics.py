lines = int(input())
positives = []
count_positives = 0
negatives = []
sum_negatives = 0
for i in range(lines):
    num = int(input())
    if num >= 0:
        positives.append(num)
        count_positives += 1
    else:
        negatives.append(num)
        sum_negatives += num
print(positives)
print(negatives)
print(f'Count of positives: {count_positives}. Sum of negatives: {sum_negatives}')