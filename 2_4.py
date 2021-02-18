users = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in users:
    name = item.split(" ")
    #print(name[-1].capitalize())
    hello = f'Привет,{name[-1].capitalize()}! '
    print(hello)

