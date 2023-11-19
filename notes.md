## Good site for Markdown sytax
# https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# https://pypi.org/project/Flask/

# https://www.askpython.com/python-modules/python-hashlib-module

# https://requests.readthedocs.io/en/latest/


# https://expressjs.com/en/guide/routing.html

# https://www.fullstackpython.com/flask-code-examples.html    

# https://realpython.com/defining-your-own-python-function/




# Git

# hint:   git config pull.rebase false  # merge (the default strategy)
# hint:   git config pull.rebase true   # rebase
# hint:   git config pull.ff only       # fast-forward only


# flask
# pip install -U Flask
# which updated below
# Successfully installed Flask-3.0.0 Jinja2-3.1.2 MarkupSafe-2.1.3 Werkzeug-3.0.1 blinker-1.7.0 # click-8.1.7 importlib-metadata-6.8.0 itsdangerous-2.1.2 zipp-3.17.0


export FLASK_APP=app.py


openhabian@openhabian:~/REPO/cs_test $ export FLASK_APP=hello
openhabian@openhabian:~/REPO/cs_test $ flask run hello.py
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Got unexpected extra argument (hello.py)
openhabian@openhabian:~/REPO/cs_test $ export FLASK_ENV=development
openhabian@openhabian:~/REPO/cs_test $ flask run
 * Serving Flask app 'hello'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit



openhabian@openhabian:~ $ sudo curl -v http://localhost:5000
*   Trying ::1:5000...
* connect to ::1 port 5000 failed: Connection refused
*   Trying 127.0.0.1:5000...
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.74.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.9.2
< Date: Sun, 19 Nov 2023 03:02:35 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 13
< Connection: close
<
* Closing connection 0


openhabian@openhabian:~/REPO/cs_test $ export FLASK_APP=test
openhabian@openhabian:~/REPO/cs_test $ flask run
 * Serving Flask app 'test'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [18/Nov/2023 22:29:17] "GET / HTTP/1.1" 404 -



