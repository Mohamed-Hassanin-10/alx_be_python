size = int (input("Enter the size of the pattern: "))

count = 0

while size <= 0:
    print("Please enter a positive number")
    size = int (input("Enter the size of the pattern: "))

row =0

while row < size:
    for col in range(size):
       print("*", end="")
    print()
    row += 1

