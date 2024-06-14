# Create a program that takes a single word string from a user and does the following:
# * Concatenates inator to the end if the word ends with a consonant otherwise, concatenate -inator instead.
# * Adds the word length of the original word to the end, supplied with '000'.

def inator(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[-1] in vowels:
        return word + '-inator 4000'
    else:
        return word + 'inator 6000'
print(inator('Shrink'))
print(inator('Doom'))
print(inator('EvilClone'))