print('Think of all the words that start with "a", how many can you think of?')
alist =[]
enter = []
while True:
    enter = input()
    if enter == "!":
        break
    elif enter[0] != 'a':
        print('That letter doesn\'t start with a')
    elif enter in alist:
                print('Already entered.')
    else:
        alist.append(enter)
        print(alist)    
