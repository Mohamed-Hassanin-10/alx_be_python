num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operations = input("Choose the operation (+, -, *, /):")

add = num1 + num2
sub = num1 - num2
mult = num1 * num2

match operations:
    case '+':
      print("The result is "  + str(add))

    case '-':
      print("The result is " + str(sub))

    case '*':
      print("The result is " + str(mult))

    case '/':
      if num2 ==0:
        print("Cannot divide by zero")
      else:
       print("The resilt is " + str(num1 / num2))

    case _:
      print("Invalid input")
