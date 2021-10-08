
# 1.
# First, I would declare the string 'hello'. Then, I would create another variable equal to the the value of the first string but with a slice.
# A slice inverses every item inside a variable or list. Finally, I print the new string with the reversed order.


problem1_string = "Hello"
new_problem1_string = problem1_string [::-1]
print(new_problem1_string)

# 2.
# I would first declare "hello world" in a variable. Then I would set the value of the first variable to a new string, but use the .title() function.
# Then I would print the new string.

problem2_string = "hello world"
new_problem2_string = problem2_string.title()
print (new_problem2_string)


# 3.
# What I would do is for every character in the string, I would compare it to the last stored character. If the characters are the same, then it adds one to a counter. 
# If it ends up they are not the same, the count is added to a new string with its character and restarts. Finally the new string is printed.

problem3_string = "aaabbbbbccccaacccbbbaaabbbaaa"
past_char = ""
problem3_lists = []
count = 0
for character in problem3_string:
    if past_char == character:
        count = count + 1
    else:
        count = count + 1
        problem3_lists.append(str(count))
        problem3_lists.append(character)
        count = 0
    past_char = character
problem3_lists.remove("1")

def transform (list):
    new_string = ""
    for x in list:
        new_string += x
    print (new_string)

transform (problem3_lists)


# #4
# What I would do first is let the user enter in a word and then find the length of the input. Next, I would change the string into a list for ease. 
# Then I would compare the first character and the last character using a counter and negative list indexs. If they are the same then they would
# be deleted and continue going over the rest of the letters. If not, then it breaks the command and lets the user know its not a palindrome.

problem4_lists = []
problem4_input = input("Enter a word: ")
num = len(problem4_input)
for character in problem4_input:
    problem4_lists.append(character)
count = 0
negative_count = 1
while (num/2) > count:
    if (len(problem4_lists) != 1):
        if (problem4_lists[count] == problem4_lists[-(negative_count)]):
            problem4_lists.pop(negative_count)
            problem4_lists.pop(count)
            count += 1
            negative_count += 1
        else:
            print ("Its not a palindrome")
            break
    else:
        print ("Its a palindrome!")
        break


