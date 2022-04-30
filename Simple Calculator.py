print("\n<<< Calculator >>>")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
func = input("a: add, s: subtract, d: divide, m: multiply: ")
if func == "a":
    print(x + y)
elif func == "s":
    print(x - y)
elif func == "d":
    print(x / y)
elif func == "m":
    print(x * y)
else:
    print("enter a valid number")