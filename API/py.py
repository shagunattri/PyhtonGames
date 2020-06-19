# JSON is a standard data format that can be intimidating at girst glance
# use JSON Linters to make JSON more Readable 
# Json has a key value pair 


import json
print(results['requestId'])

print(results['color']['dominantColorBackground'])

print(results['description']['tags'][0])

for  item in results['description']['tags']:
    print(item)
    

person_dict = {'first': 'Shagun','last':'Attri'}
person_dict['City']='Chennai'

person_json = json.dumps(person_dict)
print(person_json)

# create staff dictionary which assigns a person to a role
staff_dict ={}
staff_dict['Program Manager']=person_dict

#covert dictionary to JSON object
staff_json = json.dumps(staff_dict)
print(staff_json)

languages_list = ['Python','Js','Dart']

person_dict['Languages'] = languages_list

person_json = json.dumps(person_dict)
print(person_json)


# When creating and reading JSON
# Use print statements to help you debug
# usea JSON linting tool to make the JSON easier to read
# have a print out of the full JSON so you can figure out the structure when
# reading specific elements

