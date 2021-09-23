#!/usr/bin/env python3
import os, json

print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI Lab3</title>")
print("<p>Hello World - This is Lab 3!</p>")

#print(os.environ.keys)
json_environ = json.dumps(dict(os.environ), indent = 4)
print(json_environ)

for key in os.environ.keys():
    if(key == 'QUERY_STRING'):
        print(f"<p>Query Parameters: {os.environ[key]}</p>")

for key in os.environ.keys():
    if(key == 'HTTP_USER_AGENT'):
        print(f"<p>Browser Info: {os.environ[key]}</p>")

def _wrapper(page):
    """
    Wraps some text in common HTML.
    """
    return ("""
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                max-width: 24em;
                margin: auto;
                color: #333;
                background-color: #fdfdfd
            }

            .spoilers {
                color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
            }
            .spoilers:hover {
                transition: color 250ms;
                color: rgba(36, 36, 36, 1)
            }

            label {
                display: flex;
                flex-direction: row;
            }

            label > span {
                flex: 0;
            }

            label> input {
                flex: 1;
            }

            button {
                font-size: larger;
                float: right;
                margin-top: 6px;
            }
        </style>
    </head>
    <body>
    """ + page + """
    </body>
    </html>
    """)

def login_page():
    """
    Returns the HTML for the login page.
    """

    return _wrapper(r"""
    <h1> Welcome! </h1>

    <form method="POST" action="login.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)

print("Content-type:text/html\r\n\r\n")
print(_wrapper('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))
print(login_page())
print('If you logged in correctly, a cookie should have been set.\n Refresh the page and check below:')
for key in os.environ.keys():
    if(key == 'HTTP_COOKIE'):
        print(f"<p>Cookie: {os.environ[key]}</p>")