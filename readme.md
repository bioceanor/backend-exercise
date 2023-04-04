# requirements
## install poetry
`curl -sSL https://install.python-poetry.org | python3 -`

## install dependencies
`poetry install`

## apply migrations
```shell
cd weatheragg
poetry run python ./manage.py migrate 
```

## running the http server
`poetry run python ./manage.py runserver`



# migrations
In django we use models classes as a database interface, if you change the model you need to update the database using migrations:
```shell
cd weatheragg
poetry run python ./manage.py makemigrations
poetry run python ./manage.py migrate
```



# documentation
useful documentation:
Django: https://docs.djangoproject.com/en/4.2/
Django-ninja: https://django-ninja.rest-framework.com/
