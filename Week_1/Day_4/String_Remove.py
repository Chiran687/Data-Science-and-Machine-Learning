"""Write a python program to remove the nth index character from a nonempty string. 
Ask user to input non-empty string, and index"""


def remove_char(Test_String, Index):
    result = Test_String[:Index] + Test_String[Index+1:]
    print(result)


Test_String = input("Enter the string: ")
Index = int(input("Please provide the index number to remove: "))

remove_char(Test_String, Index)
