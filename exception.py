import sys
try:# this is used to try to get the input right form the user
    x =int(input("whats x: "))
    y =int(input("whats y: "))
except ValueError:#  incase of user types worng input
    print("use number instead of text")
    SystemExit(1)
try:
    result = x / y
except ZeroDivisionError:# incase of user tries to divide with zero
    print("cannot divide by zero (0)")
    SystemExit(1)# this exits the program in a proper manner after errors

print(f"{x} /  {y}  = {result}")