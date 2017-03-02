import requests
from requests.auth import HTTPBasicAuth

from cache import cacheLoad, cacheSave

class authenticate(object):
    def __init__(self, hostname, port=4712, https=True):
        self.session = None
        self.target = None
        self.hostname = hostname
        self.port = port
        self.https = https
        self.cacheDir = './'
        self.cacheFile = '.cache'

    def createSession(self, username, password):
        storedSession = cacheLoad(path=self.cacheDir, filename=self.cacheFile, 
                                    hostname=self.hostname, port=self.port, 
                                    https=self.https)
        if storedSession is None:
            self.createTargetURL()
            url = self.createAppendURL(string='/login')
            self.session = requests.Session()
            n = self.session.post(url, data={'userName': username, 'pass': password}, verify=False)
            if not 'JSESSIONID' in n.cookies:
                raise Exception(n.text)
            cacheSave(path=self.cacheDir, filename=self.cacheFile, data=self.session)
        else:
            self.session = storedSession

    def destroySession(self):
        url = self.createAppendURL(string='/logout')
        self.session.get(url)

    def createTargetURL(self):
        url = '{}://{}:{}/Konfigurator/REST/'
        http = 'http'
        if self.https:
            http = 'https'
        url = url.format(http, self.hostname, self.port)
        self.target = url

    def createAppendURL(self, string):
        self.createTargetURL()
        out = self.target + string
        return out