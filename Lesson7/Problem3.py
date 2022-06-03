f = int(input())
fibonacci = [1, 1]

def Fibonacci(n):
    for i in range(n):
        if i < 2:
            print(fibonacci[i])
        else:
            F = fibonacci[i - 1] + fibonacci[i - 2]
            fibonacci.append(F)
            print(F)

Fibonacci(f)