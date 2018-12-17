'''
Created on Dec 17, 2018

@author: peris
'''
from ip.common.extendedobject import ExtendedObject

class WLBasicAttribute(ExtendedObject):
    '''
    classdocs
    '''


    def __init__(self, path, value):
        '''
        Constructor
        '''
        self.__path = path
        self.__value = value
    
    def set(self):
        raise NotImplementedError('WLBasicAttribute.set() has not been implemented!')
    
    def setInWL(self):
        self.set()
    
    def get(self):
        raise NotImplementedError('WLBasicAttribute.get() has not been implemented!')
    
    def getFromWL(self):
        self.get()
    
    def compare(self):
        raise NotImplementedError('WLBasicAttribute.compare() has not been implemented!')
    
    def compareWithWL(self):
        self.compare()
    
    def setPath(self, path):
        raise NotImplementedError('WLBasicAttribute.setPath() has not been implemented!')
    
    def getPath(self):
        raise NotImplementedError('WLBasicAttribute.getPath() has not been implemented!')
    
    def setValue(self, value):
        raise NotImplementedError('WLBasicAttribute.setValue() has not been implemented!')
    
    def getValue(self):
        raise NotImplementedError('WLBasicAttribute.getValue() has not been implemented!')
    