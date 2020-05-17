from configparser import ConfigParser

def configRead(section,key):
    objconfig=ConfigParser()
    objconfig.read("./ConfigFiles/config.cfg")
    return objconfig.get(section,key)


def locatorRead(section,key):
    objlocator=ConfigParser()
    objlocator.read("./ConfigFiles/locators.cfg")
    return objlocator.get(section,key)

