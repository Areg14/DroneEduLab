num = int(input())
reversed_num = 0

while num != 0:
    # Getting the last number of input
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(reversed_num)