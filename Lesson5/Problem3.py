t = input()
if "C" in t:
    # Getting celsius value
    c = int(t.strip("C"))
    f = (c * 1.8) + 32
    # Printing result
    print(f"{f}F")
elif "F" in t:
    # Getting fahrenheit value
    f = int(t.strip("F"))
    c = (f - 32)/1.8
    # Printing result
    print(f"{c}C")