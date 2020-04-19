deposit_count = int(input())
count = 0
total_amount = 0
while count < deposit_count:
    deposit_amount = float(input())
    if deposit_amount < 0:
        print(f'Invalid operation!')
        break
    print(f'Increase: {deposit_amount:.2f}')
    total_amount += deposit_amount
    count += 1
print(f'Total: {total_amount:.2f}')
