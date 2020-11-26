#This docker file was created 11/26/2020 by Justin Searle.
#This container will use NodeJS to run our AngularJS app that will be used as the front end interface for the stocks web app project.

#Include main packages
FROM node

#Set container working directory
WORKDIR /usr/src/app

#Copy development environment install requirement package files into container environment working directory
COPY package.json .
COPY package-lock.json .

#Install requirement package files inside of container
RUN npm install

#Installing angular/cli manually because ng command is not found when installing only using package.json
RUN npm install -g @angular/cli

#Copy any remaining required files or directories into the VM
COPY . .
# COPY ./src/ ./src/
# COPY ./e2e/ .
# COPY ./browserslist .
# COPY ./karma.conf.js .
# COPY ./angular.json .
# COPY ./tsconfig.json .
# COPY ./tsconfig.app.json .
# COPY ./tsconfig.spec.json .
# COPY ./tslint.json .

#Expose docker container port that our angular app is running on (default: 4200)
EXPOSE 4200

#Serve the front end client (start the web process)
# CMD [ "npm", "start"]
# CMD [ "npm", "run", "build" ]
CMD ["ng", "serve", "--host", "0.0.0.0" ]



#Other code not needed but might be relevant in future 11/26/2020
# ENV PATH /app/node_modules/.bin:$PATH
# RUN ls
# HOST:CONTAINER
