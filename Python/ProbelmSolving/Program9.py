#  WAJP to check whether the entered letter is a vowel or a consonant.
letter= input("Enter a letter: ")
letters=['a','e','i','o','u','A','E','I','O','U']

if letter in letters:
    print("The letter is a vowel")
else:
    print("The letter is a consonant")
    