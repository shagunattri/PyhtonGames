def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("WHy divide by zero!!")
except:
    print('Other Exception')