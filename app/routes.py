from app import app, fingerprint, socketio, messages
from app.models import SearchedMessage



@socketio.on('IdStore')
def store_finger(IdStore):
    socketio.emit('message', messages.STOREOK)
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
    elif message == 'FakeSearch':
        print("LOG: fake search")                
        socketio.emit('message', SearchedMessage(30, 183).to_json())
    elif message == 'DeleteSendMessage':
        delete_finger()
    elif message == 'ClearSendMessage':
        if fingerprint.finger.empty_library() == fingerprint.adafruit_fingerprint.OK:
            socketio.emit('message', messages.EMPTYLIBRARY)
        else:
            socketio.emit('message', messages.EMPTYLIBRARYFAIL)
