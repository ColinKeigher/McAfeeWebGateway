from authenticate import authenticate

class backup(object):
    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https

    def performBackup(self):
        r = self.auth.get(self.backupURL())
        return r.text

    def backupURL(self):
        a = authenticate(hostname=self.hostname, port=self.port, https=self.https)
        return a.createAppendURL(string='backup')