weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(weather)
for i in range (0,len(weather)):
    if weather[i][-1].isdigit():
        dig = int(weather[i])
        if dig < 9:
            sym = weather[i][0]
            if sym == '+' or sym == '-':
                sym = f'{sym}0{weather[i][1]}'
                weather[i] = sym
            else:
                number_1 = f'0{weather[i]}'
                weather[i] = number_1
    else:
        weather[i] = weather[i] + ' '

for i in range(len(weather)-1, 0, -1):
    if weather[i][-1].isdigit():
        weather.insert(i, '"')
        weather.insert(i+2, '" ')
print(weather)

weather_str = ''.join(weather)
print(weather_str)

