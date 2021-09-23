#!/usr/bin/env python3
import cgi, cgitb, os
from secret import username, password

form = cgi.FieldStorage()

inputted_username = form.getvalue('username')
inputted_password = form.getvalue('password')

if(inputted_username == username and inputted_password == password):
    print('Set-Cookie: correct_password=true')
print("Content-type:text/html\r\n\r\n")

print(
    f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>The post-login page, wow!</title>
    </head>
    <body>
    <p>You inputted the Username: {inputted_username}</p>
    <p>You inputted the Password: {inputted_password}</p>
    <p>If your username and password were correct, a cookie will be set and a true bool will show below, yum :p</p>
    <p>... also, a page refresh might be required? :/ </p>
    </body>
    </html>

    
    """
)

for key in os.environ.keys():
    if(key == 'HTTP_COOKIE'):
        print(f"<p>Cookie: {os.environ[key]}</p>")