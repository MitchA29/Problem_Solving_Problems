
# 1.
# I would create a user input and make a function to see if it is a happy or sad number. This function would continously break down the number by 
# its squares until it reaches 1. If it doesn't it is a sad number.


def square_it (n):
    squareSum = 0
    while (n):
        squareSum += (n % 10) * (n % 10)
        n = int(n/10)
    return squareSum

def is_happy (n):
    slow = n
    fast = n
    while(True):
        slow = square_it(slow)
        fast = square_it(square_it(fast))
        if (slow != fast):
            continue
        else:
            break

    return (slow == 1)

num = 19
if (is_happy(num)):
    print(str(num) + " is a happy number!")
else:
    print (str(num) + " is a sad number :(")


# 2.
# First, I would make a for loop that iterates every number between 1 - 100. Then I would create a function that checks if it is prime.is_happy
# If it is prime then it prints out the number. If not, it skips that number.

def prime_check (num):
    fill = 0
    for i in range(2, int(num/2)+1):
        if (num % i == 0):
            break
    else:
        print (num)

count = 1
while count < 101:
    prime_check (count)
    count += 1



# 3.
# I would first let the user type in a number. It would then validate if it is an acceptable number or not. If it is acceptable it would continue
# with the function and print the number using the fibonacci formula up to 1000.

def fibonacci (num):
    if num >= 1:
        return (fibonacci(num - 1) + fibonacci(num - 2)) 
    else:
        return num


starting_input = 0
if starting_input <= 0:
    starting_input = int(input("enter a positive integer: "))
    for i in range(starting_input):
        print (-(fibonacci(i)))









    








    
    
    
    
    



