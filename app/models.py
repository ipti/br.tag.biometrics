import json

class Message:
    def __init__(self, event, code, data):
        self.event = event
        self.code = code
        self.data = data

class SearchedData:
    def __init__(self, id_finger, confidence):
        self.id_finger = id_finger
        self.confidence = confidence

class SearchedMessage(Message):
    def __init__(self, id_finger, confidence):        
        self.search_data = SearchedData(id_finger, confidence)
        Message.__init__(self, "FINGERDETECTED", 202, json.dumps(self.search_data.__dict__))
        
    def to_json():
        return json.dumps(__dict__)