# from random import choice

# bird = "pidgeon"

# flower = "Cherry Blossom"

# song = "The Higher the Fewer"

# age = "233 years"

# funfacts = []

# def randomfunfacts():
#     funfacts = [
#         "Washington, DC is the capitol of the United States.", 
#         "Has an area of 68.35 sq miles.", 
#         "Located between the states of Maryland and virginia.", 
#         "Unemployment rate is 5.3% (Feb 2024).", 
#         "The current Mayor is Muriel Bowser.", 
#         "Washington DC is missing 'J' street." 
#     ]

# index = choice("012345")
# print(len(funfacts))

# print(funfacts[int(index)])

# write a program that prompts the user to enter 3 integers separated by ",".
user_input = input("Please enter 3 numbers: ")

# Split the given input into three parts
string_tokens = user_input.split(",")
int_tokens = []
for str in string_tokens:
    int_tokens.append(int(str))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# output the result
print(result)

