from __future__ import unicode_literals
from flask import Flask, request, current_app
import logging
import json

app = Flask(__name__)
app.config.from_object('config')

from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler(app.config['LOGFILE'], maxBytes=100*1024*1024, backupCount=20)
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)


@app.before_request
def log_request():
    time = datetime.datetime.utcnow().strftime("%c")
    json_request = json.dumps(request.__dict__, skipkeys=True, default=str)
    app.logger.info("{0} {1}".format(time, json_request))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return ('', 200)
