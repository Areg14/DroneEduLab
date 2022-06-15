numbers = []
sorted_numbers = []

for i in range(8):
    number = int(input())
    numbers.append(number)

print(numbers)

for i in range(8):
    max_number = max(numbers)
    sorted_numbers.append(max_number)
    numbers.remove(max_number)

print(sorted_numbers)