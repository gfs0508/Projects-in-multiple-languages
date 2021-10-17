#Calculator 
#version 1.0
#by GFS-0508
#View GFS-0508 on GitHub :https://github.com/GFS-0508

print("||==================================================================================||");
print("||=======================Calculator version 1.0 by GFS-0508=========================||")
print("||==================================================================================||");

num1 = float(input("Enter the first number> "))
print("The first numer is:",num1)

num2 = float(input("Enter the second number> "))
print("The second numer is:",num2)

operation = input("Selection a operacion> ")

if(operation == "+"):print(num1,"+",num2,"=",num1 + num2)
if(operation == "-"):print(num1,"-",num2,"=",num1 - num2)
if(operation == "*"):print(num1,"*",num2,"=",num1 * num2)
if(operation == "x"):print(num1,"*",num2,"=",num1 * num2)
if(operation == ":"):print(num1,"/",num2,"=",num1 / num2)
if(operation == "/"):print(num1,"/",num2,"=",num1 / num2)
if(operation == "+","-","*","x",":","/"): print("") 
else: (print("Invalid Operation"))