# INTEGRATE EVENTBRITE OAUTH LOGIN IN OUR DJANGO PROJECT

[![Build Status](https://travis-ci.org/cristianemoyano/socialoauth_django.svg?branch=master)](https://travis-ci.org/cristianemoyano/socialoauth_django)

## Description

This is a project based on Django, which implements the necessary functionality to integrate social-auth-core using the outh provider of Eventbrite.

## Django version

[Django Project Supported Versions table](https://www.djangoproject.com/download/#supported-versions).

## Documentation

The social-auth documentation is available at http://python-social-auth.readthedocs.org/.
The eventbrite api documentation is available at https://www.eventbrite.com/developer/v3/.
The eventbrite backend documentation is available at http://python-social-auth.readthedocs.io/en/latest/backends/eventbrite.html

## Backend supported

[Backend supported list](http://python-social-auth.readthedocs.io/en/latest/backends/index.html).

## Setup
Clone repository
```shell
$ git clone https://github.com/cristianemoyano/socialoauth_django.git
```
Install dependencies
```shell
$ make install
```
Set enviorement: replace key & secret with your credentials
```shell
$ export SOCIAL_AUTH_EVENTBRITE_KEY=KEY
```
```shell
$ export SOCIAL_AUTH_EVENTBRITE_SECRET=SECRET
```
Run application
```shell
$ make run
```

## Makefile

When you work on projects using different technologies, it can be tricky to remember commands to run tests, build the project, deploy, etc. Providing a Makefile with a generic interface makes it easier to switch between projects.

Run django server
```shell
$ make run
```
Migrate models to database
```shell
$ make migrate
```
Make migrations from django models
```shell
$ make migrations
```
Make superuser for django admin dashboard
```shell
$ make user
```
Access to the django shell
```shell
$ make shell
```
Run test
```shell
$ make test
```
Run coverage
```shell
$ make coverage
```
Install dependencies
```shell
$ make install
```
Update dependencies in requirements
```shell
$ make freeze
```


