price = input('How much did you pay? ')
price = float(price)

if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Tax Rate is :' + str(tax))
    
    
country = input('Enter the name of your home country: ')
if country.lower() == 'canada':
    print('Oh look a candian')
else:
    print('You are not from Canada')


country = input('What Country do you live in? ')
tax =  0


if country == 'canada':
    province = input('Enter your Province: ')
    if province in('Alberta','Nunavut','Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)    
    