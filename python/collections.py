names = ['Shagun','Attri']
print(len(names)) # get the number of items
names.insert(0,'ID10t') # insert before index
print(names)
names.sort()
print(names)

presenters = names[0:2] # get the first two items 
# starting index and the number of items to retrieve
print(names)
print(presenters)


scores = []
scores.append(98)
scores.append(20)
print(scores)
print(scores[0])



from array import array
scores = array('d')

# array- simple types such as numbers must all be of the same type
# lists- stores anything and store any type
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])


#dictionaries - key/value pairs and storage order is not guranteed
#lists - zero-based index storage order is gurarenteed 

person = {'first': 'Shagun'}
person['last'] = 'Attri'
print(person)
print(person['first'])
