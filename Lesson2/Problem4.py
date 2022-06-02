# Creating method that calculates the sum for x and y
def calculate():
    # Checking if the input is integer
    try:
        x = int(input("Enter value for x: "))
        y = int(input("Enter value for y: "))
        sum = x + y
        return sum
    except:
        print("Please enter int value")
        calculate()

print(calculate())