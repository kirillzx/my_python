names = ['John','Paul','George','Ringo']
b=[]
a = [names[i] for i in range(len(names)) if names[i] == 'John' or names[i] == 'Paul']
print(a)
