print(" Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")
choice = int(input("Enter your choice: "))
if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius * radius
    print("The area of the circle is: ", area)
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print("The area of the rectangle is: ", area)
elif choice == 3:
    side = float(input("Enter the side of the square: "))
    area = side * side
    print("The area of the square is: ", area)
elif choice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is: ", area)
else:
    print("Invalid choice")