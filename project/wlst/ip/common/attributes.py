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
            keyValuePair = re.split(r'[:=\s]+', attribute,1)
            self.logger.trace('Key-Value pair: ' + str(keyValuePair))
            self.__setattr__(str(keyValuePair[0]).strip(), self.__convertValueToDataSequence(str(keyValuePair[1]).strip()), True)
    
    def __convertValueToDataSequence(self,value):
        try:
            return self.__convertToBoolean(value)
        except:
            try:
                return self.__convertToInteger(value)
            except:
                try:
                    return self.__convertToString(value)
                except:
                    raise ValueError('Value \'' + str(value) + '\' cannot be converted to any type')
        
    def __convertToString(self,value):
        self.logger.trace('Try to convert value \'' + str(value) + '\' to string...')
        ret = str(value)
        self.logger.trace('Conversion success.')
        return ret
    
    def __convertToInteger(self,value): 
        try:
            self.logger.trace('Try to convert value \'' + str(value) + '\' to integer...')
            ret = int(value)
            self.logger.trace('Conversion success.')
            return ret
        except ValueError, e:
            self.logger.trace('Conversion failed.')
            raise e
        
    def __convertToBoolean(self,value):
        self.logger.trace('Try to convert value \'' + str(value) + '\' to boolean...')
        if str(value).lower() == 'true':
            self.logger.trace('Conversion success.')
            return True
        elif str(value).lower() == 'false':
            self.logger.trace('Conversion success.')
            return False
        else:
            self.logger.trace('Conversion failed.')
            raise ValueError('Value \'' + value + '\' cannot be converted to boolean')
    