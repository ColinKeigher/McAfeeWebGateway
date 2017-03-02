from tools import mergeDict

import urlparse

class process(object):
    def __init__(self, data):
        self.data = data

    def isFeedData(self):
        return 'feed' in self.data

    def processPages(self):
        d = self.data['feed']['link']
        f, l = None, None
        if len(d) is not 1:
            for i in d:
                n = urlparse.urlparse(i['@href']).query
                n = int(urlparse.parse_qs(n)['page'][0])
                if i['@rel'] == 'first':
                    f = n
                if i['@rel'] == 'last':
                    l = n
        if f + 1 == l:
            out = [f]
        else:
            out = list(xrange(f + 1, l))
        return out

    def processList(self):
        out = {}
        out['source'] = self.data['feed']['title']
        out['data'] = self.processListEntry()
        return out

    def processListCombine(self):
        out = {'data': {}}
        for item in self.data:
            out['source'] = item['source']
            out['data'] = mergeDict(out['data'], item['data'])
        return out

    def processListEntry(self):
        o = {}
        for e in self.data['feed']['entry']:
            tag = e['id']
            o[tag] = {}
            o[tag]['title'] = e['title']
            o[tag]['type'] = e['listType']
        return o

    def processListID(self):
        out = {'data': {}}
        d = self.data['entry']
        out['source'] = d['id']
        out['title'] = d['title']
        out['type'] = d['type']
        out['listType'] = d['listType']
        for item in d['content']['list']['content']['listEntry']:
            e = item['entry']
            d = item['description']
            out['data'][e] = d
        return out