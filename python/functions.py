# import datetime

# first_name = 'Shagun'
# print('Task Completed')
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#     print(x)
# print('task Completed')
# print(datetime.datetime.now())
# print()



# from datetime import datetime


#  function to clean code
# def print_time():
#     print('Task Completed')
#     print(datetime.now())
#     print()
    
# firstName = 'Shagun'
# print_time()

# for x in range[0,10]:
#     print(x)
#     print_time()

from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()
    

first_name = 'Shagun'
print_time('First Name Assigned')

for x in range(0,10):
    print(x)
print_time('Loop Completed')



def get_initial(name):
    initial = name[0:1].upper() 
    return initial

fname = input('Enter your First Name: ')
fname_initial = get_initial(fname)
lname = input('Enter your Last Name: ')
lname_initial = get_initial(lname)

print('Your Initials are; ' + fname_initial + lname_initial)