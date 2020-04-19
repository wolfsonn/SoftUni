def number_search():
    number = float(input())
    if 1 <= number <= 100:
        print(f'The number {number} is between 1 and 100')
    else:
        number_search()


number_search()
