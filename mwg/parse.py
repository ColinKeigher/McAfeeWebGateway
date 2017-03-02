import xmltodict

def parseData(data):
    try:
        return xmltodict.parse(data)
    except:
        raise Exception('Invalid data', data)

