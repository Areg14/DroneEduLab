string1 = "This is a short text"
print(string1)
string2 = input("Enter ward you want to remove: ")

try:
    print(string1)
    print(string1.replace(string2, ""))
except:
    print("Can't strip the word!")