money_goal = float(input())
fantasy_ct = int(input())
horror_ct = int(input())
romantic_ct = int(input())
fantasy_pr = 14.9
horror_pr = 9.8
romantic_pr = 4.3
collected_amount_no_tax = round(0.8 * ((fantasy_ct * fantasy_pr) + (horror_ct * horror_pr) + (romantic_ct * romantic_pr)), 2)
delta = abs((round(float(money_goal) - float(collected_amount_no_tax), 2)))
sellers_money = round(delta * 0.10)
if collected_amount_no_tax >= money_goal:
    collected_money_goal = float(money_goal) + float(delta) - float(sellers_money)
    print(f'{collected_money_goal:.2f} leva donated.')
    print(f'Sellers will receive {sellers_money:.0f} leva.')
else:
    print(f'{delta:.2f} money needed.')