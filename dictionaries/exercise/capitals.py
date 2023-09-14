country = input().split(', ')
capital = input().split(', ')

res = list(zip(country, capital))

for country, capital in res:
    print(f"{country} -> {capital}")
