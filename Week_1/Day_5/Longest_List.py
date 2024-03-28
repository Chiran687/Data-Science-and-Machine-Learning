# Write a python program that initializes non empty list of words with length = 5. 
#Display longest word with its length.

sample_list= ['mango', 'banana', 'kiwi', 'apple', 'grapes']
pri = max(sample_list, key=len)
print(pri, len(pri))