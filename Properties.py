import ConfigParser
import os

def getPropertie(section, property):
    dir = os.path.dirname(__file__)
    config = ConfigParser.ConfigParser()
    config.read(dir + '/config.cfg')
    return config.get(section, property)