import time
import serial
from tkinter import messagebox


import adafruit_fingerprint

from app import messages

class FingerprintController:
    def __init__(self, port):                
        uart = serial.Serial(port, baudrate=57600, timeout=1)                    
        self.finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)            
        

    async def get_fingerprint(self, socketio):
        await socketio.emit('message', messages.WAITINGIMAGE)
        while self.finger.get_image() != adafruit_fingerprint.OK:
            await socketio.sleep(1)
            pass
        await socketio.emit('message', messages.MODELING)
        if self.finger.image_2_tz(1) != adafruit_fingerprint.OK:
            return False
        await socketio.emit('message', messages.SEARCHING)
        if self.finger.finger_search() != adafruit_fingerprint.OK:
            return False
        return True


    def get_fingerprint_detail(self):
        print("Getting image...")
        i = self.finger.get_image()
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
        i = self.finger.image_2_tz(1)
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
        i = self.finger.finger_fast_search()
        if i == adafruit_fingerprint.OK:
            print("Found fingerprint!")
            return True
        else:
            if i == adafruit_fingerprint.NOTFOUND:
                print("No match found")
            else:
                print("Other error")
            return False

    async def enroll_finger(self, location, socketio):
        for fingerimg in range(1, 3):
            if fingerimg == 1:
                await socketio.emit('message', messages.PUTFINGER)
            else:
                await socketio.emit('message', messages.PUTFINGERAGAIN)

            while True:
                i = self.finger.get_image()
                if i == adafruit_fingerprint.OK:
                    await socketio.emit('message', messages.PICTURETAKEN)
                    break
                if i == adafruit_fingerprint.NOFINGER:
                    await socketio.emit('message', messages.WAITINGFINGER)
                elif i == adafruit_fingerprint.IMAGEFAIL:
                    await socketio.emit('message', messages.IMAGEFAIL)
                    return False
                else:
                    await socketio.emit('message', messages.OTHERERROR)
                    return False

            await socketio.emit('message', messages.MODELING)
            i = self.finger.image_2_tz(fingerimg)
            if i == adafruit_fingerprint.OK:
                await socketio.emit('message', messages.MODELED)
            else:
                if i == adafruit_fingerprint.IMAGEMESS:
                    await socketio.emit('message', messages.CONFUSINGIMAGE)
                elif i == adafruit_fingerprint.FEATUREFAIL:
                    await socketio.emit('message', messages.NOTIDENTIFTRESOURCES)
                elif i == adafruit_fingerprint.INVALIDIMAGE:
                    await socketio.emit('message', messages.INVALIDIMAGE)
                else:
                    await socketio.emit('message', messages.OTHERERROR)
                return False
            if fingerimg == 1:
                await socketio.emit('message', messages.REMOVEFINGER)
                time.sleep(1)
                while i != adafruit_fingerprint.NOFINGER:
                    i = self.finger.get_image()

        await socketio.emit('message', messages.MODELING)
        i = self.finger.create_model()
        if i == adafruit_fingerprint.OK:
            await socketio.emit('message', messages.CARRER)
        else:
            if i == adafruit_fingerprint.ENROLLMISMATCH:
                await socketio.emit('message', messages.FINGERSNOTMATCH)
            else:
                await socketio.emit('message', messages.OTHERERROR)
            return False
        i = self.finger.store_model(location)
        if i == adafruit_fingerprint.OK:
            await socketio.emit('message', messages.STORED)
        else:
            if i == adafruit_fingerprint.BADLOCATION:
                await socketio.emit('message', messages.BADSTORAGELOCATION)
            elif i == adafruit_fingerprint.FLASHERR:
                await socketio.emit('message', messages.FLASHSTORAGEERROR)
            else:
                await socketio.emit('message', messages.OTHERERROR)
            return False

        return True