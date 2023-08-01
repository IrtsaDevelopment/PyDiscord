# PyDiscord | DataClasses > Stickers






#Imports
from PyDiscord.Functions.Conversions import stringToBool
from PyDiscord.Functions.Dates import creationDateUTC, creationDateLocal





#Classes
class Sticker:
    def __init__(self, information: dict):
        self.name = information.get('name')
        self.id = int(information.get('id'))
        self.Tags = information.get('tags')
        self.type = information.get('type')
        self.formatType = information.get('format_type')
        self.description = information.get('description')
        self.asset = information.get('asset')
        self.available = stringToBool(information.get('available'))
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)



    def listInformation(self) -> dict:
        return self.__dict__



    def __repr__(self) -> str:
        return f"{self.name} ({self.id})"




class StickerLimited:
    def __init__(self, information: dict):
        self.name = information.get('name')
        self.id = int(information.get('id'))
        self.formatType = information.get('format_type')
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)
    

    @property
    def fullSticker(self):
        return Sticker({
            'name' : self.name,
            'id' : self.id,
            'tags' : None,
            'type' : None,
            'format_type' : self.formatType,
            'description' : None,
            'asset' : None,
            'available' : None})
    


    def listInformation(self) -> dict:
        return self.__dict__



    def __repr__(self) -> str:
        return f"{self.name} ({self.id})"