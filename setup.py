# static
    # js
    # css
# templates
    # index.html
# venv
# app.py

import os

os.mkdir("static")
os.mkdir("static/jss")
os.mkdir("static/css")
os.mkdir("templates")

with open("templates/index.html","w"):
    pass
with open("app.py","w"):
    pass

os.system("python -m venv venv")
os.system("venv\\scripts\\pip install flask pymongo")
