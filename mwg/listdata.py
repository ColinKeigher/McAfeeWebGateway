from authenticate import authenticate
from parse import parseData
from process import process

class listdata(object):
    def __init__(self, auth, hostname, port=4712, https=True):
        self.auth = auth
        self.hostname = hostname
        self.port = port
        self.https = https

    def listData(self, pagesize=100, page=1):
        r = self.auth.get(self.listURL(), params={'pageSize': pagesize})
        p = process(data=parseData(r.text))
        data = p.processList()
        pages = p.processPages()
        if len(pages) is not 1:
            data = [data]
            for page in pages:
                r = self.auth.get(self.listURL(), params={'pageSize': pagesize, 'page': page})
                p = process(data=parseData(r.text))
                data.append(p.processList())
            p = process(data=data)
            data = p.processListCombine()
        return data

    def listID(self, value):
        r = self.auth.get(self.listURL(value=value))
        p = process(data=parseData(r.text))
        return p.processListID()

    def listIDInsert(self, value, entry, description, position=1):
        u = self.listURL(value=value, entry=position)
        i = '''<entry xmlns="http://www.w3org/2011/Atom">
                    <content type="application/xml">
                        <listEntry>
                            <entry>{}</entry>
                            <description>{}</description>
                        </listEntry>
                    </content> 
                </entry>'''
        i = i.format(entry, description)
        r = self.auth.post(u, data=i, headers={'Content-Type': 'application/xml'})
        return parseData(r.text)

    def listURL(self, value=None, entry=None):
        a = authenticate(hostname=self.hostname, port=self.port, https=self.https)
        string = 'list'
        if value is not None:
            string = '{}/{}'.format(string, value)
        if entry is not None:
            string = '{}/entry/{}/insert'.format(string, entry)
        return a.createAppendURL(string=string)