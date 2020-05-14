import string
str = input()

for letter in string.ascii_lowercase:
    cnt = str.count(letter)
    if cnt > 0:
        print("{},{}".format(letter,cnt))
        