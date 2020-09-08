![GitHub license](https://img.shields.io/github/license/jjcapellan/flask-examples-pyjwt.svg)
# FLASK-EXAMPLES-PYJWT 
Simple example of **PyJWT** use in flask.
This example has 4 routes:
* /login : client sends username and password in plain text in JSON format ({username:'name',password:'pass'}) (POST). If login is correct, the client receives the JWT token.
* /unprotected : this route doesn't need credentials.
* /onlyadmins: Only logged user with "admin" rol can acces. Checks the request header named "Authorization" which contains the JWT token obtained after succes login.
* /onlyusers: Only logged user with "user" rol can acces. Checks the request header named "Authorization" which contains the JWT token obtained after succes login.

## How to use
1. Clone or download this repository
2. Install the dependencies:
```
$ pip install -r requirements.txt
```
3. Run the server using run.py file:
```
$ python run.py
```
4. The file **app/db.py** contains users info in a dictionary. It is used like a database.
5. Use some software like postman, insomnia or others REST clients to test the api.