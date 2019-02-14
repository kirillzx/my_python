#atoms number
#Li=3,Mn=25,Hg=80,Cl=17
element = input('Enter the number of the atom: ')
if element:
    atom = int(element)
    if atom == 3:
        print('Li')
    elif atom == 25:
        print('Mn')
    elif atom == 80:
        print('Hg')
    elif atom == 17:
        print('CL')
    else:
        print('Failed to recognize')
else:
    print('Enter the number')

