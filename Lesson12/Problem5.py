numbers = []

while True:
    input_ = input()
    if input_ == "exit":
        break
    number = int(input_)
    if number not in numbers:
        numbers.append(number)

print(numbers)