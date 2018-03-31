from pprint import pprint
import json


class api_gen:
    tel = {'Ben': '65da52ba54ce4f99b795a3ebaead6b02', 'default': 'abcd'}

    def __init__(self):  # this method creates the class object.
        self.importKeys()
        pass

    def importKeys(self):
        while True:
            try:
                self.tel = json.load(open("apiKeys.json"))
                break
            except IOError:
                print "No Data Input"
                print "Creating API Key File"
                self.exportKeys()
                break

    def exportKeys(self):
        json.dump(self.tel, open("apiKeys.json", 'w'))

    def addKey(self, label, key):
        self.tel[label] = key
        self.exportKeys()

    def getKey(self, key):
        a = self.tel[key]
        return a

    def printAllKeys(self):
        print "Available API Keys:"
        for x in self.tel:
            print "\t",str(x), "\t:", str(unicode(self.tel[x]))

