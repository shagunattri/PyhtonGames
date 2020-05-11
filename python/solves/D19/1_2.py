import datetime

before = datetime.datetime.now()
for i in range(100):
    x += 1

after = datetime.datetime.now()

exec_time = after - before
print(exec_time.microseconds)