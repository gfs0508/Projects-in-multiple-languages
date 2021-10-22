#Calculator 
#version 1.2
#by GFS-0508
#View GFS-0508 on GitHub :https://github.com/GFS-0508

print("||==================================================================================||");
print("||=======================Calculator version 1.2 by GFS-0508=========================||")
print("||==================================================================================||");

num1 = float(input("Enter the first number> "))
num2 = float(input("Enter the second number> "))
num3 = 0
operation = input("Selection a operacion> ")

if(operation == "+"):num3 = num1 + num2;print(num1,"+",num2,"=",num1 + num2) 
if(operation == "-"):num3 = num1 - num2;print(num1,"-",num2,"=",num1 - num2) 
if(operation == "*"):num3 = num1 * num2;print(num1,"*",num2,"=",num1 * num2) 
if(operation == "x"):num3 = num1 * num2;print(num1,"*",num2,"=",num1 * num2) 
if(operation == ":"):num3 = num1 / num2;print(num1,"/",num2,"=",num1 / num2) 
if(operation == "/"):num3 = num1 / num2;print(num1,"/",num2,"=",num1 / num2) 
if(operation == "+","-","*","x",":","/"): print("") 
else: (print("Invalid Operation"))

print("Add a third number?")

operation = input("Selection a new operacion> ")

if(operation == "+"): num4 = float(input("Enter the third number> ")); print(num3,"+",num4,"=",num3 + num4)
if(operation == "-"): num4 = float(input("Enter the third number> ")); print(num3,"-",num4,"=",num3 - num4)
if(operation == "*"): num4 = float(input("Enter the third number> ")); print(num3,"*",num4,"=",num3 * num4)
if(operation == "/"): num4 = float(input("Enter the third number> ")); print(num3,"/",num4,"=",num3 / num4)

if(operation == "+","-","*","x",":","/"): print("") 
else: (print("Invalid Operation"))