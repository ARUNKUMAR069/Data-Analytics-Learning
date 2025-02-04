# What is TypeCasting and what are it's sub types

# So to Convert one data type to another one is called as typecasting

# Types of Typecasting

# 1. Implicit Typecasting : Where python itself converts
# 2. Explicit Typecasting : Where User Converts


# Example of Implicit Typecasting
name= "John"
age= 23
print(type(name), type(age))


# Implicit example

a= 10
b= 20.5
c= a+b
print(c)
print(type(c))

# Explicit Typecasting

a1= "10"
b1= 20.5
c1= int(a1)+int(b1)
print(c1)
print(type(c1))