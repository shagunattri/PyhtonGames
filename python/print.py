from datetime import datetime, timedelta
from datetime import datetime
print('Shagun Attri')

name = input('Enter your name:')
print(name)

print()  # print blank line s
print('new line with in the middle of the string')

print('Adding numbers')
x = 42 + 609

# print('Hello \nWorld')


# Strings

first_name = 'Shagun'
last_name = 'Attri'
print(first_name + last_name)
print('Yo' + first_name + ' ' + last_name + 'Wutup pleb!')


sentence = 'shagun is a Pleb He needs to bless up!'
print(sentence.capitalize())
print(sentence.upper())
print(sentence.lower())
print(sentence.count('a'))


fname = input('Enter your first name: ')
lname = input('Enter your last name: ')
print('Hello, ' + fname.capitalize() + ' ' +
      lname.capitalize() + " Let's get started!!")

# Formatting strings
unoname = 'Nintendo'
dosname = 'Switch'

out1 = 'My Fav Console is ' + unoname.capitalize() + ' ' + dosname.capitalize()
print(out1)

out2 = 'My Fav Console is {} {}'.format(
    unoname.capitalize(), dosname.capitalize())
print(out2)

out3 = 'My Fav Console is {1} {0}'.format(
    unoname.capitalize(), dosname.capitalize())
print(out3)

# Only in python 3 and above
out4 = f'My Fav console is {unoname.capitalize()} {dosname.capitalize()}'
print(out4)

# working with numbers

pi = 3.14159
print(pi)

first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num ** second_num)


# type conversion int to str
days_in_feb = 28
print(str(days_in_feb) + ' are the number of days in February!')

# concatenates as nos are converted into strings
fname = '5'
lname = '6'
print(fname + lname)

# input function always returns strings
unono = input('Enter 1st Number: ')
dosno = input('Enter 2nd Number: ')
print(unono + dosno)

# numbers stored as strings must be converted to numeric values before doing math
ano = input('1st Number: ')
bno = input('2nd Number: ')
print(int(ano) + int(bno))
print(float(ano) + float(bno))

# working with dates
current_date = datetime.now()
print('Today is: ' + str(current_date))
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))
print('Hours: ' + str(current_date.hour))


# using datetime and timedelta for knowing day before yesterday and maipulate dates
today = datetime.now()
print('Today is: ' + str(today))


oneday = timedelta(days=2)
daybefore = today - oneday
print('Day before yesterday was: ' + str(daybefore))

# receive the date as a string and convert it to a date time object
birthday = input('When is your birthday? (dd/mm/yyyy):  ')
# format of strip time is important
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))


# using timedelta and datetime to find day before my birthday
bday = input('When is your birthday? (dd/mm/yyyy)')
# strips elements and converts into date time
bday_date = datetime.strptime(bday, '%d/%m/%Y')
print('Birthday: ' + str(bday_date))

unoday = timedelta(weeks=1)
week = bday_date - unoday
print('Week before birthday: ' + str(week))


print('HI')