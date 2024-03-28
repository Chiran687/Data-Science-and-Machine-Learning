#Write a python program to sum all the items in a list.

new_sample_list = [1, 2, 3, 4, 5]
sum = 0
for i in range(0, len(new_sample_list)):
    sum = sum+ int(new_sample_list[i])
print(sum)