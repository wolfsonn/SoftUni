daily_cash = float(input())
daily_sales = float(input())
total_expenses = float(input())
gift_price = float(input())
total_savings = (5 * daily_cash) + (5 * daily_sales) - total_expenses
if total_savings >= gift_price:
    print(f'Profit: {total_savings:.2f} BGN, the gift has been purchased.')
else:
    money_needed = gift_price - total_savings
    print(f'Insufficient money: {money_needed:.2f} BGN.')