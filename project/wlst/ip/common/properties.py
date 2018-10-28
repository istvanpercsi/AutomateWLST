'''
Created on Oct 28, 2018

@author: peris
'''
import re
from ip.common.extendedobject import ExtendedObject

class Properties(ExtendedObject):
    '''
    Properties Object. This is an extension for Extended Object.
    This object can process key value list from properties file, and comma or semicolon separated key value list.
    '''

    def readPropertiesFromFile(self,fileName):
        propertiesFile = open(fileName)
        propertiesList = list()
        for propertyLine in propertiesFile:
            propertyLine = propertyLine.strip()
            regex = re.compile('^\s(!|#).*$')
            if not len(propertyLine) != 0 and not regex.match(propertyLine):   
                self.__propertiesList.append(propertyLine)
        self.__processPropertiesList(propertiesList)
    
    def readPropertiesFromSeparatedKeyValueList(self,separatedKeyValueList):
        propertiesList = re.split(r'[,;]+', separatedKeyValueList)
        self.__processPropertiesList(propertiesList)
        
    def __processPropertiesList(self,propertiesList):
        print('---> TODO')
        