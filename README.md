[![CodeClimate](http://img.shields.io/codeclimate/github/akozl/configuration.py.svg?style=flat)](https://codeclimate.com/github/akozl/configuration.py 
"CodeClimate")

# configuration.py: easy and flexible configuration management for python applications

Configuration.py is a library for configuration management in python apps. Its goal is to make configurations management
as human-friendly as possible. It provides a simple `load` function that allows to load configuration for given environment 
from any supported formats.
Configuration.py can be used to organize configs for any python applications. Taste better with [dotenv](https://github.com/theskumar/python-dotenv). 

## Installation

> $ pip install configuration.py

## Usage

By default library trying to find `application` config file in `config` folder relatively to application working directory.
Config could be in any supported formats: `application.yaml, application.json` etc. 
`load` function will return config from environment section set by `ENV` or `ENVIRONMENT` system environment variable.

Create `application.yaml` in `config` folder with the content:

```yaml
production:
  debug: False
development:
  debug: True
```

Set current environment into system variable:

>$ export ENV=development

Usage:

```python
>>> from configuration_py import load
>>> config_dict = load()
>>> print(config_dict)
{'environment': 'development', 'debug': True}
```

You can also be more specific, which config should be loaded and from where:

```python
from configuration_py import load

config_dict = load('database', folder='./config/db')
```

You can set environment directly on load:

```python
from configuration_py import load

config_dict = load(environment='test')
```

Config could be generated using supported template language.  From the box you can use python string templates.
System environment variables will be passed to the template automatically. 

So you can create `application.yaml.tmpl`, which means yaml config will be generated using python string templates, 
and you can use system environment variables inside a config.

>application.yaml.tmpl

```yaml
production:
  log_file: $LOG_FILE 
development:
  log_file: None
```

>$ export LOG_FILE=/var/log/logfile.log

```python
>>> from configuration_py import load
>>> config_dict = load(environment='production')
>>> print(config_dict)
{'environment': 'production', 'log_file': '/var/log/logfile.log'}
>>> config_dict = load(environment='development')
>>> print(config_dict)
{'environment': 'development', 'log_file': 'None'}
```

## Supported formats

* YAML by extensions `.yaml`, `.yml`
* JSON by extensions `.json`
* Python string templates by `.tmpl` and `.strtmpl` 

## Examples

### Django 

#### Database 

`config/application.yaml.tmpl`:

```yaml
production:
  databases:
    default: 
      ENGINE: 'django.db.backends.postgresql'
      NAME: 'mydatabase'
      USER: $DATABASE_USER
      PASSWORD: $DATABASE_PASSWORD
      HOST: '127.0.0.1'
      PORT: $DATABASE_PORT
    
development:
  databases:
    default: 
      ENGINE: 'django.db.backends.postgresql'
      NAME: 'mydatabase'
      USER: 'user'
      PASSWORD: ''
      HOST: '127.0.0.1'
      PORT: '5432'
  
test:
  databases:
    default: 
      ENGINE: 'django.db.backends.sqlite3'
      NAME: ':memory:'
```

In `settings.py`:

```python
from configuration_py import load
...
DATABASES = load()['databases']
```

#### Middleware

Loading config in code:

```python
from configuration_py import load
...
MIDDLEWARE_CLASSES = reduce(lambda x, item: x+item[1], sorted(load()['middleware'].items()), [])
```

This will add extra middleware on development:

```yaml
default: &default
  1:
    - django.middleware.security.SecurityMiddleware
    - django.contrib.sessions.middleware.SessionMiddleware
    - django.middleware.common.CommonMiddleware
    
production:
  middleware:
    <<: *default
    
development:
  middleware:
    <<: *default
    2: 
      - python.path.to.LoginRequiredMiddleware
```

Split middleware list to insert additional middleware:

```yaml
default: &default
  1:
    - django.middleware.security.SecurityMiddleware
    - django.contrib.sessions.middleware.SessionMiddleware
    - django.middleware.common.CommonMiddleware

  3:
    - django.middleware.csrf.CsrfViewMiddleware
    - django.contrib.auth.middleware.AuthenticationMiddleware

    
production:
  middleware:
    <<: *default
    
development:
  middleware: &development
    <<: *default
    2: 
      - python.path.to.LoginRequiredMiddleware

test:
  middleware:
    <<: *development
    4: 
      - python.path.to.LastMiddleware
```

Middleware list will be loaded from configuration and merged in a right order:

```python
>>> reduce(lambda x, item: x+item[1], sorted(load(environment="production")['middleware'].items()), [])
['django.middleware.security.SecurityMiddleware', 
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware']
>>>
>>> reduce(lambda x, item: x+item[1], sorted(load(environment="development")['middleware'].items()), [])
['django.middleware.security.SecurityMiddleware', 
 'django.contrib.sessions.middleware.SessionMiddleware', 
 'django.middleware.common.CommonMiddleware', 
 'python.path.to.LoginRequiredMiddleware', 
 'django.middleware.csrf.CsrfViewMiddleware', 
 'django.contrib.auth.middleware.AuthenticationMiddleware']
>>>
>>> reduce(lambda x, item: x+item[1], sorted(load(environment="test")['middleware'].items()), [])
['django.middleware.security.SecurityMiddleware', 
 'django.contrib.sessions.middleware.SessionMiddleware', 
 'django.middleware.common.CommonMiddleware', 
 'python.path.to.LoginRequiredMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware', 
 'django.contrib.auth.middleware.AuthenticationMiddleware', 
 'python.path.to.LastMiddleware']

```

#### Caches

`config/application.yaml.tmpl`:

```yaml
default:
  cache: &default_cache
    default: 
      BACKEND: django.core.cache.backends.locmem.LocMemCache
      
production:
  cache:
    default: 
      BACKEND: django.core.cache.backends.memcached.MemcachedCache
    
development:
  cache:
    <<: *default_cache
  
test:
  cache:
    <<: *default_cache
```

In `settings.py`:

```python
from configuration_py import load
...
CACHES = load()['cache']
```


### SQLAlchemy 

Configuration loading:

> database.yaml.tmpl

```yaml
production:
  database: 
    url: $DATABASE_URL
    
development:
  database:
    url: 'sqlite:///local.db'
  
test:
  database:
    url: 'sqlite://'
```

```python
>>> from configuration_py import load
>>> from sqlalchemy import create_engine
>>> db_config = load(configuration='database')
>>> engine = create_engine(db_config['database']['url'])
```

```python
>>> from configuration_py import load
>>> from sqlalchemy import engine_from_config
>>> db_config = load(configuration='database')
>>> engine = engine_from_config(**db_config['database'])
```

### PyMongo

> application.yaml.tmpl

```yaml
default: 
  mongo: &default_mongo
    host: 'localhost'
    port: 27017
 
production:
  mongo: 
    <<: *default_mongo
    host: 'aws_mongo_host'
    ssl: yes
    
development:
  mongo:
    <<: *default_mongo
  
test:
  mongo:
    <<: *default_mongo
    port: 27027
```

```python
>>> from pymongo import MongoClient
>>> from configuration_py import load
>>> client = MongoClient(**load()['mongo'])
```


## Contributing

Want to contribute? Great!

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Make the appropriate changes in the files. Don't forget about tests!
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin my-new-feature`
6. Submit a pull request :D

## Testing

Project has two kind of tests: unit tests and acceptance tests. 
To run unit tests project uses [nose](http://nose.readthedocs.io/en/latest/) (with optional [coverage](https://coverage.readthedocs.io/en/coverage-4.3.4/#)) and for acceptance tests - [behave](https://pythonhosted.org/behave/behave.html) and [sure](https://sure.readthedocs.io/en/latest/).
To run tests install all of this tools and use appropriate CLI:

> nosetests --with-coverage --cover-package=configuration_py

> behave ./configuration_py/tests/acceptance/

## License

[MIT](https://github.com/Ferroman/configuration.py/blob/master/LICENSE) © Bogdan Frankovskyi