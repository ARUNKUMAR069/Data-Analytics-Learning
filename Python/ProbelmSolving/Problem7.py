#   Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.
number=int(input("Enter a number: "))

if number%2==0:
    print("The number is even")
else:
    print("The number is odd")