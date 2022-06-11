string1 = input()
string2 = input()
string3 = input()

# Checking if the first string is palindrome
reversed_string1 = string1[::-1]
if reversed_string1 == string1:
    print(f"{string1} is palindrome")
else:
    print(f"{string1} isn't palindrome")
# Checking if the second string is palindrome
reversed_string2 = string2[::-1]
if reversed_string2 == string2:
    print(f"{string2} is palindrome")
else:
    print(f"{string2} isn't palindrome")
# Checking if the third string is palindrome
reversed_string3 = string3[::-1]
if reversed_string3 == string3:
    print(f"{string3} is palindrome")
else:
    print(f"{string3} isn't palindrome")

print("\n")

if string1 in string2:
    print(f"{string1} and {string2} are the same")
if string1 in string3:
    print(f"{string1} and {string3} are the same")
if string2 in string3:
    print(f"{string2} and {string3} are the same")
