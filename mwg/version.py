from authenticate import authenticate
from parse import parseData

class version(object):
    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https

    def checkVersion(self):
        r = self.auth.get(self.versionURL())
        return parseData(r.text)

    def versionURL(self):
        a = authenticate(hostname=self.hostname, port=self.port, https=self.https)
        return a.createAppendURL(string='version')