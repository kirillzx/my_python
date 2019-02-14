#Екатеринбург-код 343, 15 руб/мин
#Омск-код 381, 18 руб/мин
#Воронеж-код 473, 13 руб/мин
#Ярославль-код 485, 11 руб/мин

area_code = int(input('Entry the area code: '))
call_duration = int(input('Entry the call duration: '))

if area_code == 343:
    print('the cost of a call:',call_duration*15,' rubles')
elif area_code == 381:
    print('the cost of a call:',call_duration*18,' rubles')
elif area_code == 473:
    print('the cost of a call:',call_duration*13,' rubles')
elif area_code == 485:
    print('the cost of a call:',call_duration*11,' rubles')
else:
    print('no such area code')
