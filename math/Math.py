'''
Created on 31 May 2017

@author: Administrator
'''

operations = ("Addition", "Subtraction", "Division", "Multiplication", "TimesTable")
num1, num2, chosenOption = 0, 0, 0
valid = False
repeat = True
running = True

def TimesTable(x, y):
        g=lambda x,y:range(x,y-1,-1)if(x>y)else range(x,y+1) 
        for z in g(x,y): print ("".join("%dx%d=%d \n"%(z,w,(z*w)) for w in range(1,11)))

def calculate(num1, num2, op):
    if operations[op-1] == "Addition":
        print("%d + %d = %d" %(num1, num2, (num1+num2)))
    elif operations[op-1] == "Division":
        print("%d / %d = %d" %(num1, num2, (num1/num2)))
    elif operations[op-1] == "Multiplication":
        print("%d x %d = %d" %(num1, num2, (num1*num2)))
    elif operations[op-1] == "TimesTable":
        TimesTable(num1, num2)

while running:
    repeat = True
    while not valid:
        for idx, x in enumerate(operations):
            print(idx+1, x)
        print(operations.__len__()+1, "Quit")
        
        while not valid:
            option = input("Choose an option: ")
            if option.isdigit():
                option = int(option)
                valid = True
            else:
                print("Invalid option, it must be numeric")
                valid = False
            
        valid = False
        
        if option > 0 and option <= operations.__len__():
            chosenOption = option
            valid = True
        elif option == operations.__len__()+1:
            #quit
            print("Quiting application...")
            repeat = False
            running = False
            valid = True
        else:
            print("Invalid option, please choose again")
            valid = False
            
    while repeat:
        valid = False
        while not valid:
            num1 = input("Please choose the first number: ")
            if num1.isdigit():
                num1 = int(num1)
                valid = True
            else:
                print("Invalid number, it must be numeric")
                valid = False
          
        valid = False
                
        while not valid:
            num2 = input("Please choose the second number: ")
            if num2.isdigit():
                num2 = int(num2)
                valid = True
            else:
                print("Invalid number, it must be numeric")
                valid = False
        
        calculate(num1, num2, chosenOption)
        repeatOp = input("Would you like to start again? (Y for yes)")
        if(repeatOp == "y" or repeatOp == "Y"):
            repeat = True
            valid = False
        else:
            repeat = False
            valid = False
            num1, num2, chosenOption = 0, 0, 0