import xmltodict

def parseData(data):
    try:
        return xmltodict.parse(data)
    except:
        if len(data.split()) is 0:
            return None
        else:
            raise Exception('Invalid XML data', data)

