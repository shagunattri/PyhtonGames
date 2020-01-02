import jwt
import requests

token = jwt.encode( {'username':'id10t','iat':'0'},key='id10tisajoke',algorithm='HS256')
token = token.decode("UTF-8")
headers = {'Authorization': f'Bearer {token}'}

print(token)
r = requests.get('http:10.10.10.137:3000', headers=headers)
print(r.text)