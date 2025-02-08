number = input("Enter a number up to 5 digits: ")

if not number.isdigit() or len(number) > 5:
    print("Invalid input. Please enter a number with up to 5 digits.")
else:
    num_digits = len(number)
    if num_digits == 1:
        print("The number is a single digit number")
    elif num_digits == 2:
        print("The number is a two digit number")
    elif num_digits == 3:
        print("The number is a three digit number")
    elif num_digits == 4:
        print("The number is a four digit number")
    else:
        print("The number is a five digit number")