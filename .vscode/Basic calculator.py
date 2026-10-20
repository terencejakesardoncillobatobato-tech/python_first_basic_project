# This where the operation begin.
operator = input("choose : +-*/ ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

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
# this place where if the answer is invalid.
else:
    print(f"{operator} invalid")
    
















