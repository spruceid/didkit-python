# Django Example

This project demonstrates use of verifiable credentials and presentation  for an
application.

## Dependencies

- Poetry ([installation instructions](https://python-poetry.org/docs/#installation))
- Python 3.8 or higher

### Python dependencies

```bash
$ poetry install
```

## Running

For the first time running you will need to run the migrations,
this can be accomplished by running the following command:

```bash
$ poetry run python manage.py migrate
```

To start the server just run:

```bash
$ poetry run python manage.py runserver
```
