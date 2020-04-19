baklava_price = float(input())
muffin_price = float(input())
stollen_kg = float(input())
stollen_price = float(baklava_price) * 1.6
candy_kg = float(input())
candy_price = float(muffin_price * 1.8)
cookies_kg = float(input())
cookies_price = 7.5
total_price = (stollen_kg * stollen_price) + (candy_kg * candy_price) + (cookies_kg * cookies_price)
print(f'{total_price:.2f}')