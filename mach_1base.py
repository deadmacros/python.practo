import getpass
req =int(getpass.getpass("Enter required number: "))
x=int(input("Enter first number: "))
y=int(input("Enter second number:"))
sum = x + y
need = req-sum
if sum>req:
    print("input is right")
elif sum==req:
    print("perfect")
else:
    print("number must incease by",need)
perfect = need+sum
print ("perfect number is",perfect)
