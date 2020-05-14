class Person(object):
    def get_gender(self):
        return "unknown"


class Male(Person):
    def get_gender(self):
        return "Male"

class Female(Person):
    def get_gender(self):
        return "Female"

aMale = Male()                
aFemale = Female()

print(aMale.get_gender())
print(aFemale.get_gender())
