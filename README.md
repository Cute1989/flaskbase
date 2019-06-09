# flaskbase
## intoro
- a flask demo base on cute18/python3-flask-uwsgi
- a falsk base imgae can be use to build other flask project
## Demo run
```
docker pull cute18/flaskbase
docker run -p 80:80 -d cute18/flaskbase
```
## base images
### Structure
#### folder tree
```
|--app
|    -- __init__.py
|    -- ... ...
|--Dockerfile
|--manager.py
```
#### Dockerfile
```
FROM cute18/flaskbase
LABEL maintainer="ljy_coder@163.com"
RUN rm -rf app manager.py 
COPY . .
RUN pip install -r requirements.txt
CMD ["uwsgi", "--ini","uwsgi.ini"]
```
### Docker Command
```
docker build -t PROJECTNAME .
docker run -p 80:80 -d PROJECTNAME
```
