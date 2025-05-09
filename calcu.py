# calculator

operator = input (" + - / * ")
num1 = float(input(" enter n1"))
num2 = float(input(" enter n2"))        

if operator == "+":
    result = num1 + num2 
    print(result) 

elif operator == "-":
     result = num1 - num2
     print(result) 

elif operator == "*":
     result = num1 * num2
     print(result) 

elif operator == "/":
     result = num1 / num2   
     print(result) 

else:
     print(f"{operator} is not a invalid operator")     

