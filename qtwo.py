# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

def add_two_list (list_1,list_2):
    add = list_1 + list_2
    add.sort ()
    return add
hi = [1,4,6,9]
bye = [3,8,7,2,5]
print (add_two_list ([1,4,6,9],[3,8,25,2,5]))