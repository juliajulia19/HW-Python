import random

cocktails = [
    ["мартини","грейпфрутовый сок","жасмин","тоник","лосось"],
    ["клубника","какао","мята","марсала"],
    ["водка","томатный сок","лимонный сок","вустерширский соус","черный перец","сельдерей","лосось"],
    ["джин","вермут","ликер мараскино","апельсины","коктейльная вишня","лосось"],
    ["ром","авокадо","сахарный сироп","сливки","лимонный сок","лед"],
    ["красный вермут","тоник","апельсины","лосось"],
    ["только чай"]
        ]
for i in cocktails:
    if 'лосось' in i:
        i.remove('лосось')

x = random.choice(cocktails)
print('Сегодня в вашем коктейле будет:')
print(*x, sep=', ')