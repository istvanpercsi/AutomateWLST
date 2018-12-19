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
    def __init__(self, attributes=dict()):
        ExtendedObject.__init__(self, attributes=attributes)
        self.logger = Logger.getInstance()
    

    def readAttributesFromFile(self,fileName):
        self.logger.setNameOfFunction('readAttributesFromFile')
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
        self.logger.setNameOfFunction('')
    
    def readAttributesFromSeparatedKeyValueList(self,separatedKeyValueList):
        attributesList = re.split(r'[,;]+', separatedKeyValueList)
        self.__processAttributesList(attributesList)
        
    def __processAttributesList(self,attributesList):
        self.logger.setNameOfFunction('__processAttributesList')
        self.logger.trace(str(attributesList))
        for attribute in attributesList:
            keyValuePair = re.split(r'[:=]+', attribute)
            self.logger.trace('Key-Value pair: ' + str(keyValuePair))
            self.__setattr__(str(keyValuePair[0]).strip(), str(keyValuePair[1]).strip(), True)
        self.logger.setNameOfFunction('')
        
        