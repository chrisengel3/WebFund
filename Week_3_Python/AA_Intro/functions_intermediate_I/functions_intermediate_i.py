# UPDATING VALUES IN DICTIONARIES AND LISTS ===================================================== 11111111111111111
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students[0])

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z) 



# ITERATE THROUGH A LIST OF DICTIONARIES ============================================================= 2222222222222222222
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first_name = {students[i]['first_name']}, last_name - {students[i]['last_name']}")

iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



# GET VALUES FROM A LIST OF DICTIONARIES ============================================================ 33333333333
def iterate_dictionary2(key_name, students):
    for i in range(len(students)):
        print(students[i][key_name])

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)



# ITERATE THROUGH A DICTIONARY WITH LIST VALUES ============================================================ 444444444444444
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']

}
# printInfo(dojo)

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def print_info(some_dictionary):
    print(len(some_dictionary))
    for i in range(len(some_dictionary)):
        print(some_dictionary[i])

print_info(dojo['locations'])
print_info(dojo['instructors'])
