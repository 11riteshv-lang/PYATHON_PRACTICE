sp = int(input(" Enter salaing price: "))
cp = int(input("Enter cost price: "))
if sp>cp:
    print("profit")
elif cp>sp:
    print("Profit")
elif sp>cp :
    print("loss")
elif sp==cp:
    print("no profit equal to no loss")
