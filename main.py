import _thread
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import messages

import fingerprint
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')


print("Conectado")
@app.route('/')
def home():
    print("Chamou /")
    return render_template("index.html")

@app.route('/init')
def teste():
    global socketio
    socketio.emit('message', messages.WAITINGFINGER)
    id = _thread.start_new_thread(metodoLer,("message",))


@socketio.on('IdStore')
def store_finger(IdStore):
    print("IDSTORE")
    if fingerprint.enroll_finger(int(IdStore), socketio):
        socketio.emit('message', messages.STOREOK)
    else:
        socketio.emit('message', messages.STOREFAIL)

@socketio.on('IdDelete')
def delete_finger(IdDelete):
    print("IDdeleted")
    if fingerprint.finger.delete_model(int(IdDelete)) == fingerprint.adafruit_fingerprint.OK:
        socketio.emit('message', messages.DELETEOK)
    else:
        socketio.emit('message', messages.DELETEFAIL)

def lerDigital():
    print("Lendo digital")
    if fingerprint.get_fingerprint(socketio):
        messages.FINGERDETECTED['id_finger'] = fingerprint.finger.finger_id
        messages.FINGERDETECTED['confidence'] = fingerprint.finger.confidence
        socketio.emit('message', messages.FINGERDETECTED)
        print("Emitindo Finger detected")
    else:
        socketio.send(messages.FINGERNODETECTED)
        print("Emitindo Finger not detected")
    
def metodoLer(message):
    lerDigital()
    print("Passou")
    fingerprint.unlockScan()


@socketio.on('message')
def handle_message(message):
    print(f"message: {message}")
    if message == 'SearchSendMessage':
        # metodoLer(socketio)
        id = _thread.start_new_thread(metodoLer,("",))
        pass
    elif(message == 'CancelMessage' or _thread._count() != 0):
        fingerprint.lockScan()
    elif message == 'StoreSendMessage':
        store_finger()
    elif message == 'DeleteSendMessage':
        delete_finger()
    elif message == 'ClearSendMessage':
        if fingerprint.finger.empty_library() == fingerprint.adafruit_fingerprint.OK:
            socketio.emit('message', messages.EMPTYLIBRARY)
        else:
            socketio.emit('message', messages.EMPTYLIBRARYFAIL)

    print("Saindo do handle")
    _thread.exit()
    
    

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0')
    #gunicorn -w 1 --threads 100 --bind 0.0.0.0:5000 main:app