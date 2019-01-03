### script to test GatesWithNAND.py

from GatesWithNAND import *

print("Program to add two numbers using logic gates")

print("Enter the input:\nFirst number: 1\nSecond number: 1")

obj = Adder([1,1,0])
print("The sum is: ",obj.Output[1],obj.Output[0])
