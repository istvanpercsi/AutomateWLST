'''
Created on Oct 28, 2018

@author: peris
'''
import re
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger

class Properties(ExtendedObject):
    '''
    Properties Object. This is an extension for Extended Object.
    This object can process key value list from properties file, or comma or semicolon separated list.
    '''

    logger = Logger.getInstance('Properties')

    def readPropertiesFromFile(self,fileName):
        self.logger.trace('Filename: ' + str(fileName))
        propertiesFile = open(fileName)
        propertiesList = list()
        for propertyLine in propertiesFile:
            self.logger.trace('Property line: ' + str(propertyLine))
            propertyLine = propertyLine.strip()
            regex = re.compile('^\s*[!#]+.*$')
            if len(propertyLine) != 0 and not regex.match(propertyLine):   
                propertiesList.append(propertyLine)
        self.__processPropertiesList(propertiesList)
    
    def readPropertiesFromSeparatedKeyValueList(self,separatedKeyValueList):
        propertiesList = re.split(r'[,;]+', separatedKeyValueList)
        self.__processPropertiesList(propertiesList)
        
    def __processPropertiesList(self,propertiesList):
        print('---> TODO')
        self.logger.trace(str(propertiesList))
        
        