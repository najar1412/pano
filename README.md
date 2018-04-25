pano
--

Understanding current limitations of 360 pano software and extending them to support post lens effects, in an attempt to produce maximum realism with little additional work.

#### Current Features

* Background parallax.
* Chromatic aberration
* Lighting manipulation.
* Bloom and glare.

#### Desired Features

* user login
* management of 360s
* produce different versions of the same 360s using different effects.
* publish-able 360s.
* database backed

#### Installation

```
:~/$ git clone https://github.com/najar1412/pano.git

:~/$ cd pano

:~/pano/$ pipenv install
:~/pano/$ pipenv shell

:~/pano/$ cd pano

:~/pano/pano/$ pipenv run python app.py
```

#### Running dev

```
:~/pano/pano/$ gunicorn --bind 0.0.0.0:5000 wsgi:app
```