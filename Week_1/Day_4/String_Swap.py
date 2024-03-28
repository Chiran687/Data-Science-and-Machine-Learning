"""Write a python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string."""

first_string = "first"
second_string = "second"

temp_string1 = first_string[:2]
temp_string2 = second_string[:2]

output=print(first_string.replace(temp_string1, temp_string2) + " " + second_string.replace(temp_string2, temp_string1))
