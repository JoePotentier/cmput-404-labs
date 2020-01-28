#!/usr/bin/env python3

import cgi
import cgitb
from templates import login_page, secret_page, after_login_incorrect
import os
from http.cookies import SimpleCookie 
import secret

print('Content-Type: text/html')
#print()

#Q1
#print(os.environ, '\n')

#Q2
#print(os.environ['QUERY_STRING'], '\n')

#Q3
#print(os.environ['HTTP_USER_AGENT'])

#print(login_page())

s = cgi.FieldStorage()
username = s.getfirst('username')
password = s.getfirst('password')
#print(username, password)

form_ok = username == secret.username and password == secret.password
c = SimpleCookie(os.environ['HTTP_COOKIE'])
c_username = None
c_password = None
if c.get("username"):
    c_username = c.get('username').value
if c.get("password"):
    c_password = c.get('password').value

cookie_ok = c_username == secret.username and c_password == secret.password

if cookie_ok:
    username = c_username
    password = c_password

if form_ok:
    print("Set-Cookie: username=", username)
    print("set-Cookie: password=", password)

print()

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
