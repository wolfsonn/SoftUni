book_name = str(input())
capacity = int(input())
count = 0
book_found = False
while count < capacity:
    library_entry = str(input())
    count += 1
    if library_entry == book_name:
        book_found = True
        break
if not book_found:
    print(f'The book you search is not here!')
    print(f'You checked {count} books.')
else:
    print(f'You checked {count - 1} books and found it.')
