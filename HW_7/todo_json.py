def writer(filename, numbers):
    '''
    Запись в json файл 
    '''
    import json    
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)

def reader(filename):
    '''
    Чтение содержимого json файла 
    '''
    import json    
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e

list_of_todo = list(reader('list_of_tasks.json'))
list_of_tasks = {}
while True:
    number = int(input(
    'Simple todo:\n\t1. Add the task.\n\t2. show task list.\n\t3. Exit.\nEnter the digit: '))    
    if number == 3:
            break
    elif number == 2:
            count = 0
            for k in list_of_todo:
                count += 1
                print(str(count)+" задача")
                for i in k:
                    print('\t'+i+':', k[i])
                print()
                 
    elif number == 1:
            
            list_of_tasks['Задача'] = input('Add the task: ')
            list_of_tasks['Категория'] = input('Add category to the task: ')
            list_of_tasks['Время'] = input('Add time to the task: ')
            list_of_todo.append(list_of_tasks)
            writer('list_of_tasks.json', list_of_todo)
