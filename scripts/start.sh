#!/bin/sh
kill -9 `cat /var/run/mysite.pid`
gunicorn --pid=/var/run/mysite.pid -k gevent -b 0.0.0.0:80 mysite.wsgi