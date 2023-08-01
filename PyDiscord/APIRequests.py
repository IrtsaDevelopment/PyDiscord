# PyDiscord | APIRequests






#Imports
from requests import Session
from json import loads, dumps





#Classes
class APIRequest:
    @staticmethod
    def __getParams(params: dict) -> str:
        if len(params) == 0: params = ''
        else: params = '?' + ''.join([(str(p) + '=' + str(params.get(p)) + '&') for p in params])

        return params
    


    def __init__(self):
        self.CurrentSession: Session = Session()

        self.baseUrl: str = 'https://discord.com/api/v9/'
        self.headers: dict = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36', 'Content-Type' : 'application/json'}
    


    def newHeader(self, header, value):
        try: self.headers[header] = value
        except: pass   



    def removeHeader(self, header):
        try: self.headers.pop(header)
        except: pass

    

    def get(self, endpoint: str, params: dict = {}):
        return loads(self.CurrentSession.get((self.baseUrl + endpoint + self.__getParams(params)), headers = self.headers).__dict__.get('_content'))
    


    def post(self, endpoint, params = {}, data = None):
        return loads(self.CurrentSession.post((self.baseUrl + endpoint + self.__getParams(params)), headers = self.headers, data = dumps(data)).__dict__.get('_content'))