a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("\n")
x = input()

result = 0
if x == "*":
    result = a*b*c*d
    print(result)
elif x == "/":
    result = a/b/c/d
    print(result)
elif x == "+":
    result = a+b+c+d
    print(result)
elif x == "-":
    result = a-b-c-d
    print(result)