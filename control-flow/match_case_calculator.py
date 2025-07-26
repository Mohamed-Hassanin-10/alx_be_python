num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

match opr:
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
       print("The resilt is " + str(div))

    case _:
      print("Invalid input")
