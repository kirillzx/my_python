with open('temp.txt','r') as file:
    content = file.read()
a = content.split()
temp = []
for i in a:
    temp.append(float(i))
k = 0
for i in temp:
    if temp.count(i) == 1:
        k += 1
print('Maximum temperature',max(temp),'\nMinimum temperature',min(temp),
      '\nAverage temperature',round(sum(temp)/len(temp),5),'\nNumber of unique',k)
