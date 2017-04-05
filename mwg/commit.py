from authenticate import authenticate
from parse import parseData

class commit(object):
    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.reference = authenticate(hostname=self.hostname, port=self.port, https=self.https)

    def commitData(self, pagesize=10, page=1):
        url = self.reference.createAppendURL(string='commit')
        r = self.auth.post(url)
        return parseData(r.text)