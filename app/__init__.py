import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from app import messages
from app import fingerprint

import eventlet
eventlet.monkey_patch()


app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*")

if(os.name == 'nt'):
    fingerprint.connect_fingerprint("COM3");
else:
    print("initializing...")
    # fingerprint.connect_fingerprint("dev/ttyUSB0");

@app.route('/')
def home():
    return render_template("index.html")

socketio.run(app, debug=True)