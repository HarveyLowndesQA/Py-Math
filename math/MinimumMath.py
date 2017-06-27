import sys
def TimesTable(x, y):
    for n in range(x, (y+1 if x<y else y-1), (1 if x<y else -1)): return "".join(("{}x{}={}\n".format(n,i, i*n)) for i in range(1, y))
calculation = lambda x, y, z: x+y if(z==1) else x-y if(z==2) else x/y if(z==3) else x*y if(z==4) else TimesTable(x, y) if(z==5) else sys.exit(1)
def numbers(option):
    num1, num2 = input("Choose the first number: "), input("Choose the second number: ")
    print(("Result: %d" if(num1.isdigit() and num2.isdigit() and option != 5) else "Result: %s" if(num1.isdigit() and num2.isdigit() and option == 5) else numbers(option)) %(calculation(int(num1), int(num2), option)))
    if(input("Repeat?") == "Y"): numbers(option)
def options():
    for idx, x in enumerate(("Addition", "Subtraction", "Division", "Multiplication", "TimesTable", "Quit")): print(idx+1, x)
    option = int(input("Choose an option: "))
    numbers(option) if(option >= 1 and option <= 5) else calculation(0, 0, 6) if(option==6) else options()
while True: options()