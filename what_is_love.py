secret, love_name, year_of_birth = input('Tell us your secret: '), input('What is love? '), input('When were you born? ')
ciphered_secret = '_'.join([secret, love_name])
ciphered_secret = ciphered_secret[::-1]
ciphered_secret += year_of_birth
print(ciphered_secret)

