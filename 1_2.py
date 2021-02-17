cub = []
i = 0
s = 0
for i in range (1, 1000, 2):
    numeral = i ** 3
    cub.append(numeral)
print(cub)

sum = 0
for item in cub:
    res = 0
    number = item
    while item > 0:
        res += item % 10
        item = item // 10
    if res % 7 == 0:
            sum += number
print(sum)

sum = 0
for i in range (len(cub)):
    cub[i] += 17
print(cub)
for item in cub:
    res = 0
    number = item
    while item > 0:
        res += item % 10
        item = item // 10
    if res % 7 == 0:
            sum += number
print(sum)




