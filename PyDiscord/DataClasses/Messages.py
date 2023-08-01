# PyDiscord | DataClasses > Messages






#Imports
from PyDiscord.Functions.Conversions import stringToInteger, stringToBool
from PyDiscord.Functions.Dates import creationDateUTC, creationDateLocal

from PyDiscord.DataClasses.Stickers import StickerLimited
from PyDiscord.DataClasses.Attachments import Attachment
from PyDiscord.DataClasses.Embeds import Embed





#Classes
class Message:
    def __init__(self, information: dict):
        self.authorUsername = information.get('author').get('username')
        self.authorDiscriminator = int(information.get('author').get('discriminator'))
        self.authorId = int(information.get('author').get('id'))
        self.id = int(information.get('id'))
        self.content = information.get('content')
        self.Attachments = [Attachment(attachment) for attachment in information.get('attachments')]
        self.Embeds = [Embed(embed) for embed in information.get('embeds')]
        self.UserMentions = information.get('mentions')
        self.RoleMentions = information.get('mention_roles')
        self.pinned = stringToBool(information.get('pinned'))
        self.mentionedEveryone = stringToBool(information.get('mentioned_everyone'))
        self.textToSpeech = (information.get('tts'))
        self.timestamp = information.get('timestamp')
        self.editTimestamp = information.get('edited_timestamp')
        self.flags = stringToInteger(information.get('flags'))
        self.Components = information.get('components')
        
        try: self.Stickers = [StickerLimited(sticker) for sticker in information.get('sticker_items')]
        except: self.Stickers = None
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)



    def listInformation(self) -> dict:
        return self.__dict__
    


    def __repr__(self):
        return f"[{self.id}] :: {self.authorUsername} ({self.authorId})"




class MessageLimited:
    def __init__(self, information: dict):
        self.authorUsername = information.get('author').get('username')
        self.authorDiscriminator = int(information.get('author').get('discriminator'))
        self.authorId = int(information.get('author').get('id'))
        self.id = int(information.get('id'))
        self.content = information.get('content')
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)



    def listInformation(self) -> dict:
        return self.__dict__
    


    def __repr__(self):
        return f"[{self.id}] :: {self.authorUsername} ({self.authorId})"