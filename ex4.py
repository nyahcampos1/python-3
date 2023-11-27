def calculate():
    int1 = ""
    int2 = ""
    while int1 != 'q' or int2 != 'q':
        int1 = int(input("Enter a number: "))
        int2 = int(input("Enter a second number: "))
        sum = int1 + int2
        print(int1, " + ", int2, " = ", sum)
calculate()