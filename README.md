This is a sample project that showcase following elements of BE development.

* Using fastAPI to create a backend microservice.
* Using test_main.py to create test script for microservice endpoints.
* Using Dockerfile to containerize the microservice.


Useful commands:
* To create requirements.txt used command
```
pip list --format=freeze > requirements.txt
```

* To create docker image
```
docker build -t <imagename> .
```
for exmaple
``` 
docker build -t rolldice-kube-app .
```

* To run docker image
```commandline
docker run -p 80:80 rolldice-kube-app
```
