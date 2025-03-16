# Your Student ID:
# Your Name and Surname:

number1 = int(input("Enter a value: "))
number2 = int(input("Enter a value again : "))
operation = input("Which operation do you want? (add, sub, multi, div)")

if operation == "add":
    result = number1 + number2
elif operation == "sub":
    result = number1 - number2
elif operation == "multi":
    result = number1 * number2
else:
    if number2 == 0:
        result = ""
        print("invalid operation")
    else:
        result = number1 / number2

print(result)
