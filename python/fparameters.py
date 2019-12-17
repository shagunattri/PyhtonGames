def get_initial(name,force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

fname = input('Enter you first name: ')
fname_initial = get_initial(fname) # no value passed for uppercase as it take the default value 
fname_initial = get_initial(force_uppercase=True,name=fname) # u can specify and change the order of the fname to make changes 
print('Your initial is: ' + fname_initial) 
