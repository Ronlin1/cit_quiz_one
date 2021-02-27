"""
WEEK ONE QUIZ AS AT 26TH FEB 2020 ___PYTHON-BLOCKCHAIN-AWS-CIT-CLASS 2021___
"""
# WELCOME SCREEN
print('------------------------- WEEK ONE QUIZ --------------------------')

# TODO: QUIZ ANSWERS
# Global variable --->End of question separator in the ---- terminal ----
end_of_answer = '------------------------------------------------------------------'

# 1--> Writing a variable called 'name' and setting it to print out
name = 'Ronnie Atuhaire'
print(f'\nMy name is {name}')
print(end_of_answer)

# 2--> Writing a for loop that prints out numbers -1 to -10
negative_numbers_1 = []  # Initialise an empty container first
for i in range(1, 11):
    # Appending -i into numbers
    negative_numbers_1.append(i*-1)
print(f'Negative Numbers(1): {negative_numbers_1}')
print(end_of_answer)

# 3-->Writing a while loop that prints out -1 to -10
negative_numbers_2 = []  # We need Empty container
count = 1
while count <= 10:
    # appending to our container
    negative_numbers_2.append(-count)
    # Incrementing the count +
    count += 1
print(f'Negative Numbers(2): {negative_numbers_2}')
print(end_of_answer)


# 4 --> Hello Function that outputs 'Hello World' to the screen
# Function definition
def hello():
    greeting = 'Hello World'
    return greeting


# Function call
print(hello())
print(end_of_answer)


# 5--> Writing a sum function that takes two parameters
def Sum(x, y):
    # Z getting the total
    z = x + y
    return z


# Example by calling the function --> Just for testing
my_sum = Sum(x=10, y=32)
print(f'Universal answer to everything is {my_sum}')  # Ans should be 42 if called --> Just for Debugging
print(end_of_answer * 3)

# 6--> Printing out all odd numbers using the modulo operator
# modulo returns the remainder in any quotient
odd_numbers = []
for i in range(100):
    # if i's remainder is not zero
    if i % 2 != 0:
        odd_numbers.append(i)
print(f'Odds: {odd_numbers}')
print(end_of_answer * 3)

# 7--> An algorithm to detect if a number is prime?
""" 
    Prime Numbers are natural numbers greater than 1 and they are not a product of 
    two smaller natural numbers. They can only be divisible by one or themselves, 
    no other factors eg 2,3,5,7,11,13..
    
    Small numbers can be 2 0r 3 or also 5 which determine most types of numbers and 
    this will be my basis for the algorithm. We know 2 is the only even number
    among prime numbers.   5 is the only number in the multiples of 5.
    
    Any big number can be broken down by smaller numbers 2 and 3, & if not, then it is prime.
    Eg 100 = 2*50, 90 = 3*30, 843 = 3*281 and so on____
    Also Prime Numbers --> 1*2, 1*3, 1*5, 1*7 so one is a constant
"""


# Defining the algorithm
def isPrime(n):
    # Excluding one and all other numbers less than one as we defined above
    if n <= 1:
        return False
    # Excluding the first four prime numbers I know naturally
    elif n == 2 or n == 3 or n == 5 or n == 7:
        return True
    # Excluding all numbers that are divisible by 2 or 3 -->Small Numbers, add 5:
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    return True


# Just for debugging
first_100_primes = []
for k in range(100):
    prime = isPrime(k)
    if prime:
        first_100_primes.append(k)
print(f'Primes under 100 -----> {first_100_primes}')
print(end_of_answer * 2)

print(f'{end_of_answer} END OF QUIZ {end_of_answer}')
