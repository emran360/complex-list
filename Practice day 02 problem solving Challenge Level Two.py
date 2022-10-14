# Challenge Level Two
# Challenge One

sex = input('Enter your Gender male or female: ')
age = int(input('Enter your Age: '))
# maritial_status = int(input('Enter your Maritial Status: '))

if sex == "female":
    print('You can work in Urban Area')
elif age >= 20 and age < 40 and sex == 'male':
    print('You May work Anywhere')
elif age >=40 and age <=60 and sex == 'male':
    print('You Can work in Urban area')
else:
    print('You are not Fit for work')

# Challenge Two

while True:
    num1 = input('Enter your Number: ')
    print(num1, 'reverse', 'is', num1[::-1])

else:
    print('Please input a number')

# While Loop Problem Solved

user_number = int(input('Enter Your Number: '))
sum = 0
while user_number >= 0:
    sum += user_number
    user_number -= 1
print(sum)

# odd number
maximum = int(input('Enter Your Number: '))
number = 1

while number <= maximum:
    if (number % 2 != 0 ):
        print(number)
    number += 2

# Even number

maximum = int(input('Enter Your Number: '))
number = 2

while number <= maximum:
    if (number % 2 == 0 ):
        print(number)
    number += 2

#Prime Number
number = int(input('Please enter a number: '))
divisible = False
i = 2

while i < number:
    reminder = number % i
    if reminder == 0:
        divisible = True
        print(divisible)
        break
    i += 1
if divisible == True:
    # you can also write: If divisible: both are same
        print (number, 'is not prime number')
else:
    print (number, 'is prime number')


# Prime Number User input And lower number
user_number = int(input('Enter Your Number Here: '))
user_lower_number = 2

print("Prime numbers between", user_lower_number, "and", user_number, "are:")

for num in range(user_lower_number, user_number + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

