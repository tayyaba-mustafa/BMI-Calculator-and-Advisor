def addition(num1,num2):
    ans= num1+num2
    return ans
def subtraction(num1,num2):
    ans= num1-num2
    return ans
def multiplication(num1,num2):
    ans= num1*num2
    return ans
def division(num1,num2,type):
    try:
        if type.upper()== "FLOAT":
            ans= num1/num2
        elif type.upper()== "INTEGER":
            ans= num1//num2
        return ans
    except ZeroDivisionError:
        print("Divison by zero is not allowed")

print("Simple Calculator!")
first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
operation=input("Enter the operation(addition,subtraction,multiplication,division):")
if operation.upper()== "ADDITION":
    result= addition(first_number,second_number)
elif operation.upper()== "SUBTRACTION":
    result= subtraction(first_number,second_number)
elif operation.upper()== "MULTIPLICATION":
    result= multiplication(first_number,second_number)
elif operation.upper()== "DIVISION":
    division_type= input("Enter the division type(integer,float): ")
    result= division(first_number,second_number,division_type)
else :
    result="Invalid operation"

print(f"The output of {operation} on {first_number} and {second_number} is {result}.")