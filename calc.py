#!/bin/python
print("\n\nWLC To Calc\n")
num1=int(input("Enter First Number : "))
num2=int(input("Enter Secoend Number : "))
opdo=input("Please Enter Your Operator ( * + - /)")
if (opdo == "+"):
    result=num1+num2
    print("Ok Result Pulses Is : ",result)
elif (opdo == "-"):
    result=num1-num2
    print("Ok Result Menha Is : ",result)
elif (opdo == "*"):
    result=num1*num2
    print("Ok Result Multplay Is : ",result)
elif (opdo == "/"):
    result=num1/num2
    print("Ok Result Diviaion Is : ",result)
else:
    print("Please Enter A True Value")