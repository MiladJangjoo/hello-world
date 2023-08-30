# For example, if the function takes the lists [1, 2, 3, 4, 5, 6] and [3, 4, 5, 6, 7, 8, 10], and the maximum inventory size is 8, it should return [10, 8, 7, 6, 6, 5, 5, 4].
# Use the following lists and maximum inventory size:
def add_two_list (list_1,list_2,max_size):
    add = list_1 + list_2
    add = add.reverse ()
    add = add [:int(max_size)+1]
    return add

print(add_two_list ([1, 2, 3, 4, 5, 6],[3, 4, 5, 6, 7, 8, 10],8))