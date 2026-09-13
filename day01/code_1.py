# Day_01 basically recalling all data types and some stuff hehehehz

# basic printing
print ("Hello World")

# mathematics symbol

print (1+2)    # Addition
print (10-24)  # Subtraction
print (9*10)   # Multiplication
print (50/8)   # Division
print (9%10)   # Modulus
print (25**30) # Exponents

# Conditions
# the if else condition

a = 20
b = 6
c = 60 

if a < b:
    print (a, "is less than to", b)
else:
    print (a, "is not less than to", b)


# the if-else- if condition

Name = "John"
gpa = 89

if gpa >= 90:
    print("Excellent Work", Name)
elif gpa >= 80:
    print("Nice job", Name)
elif gpa >= 70:
    print("Need improvements but still nice job", Name)
else:
    print("You failed", Name)


# Loops

# for loop

y = 15

for i in range (0, y):
    print (i)

# example

fruits = ["Apple", "Watermelon", "Mango"]

for fruit in fruits:
    fruits.append ("Durian")
    fruits.remove (fruits[2])
    fruits[1] = "Pineapple"
    print (fruit)

# While loop 

b = 0
while (b < 8):
    b = b + 1
    print("Hello Crush")


