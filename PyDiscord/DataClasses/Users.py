# PyDiscord | DataClasses > Users






#Imports
from PyDiscord.Functions.Conversions import stringToInteger, stringToBool, detectNone
from PyDiscord.Functions.Dates import creationDateUTC, creationDateLocal, dateToUTC, dateToLocal

from PyDiscord.DataClasses.Badges import Badge





#Classes
class User:
    class AccountConnection:
        def __init__(self, information: dict):
            self.type = information.get('connected_accounts').get('type')
            self.id = int(information.get('connected_accounts').get('id'))
            self.name = information.get('connected_accounts').get('name')
            self.verified = stringToBool(information.get('connected_accounts').get('verified'))
        

        def listInformation(self) -> dict: self.__dict__

        def __repr__(self): return self.type
    

    @staticmethod
    def __getNitro(nid: int) -> str:
        return {0 : None, 1 : 'Nitro Classic', 2 : 'Nitro', 3 : 'Nitro Basic'}



    def __init__(self, information: dict):
        self.id = int(information.get('user').get('id'))
        self.username = information.get('user').get('username')
        self.displayname = information.get('user').get('global_name')
        self.avatar = 'https://cdn.discordapp.com/avatars/' + str(self.id) + '/' + information.get('user').get('avatar') + '.png'
        self.discriminator = int(information.get('user').get('discriminator'))
        self.flags = stringToInteger(information.get('user').get('flags'))
        self.flagsPublic = stringToInteger(information.get('user').get('flags'))
        self.banner = information.get('user').get('banner')
        self.bannerColor = information.get('user').get('banner_color')
        self.accentColorv = information.get('user').get('accent_color')
        self.bio = information.get('user').get('bio')
        self.avatarDecoration = information.get('user').get('avatar_decoration')
        self.ConnectedAccounts = [User.AccountConnection(account) for account in information.get('connected_accounts')]
        self.premiumType = self.__getNitro(information.get('premium_type'))
        self.profileThemesExperimentBucket = information.get('profile_themes_experiment_bucket')
        self.sharedGuilds = [guild.get('id') for guild in information.get('mutual_guilds')]
        self.guildNickNames = [guild.get('nick') for guild in information.get('mutual_guilds')]
        self.pronouns = information.get('pronouns')
        self.Badges = [Badge(badge) for badge in information.get('badges')]
        
        try: self.legacyUsername = information.get('legacy_username')
        except: self.legacyUsername = None

        if not detectNone(self.banner): self.banner = 'https://cdn.discordapp.com/banners/' + str(self.id) + '/' + self.banner + '.png'

        if not detectNone(information.get('premium_since')):
            self.premiumDateUTC = dateToUTC(information.get('premium_since'))
            self.premiumDateLocal = dateToLocal(information.get('premium_since'))
        else:
            self.premiumDateUTC = None
            self.premiumDateLocal = None
        
        if not (information.get('premium_guild_since')):
            self.guildBoostDateUTC = dateToUTC(information.get('premium_guild_since'))
            self.guildBoostDateLocal = dateToLocal(information.get('premium_guild_since'))
        else:
            self.guildBoostDateUTC = None
            self.guildBoostDateLocal = None

    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)
        


    def listInformation(self) -> dict:
        return self.__dict__
    


    def __repr__(self):
        return f"{self.username} ({self.id})"




class UserLimited:
    def __init__(self, information):
        self.id = int(information.get('id'))
        self.username = information.get('username')
        self.displayname = information.get('global_name')
        self.avatar = 'https://cdn.discordapp.com/avatars/' + str(self.id) + '/' + information.get('avatar') + '.png'
        self.discriminator = int(information.get('discriminator'))
        self.flags = stringToInteger(information.get('flags'))
        self.flagsPublic = stringToInteger(information.get('public_flags'))
        self.banner = information.get('banner')
        self.bannerColor = information.get('banner_color')
        self.accentColor = information.get('accent_color')
        self.avatarDecoration = information.get('avatar_decoration')

        if not detectNone(self.banner): self.banner: str = 'https://cdn.discordapp.com/banners/' + str(self.id) + '/' + self.banner + '.png'
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)
        


    def listInformation(self) -> dict:
        return self.__dict__
    


    def __repr__(self):
        return f"{self.username} ({self.id})"




class UserFriend:
    def __init__(self, information):
        self.id = int(information.get('user').get('id'))
        self.username = information.get('user').get('username')
        self.displayname = information.get('user').get('global_name')
        self.avatar = 'https://cdn.discordapp.com/avatars/' + str(self.id) + '/' + information.get('user').get('avatar') + '.png'
        self.discriminator = int(information.get('user').get('discriminator'))
        self.flagsPublic = stringToInteger(information.get('user').get('public_flags'))
        self.avatarDecoration = information.get('user').get('avatar_decoration')
        self.friendSinceUTC = dateToUTC(information.get('since'))
        self.friendSinceLocal = dateToLocal(information.get('since'))
    

    @property
    def creationDateUTC(self) -> str:
        return creationDateUTC(self.id)
    

    @property
    def creationDateLocal(self) -> str:
        return creationDateLocal(self.id)
        


    def listInformation(self) -> dict:
        return self.__dict__
    


    def __repr__(self):
        return f"{self.username} ({self.id})"