length = int(input("Enter a length: "))
breath = int(input("Enter a breath: "))

area = length * breath
prameter = 2 * (length + breath)

if area > prameter:
    print("area is greater")
elif prameter > area:
    print("paramete is gatrter")
else:
    print("both are equal")