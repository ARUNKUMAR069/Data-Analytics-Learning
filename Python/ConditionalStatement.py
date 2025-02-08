#  If the statement
#  The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block).

# Syntax:

a = 10
b = 15
if a > 9:
    print("a is greater than 10")
else:
    print("a is less than 10")

print("-------------------------------------------------------------")


#  If-elif-else statement

if a > 10 and (not b > 10):
    print("a is greater than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is less than 10")

    # Nested if statement

if a >= 10:
    if b > 10:
        print("a and b are greater than 10")
    else:
        print("a is greater than 10 but b is less than 10")
else:
    print("a is less than 10")

    # Short Hand If Statement
    # If you have only one statement to execute, you can put it on the same line as the if statement.

if a > b: print("a is greater than b")

    # Short Hand If-Else Statement
    # If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

print("a is greater than b") if a > b else print("a is less than b")

