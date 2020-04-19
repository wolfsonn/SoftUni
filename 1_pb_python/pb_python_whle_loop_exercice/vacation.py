vacation_budget = float(input())
balance = float(input())
action = str()
action_amount = float()
spend_count = 0
action_count = 0

while spend_count < 5:
    action = str(input())
    action_amount = float(input())
    if action == 'save':
        action_count += 1
        balance += action_amount
        if balance >= vacation_budget:
            print(f'You saved the money for {action_count} days.')
            break
        spend_count = 0
    if action == 'spend':
        action_count += 1
        spend_count += 1
        if spend_count >= 5:
            print(f'You can\'t save the money.')
            print(action_count)
            break
        balance -= action_amount
        if balance < action_amount:
            balance = 0
