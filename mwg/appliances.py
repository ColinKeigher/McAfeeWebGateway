from authenticate import authenticate
from parse import parseData

class appliances(object):
    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https
        self.reference = authenticate(hostname=self.hostname, port=self.port, https=self.https)

    def listAppliances(self, pagesize=10, page=1):
        url = self.reference.createAppendURL(string='appliances')
        r = self.auth.get(url, params={'pageSize': pagesize, 'page': page})
        return parseData(r.text)

    def listAppliancesList(self, name=None, ltype=None):
        url = self.reference.createAppendURL(string='appliances')
        data = {}
        if ltype is not None:
            data['type'] = ltype
        if name is not None:
            data['name'] = name
        r = self.auth.get(url, params=data)
        return parseData(r.text)