## Day-02 exam

## Github practice repository by Asabeneh
## Exercise: level 1 variable declaration

first_name = 'Jacob'
last_name = 'Smith'
full_name = 'Jacob Smith'
country = 'Canada'
city = 'Montreal'
age = 62
year = 1962
is_married = True
is_true = True
is_light = True
first_name, last_name, country, city, age = 'Jacob', 'Smith', 'Canada', 'Montreal', 62

## Math (Level 2)
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

## Getting the area and circumference of a circle
radius = 30
pi = 3.14
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius

## Exercise: Level 2 using the already declared variables

## Identifying data types using type() functions
print (type(first_name)) ## str
print (type(last_name)) ## str
print (type(country)) ## str
print (type(city)) ## str
print (type(age)) ## int
print (type(year)) ## int
print (type(is_married)) ## bool
print (type(is_true)) ## bool
print (type(is_light)) ## bool

## Getting the length both first and last name, and compare it using the if else if condition

print ('\nFirst Name Length:',len(first_name)) ## len = 5
print ('Last Name Length:',len(last_name)) ## len = 5

if len (first_name) == len(last_name):
    print ('Both first and last name has a same length\n')

elif len (first_name) > len(last_name):
    print ('First name length is greater than to Last name length\n')

elif len (first_name) < len(last_name):
    print ('First name length is less than to Last name length\n')

## simple math operation
print ('First num:', num_one)
print ('Second num', num_two)
print ('Addition:', total)
print ('Subtraction:', diff)
print ('Multiplication:', product)
print ('Division:', division)
print ('Modulus:', remainder)
print ('Exponent:', exp)
print ('Floor Division:', floor_division)

## equation of the circle getting the area, circumference, and user input of radius

## Getting the area of the circle
print ('\n Area of the circle:', area_of_circle)

## Getting the circumference of the circle
print ('\n Circumference:', circum_of_circle)

radius_2 = float(input('\nInsert your desire radius: '))
area_circle = pi * (radius_2 ** 2)

print ('Area of the circle:', round(area_circle, 2))

## Input of first name, last name, country, and age

first_name = input('What is your First Name: ')
last_name = input('What is your Last Name: ')
country = input('Where are you from: ')
age = input('How old are you: ')

print ('\nFirst Name:', first_name)
print ('Last Name:', last_name)
print ('Country:', country)
print ('Age:', age)




