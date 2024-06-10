# LESSON 1 ASSIGNMENT: PYTHON SYNTAX

# Objective 1: The aim of this assignment is to understand the importance of indentation in Python, especially with if statements.

# Task 1: Code Correction Below is a piece of Python code with incorrect indentation. Your task is to correct it.

# weather = "sunny"

# if weather == "sunny":
# print("Wear sunglasses!")
# else:
# print("Take an umbrella!")

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!") # If you didnt indent here then the it would print "Wear sunglasses!" regardless of if its true or not. (Also gives indentation error)
else: # You dont indent here. This is the alternative function if the first one is false it will now breakout and move to what it should do next which is print "Take an umbrella!"
    print("Take an umbrella!")


# Task 2: Your Mood Today  Create another if statement evaluating the users mood. 
# Ask the user how they feel today using input(). If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". 
# Ensure your if statement is properly indented.

user_mood = input("")

if user_mood != "happy" and user_mood != "sad": # added in a statement to help them input the correct word we are looking for. (Alot of people did this in the flowchart exercise so i wanted to incorporate it here.)
    print("Please enter either happy or sad. ")
elif user_mood == "happy":
    print("That's great to hear!")
elif user_mood == "sad":
    print("I hope your day gets better!")


# Objective 2: The aim of this assignment is to practice identifying and using Python's basic data types, as well as the type() function for checking a variable's data type.

#Task 1: Code Correction Given below are some variable assignments. 
# Your task is to identify the data type of each variable using type() and then use the print() function to print it out:

variable_a = "Hello, World!"
variable_b = 23
variable_c = 3.14
variable_d = True

variable_a_type = type(variable_a)
print(variable_a_type) #This will tell us that variable_a is a string. 

variable_b_type = type(variable_b)
print(variable_b_type) #This will tell us that variable_b is a integer. 

variable_c_type = type(variable_c)
print(variable_c_type) #This will tell us that variable_c is a float. 

variable_d_type = type(variable_d)
print(variable_d_type) #This will tell us that variable_d is a boolean. 

#Objective 3: The aim of this assignment is to get familiarized with basic arithmetic operations and understand how they can be applied in everyday situations.

bread = 2.75
peanut_butter= 4.50
jelly = 3.23

grocery_list_cost = bread + peanut_butter + jelly # Add together each variable and then print out the sum.

print(grocery_list_cost)
