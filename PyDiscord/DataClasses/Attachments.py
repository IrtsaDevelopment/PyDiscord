# PyDiscord | DataClasses > Attachments






#Imports
from math import ceil






#Classes
class Attachment():
    def __init__(self, information: dict):
        self.id = int(information.get('id'))
        self.filename = information.get('filename')
        self.size = int(information.get('size'))
        self.url = information.get('url')
        self.proxyUrl = information.get('proxy_url')
        self.width = int(information.get('width'))
        self.height = int(information.get('height'))
        self.contentType = information.get('content_type')
    

    @property
    def sizeCondense(self) -> str:
        size = int(ceil(len(str(self.size)) / 3.0) - 1)
        return str(round((self.size / (1000 ** size)), 2)) + {0:'',1:'K',2:'M',3:'G',4:'T',5:'P'}.get(size) + 'b'
    


    def listInformation(self) -> dict:
        return self.__dict__
    


    def __repr__(self) -> str:
        return f"{self.filename} ({self.id}) [{self.size}]"