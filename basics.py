def printNum():
    inputNum = int(input("Enter a number: " ))
    print("The number you entered is: ",inputNum)
    print(f"Checking formatted pattern: {inputNum}")

printNum()

def printBool():
    print(bool("False"))

printBool()

def checkAge():
    age = int(input("Enter age: "))
    if age>=18:
        return "ADULT"
    else:
        return "NOT ADULT"
    
checkAge()

def switchCase():
    inputValue = int(input("Enter a number between 1-3: "))
    match inputValue:
        case 1:
            print("You entered One")
        case 2:
            print("You entered Two")
        case 3:
            print("You entered Three")
        case _:
            print("Invalid input")

switchCase()

def whileLoop():
    count = 0
    while count < 5:
        print("Count is:", count)
        count += 1

whileLoop()

# In pass by reference the original variable is changed
# In pass by value the original variable is not changed 
def passByReference(list):   
    return list

my_list = ["Aradhya"]
passByReference(my_list)
print(my_list)
    