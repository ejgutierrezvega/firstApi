import json

class MyException(Exception):
    def __init__(self, value, errorcode):
        self.value = value
        self.code = errorcode
    def __str__(self):
        return json.dumps({ 'errorcode': self.code, 'errordescription': self.value, 'type': 'self' }, sort_keys=True, indent=4, separators=(',', ': '))
    def valuetojson(self):
        return json.dumps({ 'errorcode': self.code, 'errordescription': self.value, 'type': 'method' }, sort_keys=True, indent=4, separators=(',', ': '))
    #pass