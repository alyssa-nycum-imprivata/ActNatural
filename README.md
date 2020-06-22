# Act Natural

## Why was it created?

## What is is?

## Technologies used:

## Installations to test locally:

1. git clone this repo in your terminal and cd into it:
```shell session
$ git clone git@github.com:alyssanycum/ActNatural.git && cd $_
```

2. Create your OSX/Linux OS virtual environment in Terminal:
```shell session
$ python -m venv actnaturalEnv
$ source ./actnaturalEnv/bin/activate
```

OR

Create your Windows virtual environment in Command Line:
```shell session
$ python -m venv actnaturalEnv
$ source ./actnaturalEnv/Scripts/activate
```

3. Install the app's dependencies:
```shell session
$ pip install -r requirements.txt
```

4. Build your database from the existing models:
```shell session
$ python manage.py makemigrations actnatural app
$ python manage.py migrate
```

5. Create a superuser for your local version of the app:
```shell session
$ python manage.py createsuperuser
```

6. Run your server:
```shell session
$ python manage.py runserver
```

7. Open http://localhost:8000 in your browser