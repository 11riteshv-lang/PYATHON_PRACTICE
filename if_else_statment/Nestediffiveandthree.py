x = int(input('Enter 1st side: '))
if x % 5 == 0:
    if x % 3 == 0:
        print('The number is divisible by both 5 and 3')
    else:
        print('The number is divisible by 5 but not by 3')
else:
    print('The number is not divisible by 5')
    
    