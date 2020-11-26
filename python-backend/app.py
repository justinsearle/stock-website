#Include Web API imports
from flask import Flask
import connexion

# import importlib
# moduleName = input('api/people')
# importlib.import_module(moduleName)

#Create the application instance
# app = Flask(__name__)
app = connexion.App(__name__, specification_dir='./')

#Read the swagger.yml file to configure the endpoints
# app.add_api('swagger.yml')

#Define routes but ONLY for testing, this API will be defined using connexion/swagger
@app.route('/')
def home():
  return '<h1>Hello</h1>'

#Run the web app on 0.0.0.0 to allow docker to expose it from the container
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    # app.run(debug=True)