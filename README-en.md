# Django Sample Settings

This repository is about sample configuration of django app.
It is compatible with django 2.0 or above, and python 3.6

## How to use

1. Clone this repository

```
$ git clone https://github.com/gyukebox/django-sample-settings
```

2. Activate virtual environment, and install dependencies

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

If your computer does not have virtualenv installed, please install it via this command line.

```
$ pip3 install virtualenv
```

3. Make a new app, and get Started!

```
$ python manage.py startapp APP_NAME
```

## How to configure

In `settings` directory there exist `base.py`, `dev.py`, `prod.py` files.
`base.py` is base settings file
You can add local development environment configuration in `dev.py`. For instance, `DEBUG` attribute should only be activated(set `True`) in local environment.
You can add remote server environment configuration in `prod.py` file.

## License
MIT