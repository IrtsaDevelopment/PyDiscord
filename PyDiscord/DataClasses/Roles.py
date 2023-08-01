# PyDiscord | DataClasses > Roles






#Imports
from PyDiscord.Functions.Conversions import *
from PyDiscord.Functions.Dates import creationDateUTC, creationDateLocal





#Classes
class Role:
    def __init__(self, information: dict, guild: int):
        self.name = information.get('name')
        self.id = int(information.get('id'))
        self.description = information.get('description')
        self.permissions = information.get('permissions')
        self.position = stringToInteger(information.get('position'))
        self.color = information.get('color')
        self.hoist = stringToInteger(information.get('hoist'))
        self.managed = stringToBool(information.get('managed'))
        self.mentionable = stringToBool(information.get('mentionable'))
        self.flags = stringToInteger(information.get('flags'))
        self.unicodeEmoji = information.get('unicode_emoji')

        if detectNone(information.get('icon')): self.icon = None
        else: self.icon: str = 'https://cdn.discordapp.com/role-icons/' + str(guild) + '/' + information.get('icon') + '.webp?size=96&quality=lossless'
    

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