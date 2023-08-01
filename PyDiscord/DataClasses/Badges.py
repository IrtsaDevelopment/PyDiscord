# PyDiscord | DataClasses > Badges






#Classes
class Badge:
    def __init__(self, information: dict):
        self.id = int(information.get('id'))
        self.description = information.get('description')
        self.icon = 'https://cdn.discordapp.com/badge-icons/' + information.get('icon') + '.png'
        self.link = information.get('link')
    


    def listInformation(self) -> dict:
        return self.__dict__
    


    def __repr__(self):
        return str(self.id)