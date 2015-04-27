'''Questions and stuff'''

def q1():
    print('whats 9 + 10?')
    answer = input('> ')
    if answer == 19:
         print('Right')
         return 2
    elif answer == 21:
         print('You stoopid')
         return 10
    else:
        print('YOU DUM SON')
        return 1

def q2():
    print('Who is Obamas terrorist brother')
    answer = input('> ')
    if answer == ' Osama Bin Laden':
        print('Uhh u musta been smokin dat loud loud')
        return 10
    elif answer == 1:
         print('insert text')
         return 10
    else:
        print('Idk you gunna fail boi')
        return 1

def q3():
    print('Where you get dat loud from boi?')
    answer = input('> ')
    if answer =='idk':
         print('Good u no snich i see ya boi')
         return 10
    elif answer == 1:
         print('insert text')
         return 10
    else:
        print('SNICHHHH')
        return 1

questions = [q1,q2,q3]

