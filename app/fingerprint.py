import time
import serial
from tkinter import messagebox
from app import messages

import adafruit_fingerprint

global finger;

def connect_fingerprint(port):
    try :
        uart = serial.Serial(port, baudrate=57600, timeout=1)
        # uart = serial.Serial("dev/ttyUSB0", baudrate=57600, timeout=1) For Linux/Raspberry PI  
    except:
        messagebox.showinfo('Ocorreu um erro', \
        'Conecte o leitor biométrico')
        exit()

    finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

    

def get_fingerprint(socketio):
    socketio.emit('message', messages.WAITINGIMAGE)
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    socketio.emit('message', messages.MODELING)
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
    socketio.emit('message', messages.SEARCHING)
    if finger.finger_search() != adafruit_fingerprint.OK:
        return False
    return True


def get_fingerprint_detail():
    print("Getting image...")
    i = finger.get_image()
    if i == adafruit_fingerprint.OK:
        print("Image taken")
    else:
        if i == adafruit_fingerprint.NOFINGER:
            print("No finger detected")
        elif i == adafruit_fingerprint.IMAGEFAIL:
            print("Imaging error")
        else:
            print("Other error")
        return False

    print("Templating...")
    i = finger.image_2_tz(1)
    if i == adafruit_fingerprint.OK:
        print("Templated")
    else:
        if i == adafruit_fingerprint.IMAGEMESS:
            print("Image too messy")
        elif i == adafruit_fingerprint.FEATUREFAIL:
            print("Could not identify features")
        elif i == adafruit_fingerprint.INVALIDIMAGE:
            print("Image invalid")
        else:
            print("Other error")
        return False

    print("Searching...", end="")
    i = finger.finger_fast_search()
    if i == adafruit_fingerprint.OK:
        print("Found fingerprint!")
        return True
    else:
        if i == adafruit_fingerprint.NOTFOUND:
            print("No match found")
        else:
            print("Other error")
        return False

def enroll_finger(location, socketio):
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            socketio.emit('message', messages.PUTFINGER)
        else:
            socketio.emit('message', messages.PUTFINGERAGAIN)

        while True:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                socketio.emit('message', messages.PICTURETAKEN)
                break
            if i == adafruit_fingerprint.NOFINGER:
                socketio.emit('message', messages.WAITINGFINGER)
            elif i == adafruit_fingerprint.IMAGEFAIL:
                socketio.emit('message', messages.IMAGEFAIL)
                return False
            else:
                socketio.emit('message', messages.OTHERERROR)
                return False

        socketio.emit('message', messages.MODELING)
        i = finger.image_2_tz(fingerimg)
        if i == adafruit_fingerprint.OK:
            socketio.emit('message', messages.MODELED)
        else:
            if i == adafruit_fingerprint.IMAGEMESS:
                socketio.emit('message', messages.CONFUSINGIMAGE)
            elif i == adafruit_fingerprint.FEATUREFAIL:
                socketio.emit('message', messages.NOTIDENTIFTRESOURCES)
            elif i == adafruit_fingerprint.INVALIDIMAGE:
                socketio.emit('message', messages.INVALIDIMAGE)
            else:
                socketio.emit('message', messages.OTHERERROR)
            return False
        if fingerimg == 1:
            socketio.emit('message', messages.REMOVEFINGER)
            time.sleep(1)
            while i != adafruit_fingerprint.NOFINGER:
                i = finger.get_image()

    socketio.emit('message', messages.MODELING)
    i = finger.create_model()
    if i == adafruit_fingerprint.OK:
        socketio.emit('message', messages.CARRER)
    else:
        if i == adafruit_fingerprint.ENROLLMISMATCH:
            socketio.emit('message', messages.FINGERSNOTMATCH)
        else:
            socketio.emit('message', messages.OTHERERROR)
        return False
    i = finger.store_model(location)
    if i == adafruit_fingerprint.OK:
        socketio.emit('message', messages.STORED)
    else:
        if i == adafruit_fingerprint.BADLOCATION:
            socketio.emit('message', messages.BADSTORAGELOCATION)
        elif i == adafruit_fingerprint.FLASHERR:
            socketio.emit('message', messages.FLASHSTORAGEERROR)
        else:
            socketio.emit('message', messages.OTHERERROR)
        return False

    return True