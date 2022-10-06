## scorg

### Installation

1. First install Docker, python, pipenv
2. DO `pipenv install -r requirements.txt`
3. or Download this docker container from dockerhub.
4. To install any new package to this project
   `pipenv install package`
5. To build a new docker image from the current Dockerfile
   `docker build . `
6. To run the docker container
   `docker-compose up`
7. TO stop the docker container
   `docker-compose down`
7. To build and run the docker container
   `docker-compose up --build`
8. To run the docker container in detach mode
   `docker-compose up -d`
9. To generate requirements.txt file after new package installation 
   `pipenv requirements > requirements.txt
10. To run docker-compose in detached mode
   $`docker-compose exec web python manage.py migrate`
   $`docker-compose exec web python manage.py createsuperuser`
11. 
