## Notes
Ava: I followed the instructions from this [post](https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/). Currently, the version of the app that is secured against SQLI is coded. I will make it insecure by the end of this week. 

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