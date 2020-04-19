companions = int(input())
days = int(input())
coins = 0
for i in range(0, days):
    coins += (50 - (2 * companions))
    if days // 10 >= 1:
        

coins_per_3_days = (days // 3) * (-3 * companions)
coins_per_5_days = (days // 5) * (20 * companions)
coins_per_15_days = (days// 15) * (2 * companions)

