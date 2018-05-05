IN DEV

## Installation

## development

```
:~$ git clone https://github.com/najar1412/pano.git
:~$ cd pano

:~/pano$ pipenv install
:~/pano$ pipenv shell
:~/pano$ cd pano

:~/pano/pano$ pipenv run python app.py
```

## production

```
:~$ git clone https://github.com/najar1412/pano.git
:~$ cd pano

:~/pano$ pipenv install
:~/pano$ pipenv shell
:~/pano$ cd pano

:~/pano/pano$ gunicorn --bind 0.0.0.0:5000 wsgi:app
```