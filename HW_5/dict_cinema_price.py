cinema = {'Пятница':
{12:250,16:350,20:450},'Чемпионы':{10:250,13:350,16:350},
'Пернатая банда':{10:350,14:450,18:450}}


film = input('Choose the film: ')
date = input('Choose the date (today or tomorrow): ')
time = int(input('Choose the time: '))
tickets = int(input('Enter number of tickets: '))

def number_people(n):
    if n >= 20:
        return 0.8
        print('Дополнительно ваша скидка составит 20% ')
def discount(n):
    if n == "сегодня":
        return 1
    else:
        return 0.95
def cinema_price(film, date, time, tickets):
    return cinema[film][time]*tickets*number_people(tickets)*discount(date)
    

if film and date and time and tickets:
    if film in cinema:
        if date == "сегодня" or date == "завтра":
            if time in cinema[film]:
                print("Фильм:", film, "День:", date, "Время:", time, "Количество билетов:", tickets)
                print("Результат:", cinema_price(film, date, time, tickets))
            
else:
    print('Input Error')
