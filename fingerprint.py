import time
import serial
from tkinter import messagebox
import messages

import adafruit_fingerprint

try :
    uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)   
except:
    messagebox.showinfo('Ocorreu um erro', \
      'Conecte o leitor biométrico')
    exit()

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)
block = False

def lockScan():
    print("lock Scan")
    global block 
    block = True

def unlockScan():
    print("Unlock Scan")
    global block 
    block = False

def get_fingerprint(socketio):
    i = finger.get_image()
    while i != adafruit_fingerprint.OK and block == False:
        i = finger.get_image()
        pass
    if i != adafruit_fingerprint.OK:
        if i == adafruit_fingerprint.NOFINGER:
            print("No finger detected")
        elif i == adafruit_fingerprint.IMAGEFAIL:
            print("Imaging error")
        else:
            print("Other error")
        return False
    print("Image taken")
    socketio.emit('message', messages.MODELING) 

    i = finger.image_2_tz(1)
    if i != adafruit_fingerprint.OK:
        if i == adafruit_fingerprint.IMAGEMESS:
            print("Image too messy")
        elif i == adafruit_fingerprint.FEATUREFAIL:
            print("Could not identify features")
        elif i == adafruit_fingerprint.INVALIDIMAGE:
            print("Image invalid")
        else:
            print("Other error")
        return False
    
    print("Templated")
    socketio.emit('message', messages.SEARCHING)

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
    print(f"Location: ${location}")
    unlockScan()
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Colocar o dedo")
            socketio.emit('message', messages.PUTFINGER)
        else:
            print("Colocar o dedo novamente")
            socketio.emit('message', messages.PUTFINGERAGAIN)

        entrou = False
        i = finger.get_image()
        while i != adafruit_fingerprint.OK and block == False:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK and entrou == False:
                print("PICTURETAKEN")
                socketio.emit('message', messages.PICTURETAKEN)
            elif i == adafruit_fingerprint.NOFINGER and entrou == False:
                print("WAITINGFINGER")
                socketio.emit('message', messages.WAITINGFINGER)
            elif i == adafruit_fingerprint.IMAGEFAIL and entrou == False:
                print("IMAGEFAIL")
                socketio.emit('message', messages.IMAGEFAIL)
                return False
            elif entrou == False:
                print("OTHERERROR")
                socketio.emit('message', messages.OTHERERROR)
                return False
            
            entrou = True
            pass
        
 
        print("Passou até aqui")

        #==============================================================
        

        socketio.emit('message', messages.MODELING)
        i = finger.image_2_tz(fingerimg)
        if i == adafruit_fingerprint.OK:
            print("IF")
            socketio.emit('message', messages.MODELED)
        else:
            print(f"ELSE {i}")
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
            print("IF SEPARADO")
            socketio.emit('message', messages.REMOVEFINGER)
            while finger.get_image() != adafruit_fingerprint.NOFINGER:
                socketio.emit('message', messages.REMOVEFINGER)
                pass
            # time.sleep(1)

    print("FORA DE TUDO")
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