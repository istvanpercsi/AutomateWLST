'''
Created on Oct 28, 2018

@author: peris
'''
import re
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger

class Attributes(ExtendedObject):
    '''
    Attributes Object. This is an extension for Extended Object.
    This object can process key value list from properties file, or comma or semicolon separated list.
    '''

    logger = Logger.getInstance('Attributes')

    def readAttributesFromFile(self,fileName):
        self.logger.trace('Filename: ' + str(fileName))
        attributesFile = open(fileName)
        attributesList = list()
        for attributeLine in attributesFile:
            self.logger.trace('Property line: ' + str(attributeLine))
            attributeLine = attributeLine.strip()
            regex = re.compile('^\s*[!#]+.*$')
            if len(attributeLine) != 0 and not regex.match(attributeLine): 
                self.logger.trace('Valid property line: ' + str(attributeLine))  
                attributesList.append(attributeLine)
        self.__processAttributesList(attributesList)
    
    def readAttributesFromSeparatedKeyValueList(self,separatedKeyValueList):
        attributesList = re.split(r'[,;]+', separatedKeyValueList)
        self.__processAttributesList(attributesList)
        
    def __processAttributesList(self,attributesList):
        self.logger.trace(str(attributesList))
        for attribute in attributesList:
            keyValuePair = re.split(r'[:=]+', attribute)
            self.logger.trace('Key-Value: ' + str(keyValuePair))
            self.__setattr__(str(keyValuePair[0]).strip(), str(keyValuePair[1]).strip(), True)
        
        
        