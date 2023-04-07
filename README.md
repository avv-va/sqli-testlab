## Notes
Ava: I followed the instructions from this [post](https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/). 

In `project/user/views.py` I added a `_authenticate` function which is called in the `login` function. If you set the `sql_safe` flag to be `false` you can perform a sql injection.

## SQL injection example

In the login form, enter this username: `ava'--` and enter any password. You should be able to log in. If the `ava` username doesn't exist, just register any username and add the `'--` when signing in. 

It's currently not able to perform SQLI by adding `OR '1' = '1` which I haven't checked yet.

## How to run
Clone the github repo and activate the virtualenv:
```
git clone git@github.com:avv-va/sqli-testlab.git
cd sqli-testlab
source venv/bin/activate
```
Install the requirements:
```
pip install -r requirements.txt
```
Make the migrations for database:
```
cd project
python manage.py makemigrations
python manage.py migrate
```
Run the server: (make sure you are in the sqli-testlab/project directory)
```
python manage.py runserver
```
Now you should be able to access the sever at http://127.0.0.1:8000/