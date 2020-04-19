integers_list = input().split(', ')


def reverse(a):
    return ''.join(reversed([i for i in str(a)]))


def is_palindrome(integers):
    for i in integers:
        if i == reverse(i):
            print('True')
        else:
            print('False')


is_palindrome(integers_list)