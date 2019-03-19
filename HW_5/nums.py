s = '''В разные эпохи и у разных народов число Пи имело разное значение.
 Например, в Древнем Египте оно равнялось 3.1604 у индусов оно приобрело значение 3.162 китайцы пользовались числом, равным 3.1459. 
 Буквенное обозначение число Пи получило только в 1706 году – оно происходит от начальных букв двух греческих слов, означающих окружность и периметр.
  Буквой π число наделил математик Джонс, а прочно вошла в математику она уже в 1737 году.'''
list_of_digits = []
number_of_digits = 0
sum_of_digits = 0
max_of_list = 0
for i in range (len(s)):
    if s[i].isdigit():
        list_of_digits.append(s[i])
        number_of_digits += 1
        sum_of_digits += int(s[i])
max_of_list = max(list_of_digits)
print('All digits: ',list_of_digits,'\nNumber of digits: ',number_of_digits,'\nSum of digits: ',sum_of_digits,'\nMax: ',max_of_list)