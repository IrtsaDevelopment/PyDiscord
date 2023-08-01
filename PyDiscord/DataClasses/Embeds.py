# PyDiscord | DataClasses > Embeds






#Classes
class Embed:
    class EmbedThumbnail:
        def __init__(self, information: dict):
            self.url = information.get('url')
            self.proxyUrl = information.get('proxy_url')
            self.width = int(information.get('width'))
            self.height = int(information.get('height'))

        def listInformation(self) -> dict: return self.__dict__
        
        def __repr__(self): return self.url
    


    class EmbedVideo:
        def __init__(self, information: dict):
            self.url = information.get('url')
            self.proxyUrl = information.get('proxy_url')
            self.width = int(information.get('width'))
            self.height = int(information.get('height'))

        def listInformation(self) -> dict: return self.__dict__
        
        def __repr__(self): return self.url



    def __init__(self, information: dict):
        self.eType = information.get('type')
        self.url = information.get('url')
        self.thumbnail = Embed.EmbedThumbnail(information.get('thumbnail'))
        self.video = Embed.EmbedVideo(information.get('thumbnail'))
    


    def listInformation(self) -> dict:
        return self.__dict__



    def __repr__(self):
        return self.url