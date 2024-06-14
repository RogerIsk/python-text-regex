import re
import os 

clear = lambda: os.system('clear')
clear()

# Task
# Make any face happy. Create a function that takes a sentence containing sad faces and turn them into happy ones! This involves changing only the mouths.  
# Make sure to only change the face if there are eyes before them, round(3.4) wouldn't become round)3.4) (for example).


def make_happy(txt):
    return re.sub(r'(?<=[:;8x])(\()', ')', txt)  
print(make_happy("My current mood: :(")) # -->    "My current mood: :)"
print(make_happy("I was hungry 8(")) # -->    "I was hungry 8)"
print(make_happy("print('x(')")) # -->    "print('x)")


# r'(?<=[:;8x]) - searching for the eye symbols before the mouth
# (\() - searching for the mouth symbol if we find the eye symbol before it
# ')' - if we found 2 of the previous patterns matching we replace the mouth symbol with the happy one



