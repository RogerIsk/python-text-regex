import re # Import the regex module
import os

clear = lambda: os.system('clear')
clear()

# Task 1 ===================================================================================================================
# Create a variable called `text` to store the data: `Berlin is a world city of culture, politics, media and science.` . 
# Then search for the first white space character in the string and print its location using the appropriate label. 
# - Your result should look like this:
# The first white-space character is located at position: 6

print("Task 1")
text = "Berlin is a world city of culture, politics, media and science."
for i in range(len(text)):
    if text[i] == " ":
        print(f"The first white-space character is located at position: {i}")
        break

# or Using regex
result = re.search(r"\s", text) # r is for raw string, \s is for white space
print(f"The first white-space character is located at position: {result.start()}")



# Task 2 ===================================================================================================================
# Create a variable called `text` to store the data: `Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.`. 
# Then search for the word `Frankfurt` in the string . 
# - Your result should look like this:
# None

print("\nTask 2")
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
result = re.search(r'Frankfurt', text) # search for the word `Frankfurt` in the string but its not there so the result is be None
print(result)



# Task 3 ===================================================================================================================
# Create a variable called `text` to store the data: `Berlin is a city of culture.` . Replace the spaces with a hyphen.
# - Your result should look like this:
# Berlin-is-a-city-of-culture.

print("\nTask 3")
text = "Berlin is a city of culture."
result = re.sub(r"\s", "-", text) # sub is short for substitute, first we find the empty spaces and then replace them with a hyphen
print(result)



# Task 4 ===================================================================================================================
# Create a variable called `text` to store the data: `Berlin is a city of culture.` . Search if the phrase `in` appears inside the string. 
# Print the output of the regex function.
# - Your result should look like this:
# <re.Match object; span=(4, 6), match='in'>

print("\nTask 4")
text = "Berlin is a city of culture."
result = re.search(r"in", text) # search for the word `in` in the string
print(result) # i thought the result would be just 'in', but its not - interesting, its actually detailed



# Task 5 ===================================================================================================================
# Use the `text` variable from the previous task. Create a regular expression to look for any word that starts with an upper case "B". 
# Print the position (start- and end-position) of the first match occurrence. 
# - Your result should look like this:
# (0, 6)

print("\nTask 5")
result = re.search(r"\bB\w+", text) # \b is for word boundary, B is for the uppercase B, \w is for any word character, + is for one or more
print(result.span()) # span is for the start and end position of the first match occurrence, 
# we are taking specifically the span and that's why the print is only (0,6)



# Task 6 ===================================================================================================================
# Create a variable called `text` to store the data: `The rain in Spain.`. Count how many times the subphrase `ai` appears in the string. Print the results on the screen.
# - Your result should look like this:
# 2

print("\nTask 6")
text = "The rain in Spain."
result = re.findall(r"ai", text) # find all ('re.findall' obviously) the occurences of the word `ai` in the string
print(len(result)) # print the length of the result specifically, which is the number of occurences of the word `ai`

