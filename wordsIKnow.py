choice = input('Think of all the words that start with a letter, starting with a,b, or c. Choose a letter')
alist =[]
blist =[]
clist =[]
enter =[]

def entry():
    while True:
        enter = input()
        if enter == "!":
            break
        elif enter[0] != choice:
            print('That letter doesn\'t start with ' + choice)
        elif enter in alist or enter in blist or enter in clist:
            print('Already entered.')
        elif choice == 'a':
            alist.append(enter)
            print(alist)    
        elif choice == 'b':
            blist.append(enter)
            print(blist)  
        elif choice == 'c':
            clist.append(enter)
            print(clist)
        else:
            print('I don\'t know what you wrote!')

entry()
