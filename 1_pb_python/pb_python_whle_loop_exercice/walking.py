steps_input = ()
total_steps = 0
while total_steps < 10000:
    steps_input = input()
    if steps_input == 'Going home' and total_steps < 10000:
        steps_input = int(input())
        total_steps += steps_input
        if total_steps >= 10000:
            print(f'Goal reached! Good job!')
            break
        steps_needed = 10000 - total_steps
        print(f'{steps_needed} more steps to reach goal.')
        break
    total_steps += int(steps_input)
    if total_steps >= 10000:
        print(f'Goal reached! Good job!')
        break