This PhishDetectApp folder contains the following - 
1) static folder - You can add your background image for the HTML page here.
2) templates - Frontend HTML and CSS script file.
3) Dockerfile - File with the docker commands to integrate front-end and back-end
4) testing.py  - Backend development file using Flask
5) preprocessing.py - Preprocessing function is added to the file.
5) requirements - Necessary libraries to be installed

Model and Vectorizer files need to be added before running this. 

Commands to run on the cmd
docker build -t flask-ml-app .
docker run -p 5000:5000 flask-ml-app