#This docker file was created 11/26/2020 by Justin Searle.
#This container will use Python 3 to run our Flask/Connexion and MongoDB Web API that will be used as the backend interface for the stocks web app project.

#Include main packages
FROM python:3.8

#Set container working directory
WORKDIR /usr/src/app
RUN mkdir -p /user/src/app/python-backend
WORKDIR /usr/src/app/python-backend

#Copy development environment install requirement package files into container environment working directory
# COPY . .
# COPY ./python-backend/requirements.txt .
COPY ./Pipfile.lock .
COPY ./Pipfile .
COPY ./app.py .
COPY ./swagger.yml .

#Install pipenv to the container. This creates python virtual environments inside our docker container
RUN pip install pipenv

#Install requirements found in the pipfile.lock instead of pipfile due to the ignore flag
RUN pipenv install --ignore-pipfile --deploy --dev
# RUN pip install --no-cache-dir -r requirements.txt


#Trying to install swagger-ui which apparently lets us edit API settings via web browser?
#RUN pipenv install 'connexion[swagger-ui]'


#Copy any remaining required files or directories into the VM
# COPY . .

#Expose docker container port that our angular app is running on (default: 5000)
EXPOSE 8000

#Run the python app (start the server)
# RUN pipenv shell
# RUN pipenv run python ./app.py
CMD [ "pipenv", "run", "python", "./app.py" ]



#Other code not needed but might be relevant in future 11/26/2020
# FROM node:current-slim