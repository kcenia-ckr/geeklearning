product = [10.05, 58.86, 89.64, 15, 28.04, 47, 55.21, 63.4, 72.12, 98]
product_str = ''
cost = []
print(id(cost))
for item in product:
    r = int(item // 1)
    kk = int(item * 100 % 100)
    if kk < 10:
        kk = f'0{kk}'
    product_str = f'{r} руб {kk} коп'
    cost.append(product_str)
cost_str = ', '.join(cost)
print(cost_str)
cost.sort()
print(cost)
print(id(cost)) #id совпали

cost_other = sorted(cost, reverse=True) # цены, отсортированные по взрастанию
print(cost_other) # другой id
print(id(cost_other)) # 5 максимальных цен в порядке возрастания

print(cost[5:])


