from random import shuffle
from typing import Sequence

# 1. 
# First, I would ask the user for a target number. Then I would have a function search the main array for any combinations of any two numbers that would add up to
# the target number. If it does, it prints out the two numbers.

given_array = [5, 17, 77, 50]
random_array = given_array
def target_check (num):
    for x in given_array:
        for y in random_array:
            print (str(x+y))
            if ((x + y) == int(num)):
                print (str(x) + " and " + str(y) + " get you to the target of " + num)
                return

    
target = input("Input a target: ")
target_check(target)
        


# 2.
# To start this one, I would use the original palindrome problem as a foundation. To make sure it can still tell if a string is a palindrome with spaces,
# I would make a if statement letting all characters be added to the list besides spaces.

problem4_lists = []
problem4_input = input("Enter a word: ")
for character in problem4_input:
    if (character != " "):
        problem4_lists.append(character)
print (problem4_lists)

while (len(problem4_lists) != 1):
    if (problem4_lists[0] == problem4_lists[-1]):
        problem4_lists.pop(-1)
        problem4_lists.pop(0)
        print (problem4_lists)
    else:
        print ("Its not a palindrome")
        break
    
else:
    print ("Its a palindrome!")
    

# 3. 
#First i would re-organize the order of the array so that the integers are in order. Then I would make a count variable equal to the first index of
#the array. Next, I would have a for statement for each item in the array to be compared with the count. If the index item is equal to the count,
#the count goes up one and it is a sequence so far.

ArrayList = [17, 15, 20, 19, 21, 16, 18]
ArrayList.sort()
count = ArrayList[0]
print (ArrayList)
for x in ArrayList:
    if int(count) == ArrayList[(ArrayList.index(x))]:
        Sequence = True
        count += 1
    else:
        Sequence = False
        break

print (Sequence)
        

# 4.
#First I would have a for loop checking each item in the array. If the item is below 0, it is added to a negative list. If the item is above
#0, the item is added to a positive list. Another for loop would be needed to add all of the negative numbers together. You would also need a variable 
#equal to the length of the positive list. Finally, you add the length of the positive list to the first index to the final array and the sum
#of the negative numbers to the second index.

problem4_lists = [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]
positive_lists = []
negatiive_lists = []
final_array = []
negative_sum = 0
for x in problem4_lists:
    if x < 0:
        negatiive_lists.append(x)
    elif x > 0:
        positive_lists.append(x)
for x in negatiive_lists:
    negative_sum = negative_sum + negatiive_lists[(negatiive_lists.index(x))]
positive_count = len(positive_lists)
final_array.append(positive_count)
final_array.append(negative_sum)
print (final_array)


# 5.
# For this problem, all you need to do is use the split method. This allows the numbers with any amount of digits to be easily added to a list.
# then you can use the math methods to easily print the maximum and minimum.

problem5_input = input ("Enter a string of numbers seperated by spaces: ")
number_list = (problem5_input.split())
ordered_list = []
for x in number_list:
    ordered_list.append(int(x))
ordered_list.sort()
print (min(ordered_list), max(ordered_list))




# 6.
#First, I would use a for loop to put all of the characters inputed into a list. Then I would have a bunch of if statements checking if the string
#had required characters for a email like the '@' symbol. If they all are true, it prints true. If any of them are false, it prints false.

problem6_input = input("Enter an email address: ")
problem6_array = []
for character in problem6_input:
    problem6_array.append(character)
if "@" in problem6_array:
    if problem6_array[-4] == ".":
        if problem6_array[-3] == "c":
            if problem6_array[-2] == "o":
                if problem6_array[-1] == "m":
                    print (True)
                else:
                    print (False)
            else:
                print (False)
        else:
            print (False)
    else:
        print (False)
else:
    print (False)


# 7.
#First I would create a list that contains all of the letter of the alphabet in order. Then when the user inputs a string, a for loop checks
#the index in the alphabet and adds that to a final list.

alphabet_list = ["*","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
input_list = []
final_list = []
problem7_input = input ("Enter a string of letters: ")
for character in problem7_input:
    input_list.append(character)
for character in input_list:
    if character == " ":
        input_list.remove(character)
for character in input_list:
    final_list.append(alphabet_list.index(character))
print (final_list)


# 8.
#First, I would ask the user for a combination. Then I would create to counts: one that counts down and one that counts up.
#Two while loops would test each count until they reach the target combination. The program will then print out which option takes less amount
#of moves to the target.

problem8_input = int(input ("Input a 4-digit lock combination: "))
option1 = 0000
option2_count = 0
option2 = 9999
while option1 < problem8_input:
    option1 += 1
while option2 > problem8_input:
    option2 -= 1
    option2_count += 1
print (option2_count)
print (option1)
if option1 < option2_count:
    print (str(option1) + " turns to combo.")
else:
    print (str(option2_count) + " turns to combo.")



# 9.
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

# 10.
#First I would create a prompt that asks the user for a number. The program then joins each digit of the input to a list. This allows the use of
#the reverse method, reversing the order of the digits. Then would require a function to add each digit back into one number. Finally, requires
#the use of the reciprocal method from numpy, printing it as a float.

def convert ():
    s = [str(i) for i in reverse_list]
    switch = int("".join(s))
    return switch

problem10_input = input ("enter a number: ")
reverse_list = []
for character in problem10_input:
    reverse_list.append(character)
reverse_list.reverse()
final_num = convert()
reciprocal_num = float (1 / final_num)
print (reciprocal_num)





