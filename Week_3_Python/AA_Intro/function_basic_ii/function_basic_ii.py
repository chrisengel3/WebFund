# COUNTDOWN
def countdown(n):
    for x in range(n, -1, -1):
        print (x)
# print(countdown(10))


# PRINT AND RETURN
def print_and_return(x,y):
    list = [x,y]
    print(list[0])
    return list[1]
print_and_return(1,2)


#FIRST PLUS LENGTH
def first_plus_length(n):
    return n[0] + len(n)

my_list = [1,2,3,4,5]
print(first_plus_length(my_list))


#VALUES GREATER THAN SECOND
def values_greater_than_second(n):
    new_list = []
    if len(n) < 2:
        return False
    for i in range(len(n)):
        if n[i] > n[1]:
            new_list.append(n[i])
    print(len(new_list))
    return new_list
    

# values_greater_than_second([5,2,3,2,1,4])
print(values_greater_than_second([5,2,3,2,1,4]))



# THIS LENGTH, THAT VALUE
def this_length_that_value(x,y):
    new_list = []
    for i in range(x):
        new_list.append(y)
    print(new_list)    
    return new_list

this_length_that_value(4,7)