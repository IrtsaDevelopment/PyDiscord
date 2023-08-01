# PyDiscord | DataClasses > Emojis






#Imports
from PyDiscord.Functions.Conversions import stringToBool
from PyDiscord.Functions.Dates import creationDateUTC, creationDateLocal





#Classes
class Emoji:
    def __init__(self, information: dict):
        self.name = information.get('name')
        self.id = int(information.get('id'))
        self.Roles = information.get('roles')
        self.requireColons = stringToBool(information.get('require_colons'))
        self.managed = stringToBool(information.get('managed'))
        self.animated = stringToBool(information.get('animated'))
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