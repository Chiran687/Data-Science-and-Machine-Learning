# Write python program to print vowel and consonants on the given string.

<<<<<<< HEAD
def get_vowel(text):
=======
def get_vowels(text):
>>>>>>> 5414fd456c4b59e7566ad32c603f2d0b624963d8
    vowels = "aeiouAEIOU"

    vowel_list = [char for char in text if char in vowels]
    consonant_list = [char for char in text if char not in vowels]

    print("Vowels:", ', '.join(vowel_list))
    print("Consonsnt:", ', '.join(consonant_list))


text = input("Give your string: ")
<<<<<<< HEAD
get_vowel(text)
=======
get_vowels(text)
>>>>>>> 5414fd456c4b59e7566ad32c603f2d0b624963d8
