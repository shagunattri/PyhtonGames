email = 'shagunattri17@gmail.com'

email = email.split('@')
print(email[0])



#2


import re 

email = "shagunatri17@gmail.com"

pattern = "(\w+)@\w+.com"

ans =re.findall(pattern,email)

print(ans)

