import dill as pickle
import os

from heartbeat import heartBeat

def cacheFileExists(path, filename):
    return os.path.exists(cacheFilename(path, filename))

def cacheFilename(path, filename):
    return os.path.join(path, filename)

def cacheLoad(path, filename, hostname, port=4712, https=True):
    out = None
    if cacheFileExists(path, filename):
        session = pickle.load(open(cacheFilename(path, filename), 'rb'))
        if heartBeat(auth=session, hostname=hostname, port=port, https=https):
            return session
    return out

def cacheSave(path, filename, data):
    filename = cacheFilename(path, filename)
    pickle.dump(data, open(filename, 'wb'))