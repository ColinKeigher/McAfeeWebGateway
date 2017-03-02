import authenticate
from parse import parseData

def authImport(hostname, port, https):
    return authenticate.authenticate(hostname=hostname, port=port, https=https)

def heartBeat(auth, hostname, port=4712, https=True):
    ref = authImport(hostname=hostname, port=port, https=https)
    url = ref.createAppendURL(string='heartbeat')
    r = auth.post(url, verify=False)
    return len(r.text.split()) is 0