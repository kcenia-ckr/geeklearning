numeber = input('Введите число от 1 до 20 ')
percent = 'процент'
numeber = int(numeber)

if numeber == 1:
    print(numeber, percent,)
elif 2 <= numeber < 5:
    print (numeber, percent + 'а')
elif 5 <= numeber < 21:
    print(numeber, percent + 'ов')

arr = []
item = 1
for i in range (1, 21, 1):
    arr.append(i)

for item in arr:
    if item == 1:
        print(item, percent)
        item += 1
    elif 2 <= item < 5:
        print(item, percent + 'а')
        item += 1
    elif 4 < item < 20:
        item += 1
        print(item, percent + 'ов')
