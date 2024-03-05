try:
    # code that may raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print(f"Error! Divided by zero is not allowed")
except ValueError:
    print(f"Error! Enter a valid number")
else:
    print(f"The sum of {num1} / {num2} = {result}")
finally:
    print(f"Program end.")