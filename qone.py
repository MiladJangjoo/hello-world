# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

def radar (list_1):
    list_2 = []
    for i in list_1:
        if i < 10:
            list_2.append(i)   
            list_2.sort()       
    return list_2
print(radar ([1,11,14,5,8,9,3]))