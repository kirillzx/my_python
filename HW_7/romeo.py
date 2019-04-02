import urllib.request
def histogram(s):
    '''
    Функция для подсчета встречаемости элементов в коллекции.
    s - последовательность
    '''
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
def url_open(url:str) -> list:
    """
    Функция возвращает список строк, прочитанный из файла на удаленном сервере.
    
    """
 
    try:     
        with urllib.request.urlopen(url) as webpage:
            lst = webpage.read().decode('utf-8')
        return lst
    except Exception as e:        
        return e
        
if __name__ == '__main__':
    lst = url_open("http://dfedorov.spb.ru/python3/src/romeo.txt")
    countW = histogram(lst.split())
    for i in countW:
        print(i+': '+str(countW[i]))
