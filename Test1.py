import requests
import pydantic
from pydantic.dataclasses import dataclass
from pydantic import BaseModel
with(open("Dictionary.txt", encoding = "utf-8")) as f:
    text = f.read()
str_text = text.split('\n')
for i in range(0,len(str_text)):
  param = str_text[i].split(' ')
  print(param)
print(str_text)
class UserText(BaseModel):
  id : int
  username: str
  firstName: str
  lastName : str
  email: str
  password: str
  phone: str
  useStatus: int
r1 = requests.post("https://petstore.swagger.io/v2/user", json={
  "id":1337,
  "username": "hesmaster",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 10
})
r = requests.get("https://petstore.swagger.io/v2/user/hesmaster")
r3 = requests.delete("https://petstore.swagger.io/v2/user/hesmaster")
input_json = """{
  "id":1337,
  "username": "hesmaster",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}"""
#print(r.json())
#print(r1.status_code)
#print(r3.status_code)

#usertest = UserText(**r.json())
#print(usertest)

class TestRequest:
  def test_get_user_200(username: str):  # Код 200 успешная операция
    response = requests.get("https://petstore.swagger.io/v2/user/" + str(username))
    return username
print(TestRequest.test_get_user_200('user1'))

#   response = requests.get("https://petstore.swagger.io/v2/user/", json={"id":id,
  # "username": username,
  # "firstName": firstName,
  # "lastName": lastName,
  # "email": email,
  # "password": password,
  # "phone": phone,
  # "userStatus": userStatus})