"""Фильм «Пятница»,
сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб.
Фильм «Чемпионы»,
сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб.
Фильм «Пернатая банда»,
сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб. """

film = input('Choose the film: ')
date = input('Choose the date (today or tomorrow): ')
time = int(input('Choose the time: '))
tickets = int(input('Enter number of tickets: '))
def number_people(n):
    global m
    m = 0
    if n >= 20:
        m = 0.2
        print('Дополнительно ваша скидка составит 20% ')
def discount(n):
    global l
    l = 0
    if n == 'завтра':
        l = 0.05
        print('Ваша скидка составит 5% ')
    elif n == 'сегодня':
        print('К сожалению у вас нет скидки ')
    else:
        print('Вы ввели не правильную дату')
def film_friday(n):
    global k
    if n == 12:
        k = 250
    elif n == 16:
        k = 350
    elif n == 20:
        k = 450
def film_champion(n):
    global k
    if n == 10:
        k = 250
    elif n == 13:
        k = 350
    elif n == 16:
        k = 350
def film_gang(n):
    global k
    if n == 10:
        k = 350
    elif n == 14:
        k = 450
    elif n == 18:
        k = 450
def cinema_price(n):
    global price
    if n == 'Пятница':
        film_friday(time)
        discount(date)
        number_people(tickets)
        price = tickets * (k-(k * l)-(k * m))
        print('Итого к оплате: ', price)

    elif n == 'Чемпионы':
        film_champion(time)
        discount(date)
        number_people(tickets)
        price = tickets * (k-(k * l)-(k * m))
        print('Итого к оплате: ', price)

    elif n == 'Пернатая банда':
        film_gang(time)
        discount(date)
        number_people(tickets)
        price = tickets * (k-(k * l)-(k * m))
        print('Итого к оплате: ', price)
    else:
        print('Такого фильма нет')
cinema_price(film)
