texts = []

for i in range(4):
    text = input()
    texts.append(text)

length = int(input("Enter length you want to check: "))
is_found = False
for i in texts:
    if length > len(i):
        is_found = True
    else:
        is_found = False

if is_found:
    print("Available")
else:
    print("Unavailable")