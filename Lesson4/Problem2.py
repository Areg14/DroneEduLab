x = int(input("Enter number for x: "))
y = int(input("Enter number for y: "))

if x > y:
    print(str(x) + " > " + str(y))
elif y > x:
    print(str(y) + " > " + str(x))
else:
    print("These numbers are equal")