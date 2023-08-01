# PyDiscord | Client






#Imports
from time import sleep
from PyDiscord.APIRequests import APIRequest

from PyDiscord.DataClasses.Guilds import *
from PyDiscord.DataClasses.Users import *
from PyDiscord.DataClasses.Messages import *





#Classes
class Discord:
    @staticmethod
    def __success(message) -> dict:
        return {'response' : True, 'message' : message}


    @staticmethod
    def __fail(message) -> dict:
        return {'response' : True, 'message' : message}



    def __init__(self, email: str = None, password: str = None):
        self.CurrentSession = APIRequest()

        self.email = email
        self.password = password

        self.needAuthentication = False

        self.__ticket = None
        self.__token = None
        self.__userid = None

    

    def login(self, email: str = None, password: str = None) -> dict:
        if email is None: email = self.email
        if password is None: password = self.password

        if email is None: return self.__fail('No email has been provided.')
        if password is None: return self.__fail('No password has been provided.')

        responsedata = self.CurrentSession.post('auth/login', data = {'login' : self.email, 'password' : self.password, 'undelete' : False})


        if 'ticket' in responsedata: self.__ticket = responsedata.get('ticket')
        if 'token' in responsedata: self.__token = responsedata.get('token')
        else: return self.__fail('Unable to login with given username and password.')

        if responsedata.get('mfa'): self.needAuthentication = True
        
        if self.needAuthentication: return self.__success('Authentication is needed.')

        self.CurrentSession.newHeader('Authorization', self.__token)

        responsedata = self.CurrentSession.get('users/@me')
        self.__userid = responsedata.get('id')
        
        return self.__success('Logged in.')



    def verify(self, code: int = None) -> dict:
        if code is None: return self.__fail('No code provided.')

        responsedata = self.CurrentSession.post('auth/mfa/totp', data = {'code' : int(code), 'ticket' : self.__ticket})


        if 'message' in responsedata:
            if responsedata.get('message') == 'Invalid two-factor code': return self.__fail('Invalid 2fa code.')
            return self.__fail('Unable to verify two factor authentication.')
        
        if 'token' in responsedata: 
            self.__token = responsedata.get('token')
            self.needAuthentication = False
            self.CurrentSession.newHeader('Authorization', self.__token)

            responsedata = self.CurrentSession.get('users/@me')
            self.__userid = responsedata.get('id')

            return self.__success('Successfully verified authentication code.')

        return self.__fail('Unable to verify two factor authentication.')
    


    def logout(self) -> dict:
        if self.__token is None: return self.__fail('No user to log out.')

        sleep(1)
        self.CurrentSession.post('auth/logout')
        self.CurrentSession.removeHeader('Authorization')
        return self.__success('Logged out.')
    


    def getGuild(self, guild: int | str) -> dict:
        if self.__token is None: return self.__fail('Not logged in.')

        responsedata = self.CurrentSession.get('guilds/' + str(guild))


        if 'message' in responsedata:
            if responsedata.get('message') == 'Missing Access': return self.__fail('Unable to get Guild (you must be in the Guild).')
            else: return self.__fail('Could not get Guild.')
        
        return self.__success(Guild(responsedata))
    


    def getCurrentGuilds(self) -> dict:
        if self.__token is None: return self.__fail('Not logged in.')

        responsedata = self.CurrentSession.get('users/@me/guilds')


        if 'message' in responsedata: return self.__fail('Unable to get Guilds')
        return self.__success([GuildSuperLimited(guild) for guild in responsedata])
    


    def getUser(self, user: int = None) -> dict:
        if self.__token is None: return self.__fail('Not logged in.')

        if user is None: responsedata = self.CurrentSession.get('users/' + self.__userid + '/profile')
        else: responsedata = self.CurrentSession.get('users/' + str(user) + '/profile')

        if 'message' in responsedata:
            if responsedata.get('message') == 'Missing Access':
                responsedata = self.CurrentSession.get('users/' + str(user))
                try: return self.__success(UserLimited(responsedata))
                except: return self.__fail('Unable to get User.')
            return self.__fail('Unable to get User.')
        return self.__success(User(responsedata))
    


    def getFriends(self) -> dict:
        if self.__token is None: return self.__fail('Not logged in.')

        responsedata = self.CurrentSession.get('users/@me/relationships')


        if 'message' in responsedata: return self.__fail('Unable to get Friends.')
        else:
            try: return self.__success([UserFriend(friend) for friend in responsedata if 'since' in friend])
            except: return self.__fail('Unable to get Friends.')
    


    def getMessages(self, channelId: int, limit: int = 50) -> dict:
        if self.__token is None: return self.__fail('Not logged in.')

        responsedata = self.CurrentSession.get(('channels/' + str(channelId) + '/messages'), params = {'limit' : 50})


        if 'message' in responsedata:
            if responsedata.get('message') == 'Unknown Channel': return self.__fail('Channel does not exist.')
            elif responsedata.get('message') == 'Missing Access': return self.__fail('Cannot access this channel.')
            
            return self.__fail('Unable to get channel.')
        
        return self.__success([Message(message) for message in responsedata])