result = 0
while True:
    num1 = int(input())
    x = str(input())
    num2 = int(input())
    if x == "*":
        result = num1 * num2
        print(f"{num1} {x} {num2} = {result}")
    elif x == "/":
        result = num1 / num2
        print(f"{num1} {x} {num2} = {result}")
    elif x == "+":
        result = num1 + num2
        print(f"{num1} {x} {num2} = {result}")
    elif x == "-":
        result = num1 - num2
        print(f"{num1} {x} {num2} = {result}")
    if input() == "exit":
        break