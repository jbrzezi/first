import math

choice1 = input('Choose a path -- left or right: ')

if choice1 == 'left':
    print('you fell in a hole...')
    choice2 = input('What do you want to do -- climb or sit: ')
    if choice2 == 'sit':
        print('you sit until dawn and are rescued...')
        print()
    elif choice2 == 'climb':
        print('you climb out of the hole...')
        print('arriving at your destination late and dirty')
        print()
    else:
        print('your choice is invalid...')
        print('goodbye...')
        print()
elif choice1 == 'right':
    print('you arrive at your destination...')
    print()
else:
    print('your choice is invalid...')
    print('goodbye...')
    print()