import re

email = "shagunattri17@gmail.com hackernalthehack@google.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern,email)
print(ans)

