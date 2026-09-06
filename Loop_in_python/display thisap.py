# display this ap 100,97,94... upto all terms which are positive

n = int(input("Enter a number: "))
a = 100

for i in range(1, n + 1, 1):
    if a > 0:
        print(a)
        a = a - 3
    else:
        break
     
    
        
        
        
    # elif a <= 0:
    #     print("The number is negative")
