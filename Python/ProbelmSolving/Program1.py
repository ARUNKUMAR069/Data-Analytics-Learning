#  Write a program to display your name, age and address in three different lines.
name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
address=str(input("Enter your address: "))

print(f"""
Your name is:{name}
Your age is:{age}
Your address is:{address}
      """)