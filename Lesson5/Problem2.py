math = int(input("Enter math rate: "))
physics = int(input("Enter physics rate: "))
geography = int(input("Enter geography rate: "))
history = int(input("Enter history rate: "))
geometry = int(input("Enter geometry rate: "))

result = math + physics + geography + history + geometry

if result <= 40:
    print("Fail")
elif result >= 41 or result <= 60:
    print("Satisfactory")
elif result >= 61 or result <= 80:
    print("Good")
elif result >= 81 or result <= 100:
    print("Outstanding")
else:
    print("Something went wrong with this input")
