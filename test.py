my_dict = {'key1': [1, 2, 3, 4, 5], 'key2': [6, 7, 8, 9, 10]}

for key in my_dict:
    my_dict[key] = my_dict[key][:-3]

print(my_dict)
