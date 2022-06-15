from itertools import zip_longest
numbers = []
actions = []
result_list = []
result = ""
print("Enter numbers")
def add_action():
    for i in range(len(numbers) - 1):
        action = input()
        actions.append(action)
while True:
    input_ = input()
    if input_ == "next":
        print(numbers)
        print("Enter actions")
        add_action()
        break
    else:
        numbers.append(int(input_))

z = 1
for n, a in list(zip_longest(numbers, actions, fillvalue="")):
    result_list.append(n)
    if z == len(numbers):
        break
    result_list.append(a)
    z += 1

for i in result_list:
    result = str(result) + str(i) + " "

print(f"{numbers}, {actions} = {result}")