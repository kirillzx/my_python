
list_of_todo = '''Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.


    '''
list_of_tasks = []
while True:
    print(list_of_todo)
    k = int(input('Enter the number'))

    list_of_intermediate = {}
    if k == 1:
        task = input('Formulate the task: ')
        list_of_intermediate['task'] = task

        category = input('Add a category to the task')
        list_of_intermediate['category'] = category

        time_of_task = input('Add time to the task')
        list_of_intermediate['timeTask'] = time_of_task

        list_of_tasks.append(list_of_intermediate)
    elif k == 2:
        for i in list_of_tasks:
            print('Task: ', i['task'], 'Category: ', i['category'], 'Date: ', i['timeTask'])
    elif k == 3:
        break
    else:
        print('Undefined Symbol')
