#exception handling

x = 42

y = 0
print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Not allowed to divide by Zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup Codess')