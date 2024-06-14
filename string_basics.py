# Create a variable called ```text``` to store the data: Berlin is a world city of culture, politics, media and science.
# Your task is to print the length of the ```text``` variable on the screen. 

print('Task 1')
text = "Berlin is a world city of culture, politics, media and science."
for i in range(len(text)):
    print(i)



# Reuse the variable called ```text```  and print the first and the last characters on the screen.

print('\nTask 2')
print(text[0],text[-1])

# Reuse the variable called ```text```  and print the first three characters in upper case.

print('\nTask 3')
print(text[0:3].upper())



# Create the variable called ```text``` with the following content:  
# ```Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital ```, 
# then count how many times the letter  ```B ``` appears in the text.

print('\nTask 4')
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
print('B appears: ', text.count('B'), 'times')


# Create a variable called ```text``` to store the data: ```Berlin straddles the banks of the Spree, 
# which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau.``` . 
# Your task is to print the last 10 characters of the ```text``` variable on screen.

print('\nTask 5')
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
print('Last ten character are: ', text[-10:])


# Create a variable called ```text``` to store the data: ```---Python programming---``` . 
# Your task is to remove the hyphen (```-```) character from the string.

print('\nTask 6')
text = "---Python programming---"
print(text.replace('-', ''))

# Create two variables to store your first and your last name. Your task is to concatenate the two variables using the appropriate labels.
# * You should provide a single line print statement.

print('\nTask 7')
first_name = 'Roger'
last_name = 'Iskrenov'
print('First name: ', first_name, '\nLast name: ', last_name)

