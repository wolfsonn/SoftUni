low_score_number = int(input())
current_problem_name = str()
last_problem_name = 'none'
score = int()
total_score = 0
test_number = 0
low_score_count = 0
while low_score_count < low_score_number:
    last_problem_name = current_problem_name
    current_problem_name = str(input())
    if current_problem_name == 'Enough':
        average_score = total_score / test_number
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {test_number}')
        print(f'Last problem: {last_problem_name}')
        break
    test_number += 1
    grade = int(input())
    total_score += grade
    if grade <= 4:
        low_score_count += 1
        if low_score_count == low_score_number:
            print(f'You need a break, {low_score_count} poor grades.')
