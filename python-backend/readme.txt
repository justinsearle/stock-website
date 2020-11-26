Links:
https://www.youtube.com/watch?v=QjtW-wnXlUY
https://pypi.org/project/pipenv/

Guide to basic python server with Flask to manage project dependencies from scratch
1. Install Python
2. Use CMD editor:
- check python version > 3.6.x with: python --version
- install pipenv: pip install pipenv
3. Create a folder for the APP with a subfolder for the backend:
- APP
  - python-backend
4. Install env and flask: 
- change directory to your python-backend folder in CMD/CLI
- run: py -m venv env
- run: pip install flask
5. Create a file called "app.py" in the python folder
- Copy this code into it and save:
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return '<h1>Hello</h1>'
6. Activate environment
- ensure directory in CLI is backend folder
- type and run three individual lines one by one: 
env\Scripts\activate
set FLASK_APP="app.py"
flask run
7. Should see in console http://127.0.0.1:5000/, type this in browser to see 'Hello'

Done!
8. Also install: pip install connexion
- Used for API endpoint functionality in python