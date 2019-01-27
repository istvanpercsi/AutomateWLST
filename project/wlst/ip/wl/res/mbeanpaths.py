'''
Created on 27.01.2019

@author: Istvan Percsi
'''
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger

class MBeanPaths(ExtendedObject):
    
    def __init__(self, attributes=dict()):
        self.logger = Logger.getInstance()
        self.__convertExtendedObjectToMBeanPath(attributes)
    
    def __convertExtendedObjectToMBeanPath(self,options):
        for k,v in options:
            if isinstance(v,ExtendedObject):
                self.setAttr(k, MBeanPaths(v))
            elif isinstance(v,str):
                self.__complieValue(k, v)
            else:
                self.logger.debug('Value can be str or ExtendedObject, but it is ' + str(type(v)))
                raise ValueError('Value can be str or ExtendedObject, but it is ' + str(type(v)))
                
    def __complieValue(self,key,value):
        self.__setToString(key, value)
    
    def __setToString(self,key, value):
        if value[0] == '"' and value[-1] == '"':
            self.setAttr(key, str(value[1:-2]))
        else:
            self.setAttr(key, str(value))
        
        
    
    
   
        