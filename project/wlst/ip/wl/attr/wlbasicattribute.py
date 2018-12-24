'''
Created on Dec 17, 2018

@author: peris
'''
import wlstModule as wlst
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger

class WLBasicAttribute(ExtendedObject):
    '''
    Basic Attribute Class for attributes of resource with basic functions.
    '''
    def __init__(self, name, value = None):
        '''
        Constructor
        '''
        self.logger = Logger.getInstance()
        self.__name = self.setName(name)
        self.__value = self.setValue(value)
    
    def set(self):
        '''
        Set value of attribute in Weblogic. Context must be set.
        '''
        wlst.set(self.__name,self.__value)
    
    def setInWL(self):
        '''
        Alias for WLBasicAttributes.set()
        '''
        self.set()
    
    def get(self):
        '''
        Get value of attribute from WebLogic. Context must be set.
        '''
        self.__value = wlst.get(self.__name)
    
    def getFromWL(self):
        '''
        Alias for WLBasicAttributes.get()
        '''
        self.get()
    
    def compare(self):
        '''
        Compare actual value with value from WebLogic
        '''
        if self.value == wlst.get(self.__name):
            return True
        else:
            return False
    
    def compareWithWL(self):
        '''
        Alias for WLBasicAttributes.compare()
        '''
        self.compare()
    
    def setName(self, name):
        if isinstance(name,str):
            self.__name = name
        else:
            self.logger.error('Value of parameter \'name\' must be string.')
    
    def getName(self):
        return self.__name 
    
    def setValue(self, value):
        self.__value = value
    
    def getValue(self):
        return self.value
    