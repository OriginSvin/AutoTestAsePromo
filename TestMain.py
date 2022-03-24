import json
import pytest
import requests
# Пока не реализовано заполнение тестовых значений из файла, скорее всего физализация в pytest
@pytest.mark.parametrize("username, status_code",[("user1",200),      #Заполнение параметраметров для теста GET
                                                  ("user2hes", 404),
                                                  ("123}{~`", 404)])
def test_get_user_status_code(username, status_code): # Код 200 успешная операция
    try:
        response = requests.get("https://petstore.swagger.io/v2/user/"+username)
    except requests.HTTPError:
        pass
    assert response.status_code == status_code
# @pytest.mark.parametrize("id, username,firstName, lastName, email, password, phone,userStatus, status_code_post",[(123,"testhes1",'aa','bb','en','123','1256',10,200)      #Заполнение параметраметров для теста GET
#                                                   ])
@pytest.mark.parametrize("json_post",[({"id":1337, #Заполнение параметраметров для теста POST
  "username": "hesmaster",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 10})])
def test_post_user_status_code(json_post):
    try:
        response = requests.post("https://petstore.swagger.io/v2/user", json=json_post)
    except requests.HTTPError:
        pass
    assert response.status_code < 400
@pytest.mark.parametrize("json_put, status_code_put,username",[({"id":1337,
  "username": "hesmaster",  #Заполнение параметраметров для теста PUT
  "firstName": "string",
  "lastName": "string12",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 10},200,'hesmaster')])
def test_put_user_status_code(username, status_code_put,json_put):
    try:
        response = requests.put("https://petstore.swagger.io/v2/user/" + username, json=json_put)
    except requests.HTTPError:
        pass
    assert response.status_code == status_code_put
@pytest.mark.parametrize("username, status_code",[("hesmaster",200),      #Заполнение параметраметров для теста DELETE
                                                  ("user2hes", 404),
                                                  ("123}{~`", 404)])
def test_delete_user_status_code(username, status_code):
    try:
        response = requests.delete("https://petstore.swagger.io/v2/user/" + username)
    except requests.HTTPError:
        pass
    assert response.status_code == status_code


@pytest.mark.parametrize("username",[('user21'),('userxcat')])
def test_get_user_format(username):
    try:
        response = requests.get("https://petstore.swagger.io/v2/user/" + username)
        chek_value = False
        j2 = response.text
        if response.status_code == 200:
            if (j2.find("id") and j2.find("username") and j2.find("firstName") and j2.find("lastName")
                    and j2.find("email") and j2.find("password") and j2.find("phone") and j2.find("userStatus")):
                chek_value = True
        if response.status_code >=400:
            if(j2.find("code") and j2.find("type") and j2.find("message")):
                chek_value = True
    except requests.HTTPError:
        pass
    assert chek_value

@pytest.mark.parametrize("json_post",[({"id":1337,
  "username": "hesmaster",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 10})])
def test_post_user_format(json_post):
    try:
        response = requests.post("https://petstore.swagger.io/v2/user", json=json_post)
        chek_value = False
        j2 = response.text
        if response.status_code < 400:
            if(j2.find("code") and j2.find("type") and j2.find("message")):
                chek_value = True
    except requests.HTTPError:
        pass
    assert chek_value

@pytest.mark.parametrize("json_put, status_code_put,username",[({"id":1337,
  "username": "hesmaster",
  "firstName": "string",
  "lastName": "string12",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 10},200,'hesmaster')])
def test_put_user_format(username, status_code_put,json_put):
    try:
        response = requests.put("https://petstore.swagger.io/v2/user/" + username, json=json_put)
        chek_value = False
        j2 = response.text
        if response.status_code < 400:
            if(j2.find("code") and j2.find("type") and j2.find("message")):
                chek_value = True
    except requests.HTTPError:
        pass
    assert chek_value

@pytest.mark.parametrize("username",[('user1'),('userxcat')])
def test_delete_user_format(username):
    try:
        chek_value = False
        response = requests.delete("https://petstore.swagger.io/v2/user/" + username)
        j2 = response.text
        if response.status_code < 400:
            if(j2.find("code") and j2.find("type") and j2.find("message")):
                chek_value = True
    except requests.HTTPError:
        pass
    assert chek_value

