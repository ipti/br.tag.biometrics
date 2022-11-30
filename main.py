from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import messages

import fingerprint
from flask_cors import CORS
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return render_template("index.html")

@socketio.on('IdStore')
def store_finger(IdStore):
    if fingerprint.enroll_finger(int(IdStore), socketio):
        socketio.emit('message', messages.STOREOK)
    else:
        socketio.emit('message', messages.STOREFAIL)

@socketio.on('IdDelete')
def delete_finger(IdDelete):
    if fingerprint.finger.delete_model(int(IdDelete)) == fingerprint.adafruit_fingerprint.OK:
        socketio.emit('message', messages.DELETEOK)
    else:
        socketio.emit('message', messages.DELETEFAIL)

@socketio.on('message')
def handle_message(message):
    if message == 'SearchSendMessage':
        if fingerprint.get_fingerprint(socketio):
            messages.FINGERDETECTED['id_finger'] = fingerprint.finger.finger_id
            messages.FINGERDETECTED['confidence'] = fingerprint.finger.confidence
            socketio.emit('message', messages.FINGERDETECTED)
        else:
            socketio.emit('message', messages.FINGERNODETECTED)
    elif message == 'StoreSendMessage':
        store_finger()
    elif message == 'DeleteSendMessage':
        delete_finger()
    elif message == 'ClearSendMessage':
        if fingerprint.finger.empty_library() == fingerprint.adafruit_fingerprint.OK:
            socketio.emit('message', messages.EMPTYLIBRARY)
        else:
            socketio.emit('message', messages.EMPTYLIBRARYFAIL)

if __name__ == '__main__':
    socketio.run(app)