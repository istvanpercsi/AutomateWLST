'''
Created on 25.12.2018

@author: Istvan Percsi
'''
import wlstModule as wlst

from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger

class WLBasicResource(ExtendedObject):
    
    def __init__(self, nameOfResource, typeOfResource, keyOfResource = 'all', options = ExtendedObject()):
        self.logger = Logger.getInstance()
        self.__changeCompleted = 0
        self.__mbeanPaths = ExtendedObject()
        
        self.setNameOfResource(nameOfResource)
        self.setTypeOfResource(typeOfResource)
        self.setKeyOfResource(keyOfResource)
        self.setOptions(options)
        
    
    def setNameOfResource(self,nameOfResource):
        if isinstance(nameOfResource,str):
            self.__nameOfResource = nameOfResource
        else:
            raise ValueError('Parameter \'nameOfResource\' must be string.')
        
    def getNameOfResource(self):
        return self.__nameOfResource
    
    def setTypeOfResource(self,typeOfResource):
        if isinstance(typeOfResource,str):
            self.__typeOfResource = typeOfResource
        else:
            raise ValueError('Parameter \'typeOfResource\' must be string.')
    
    def getTypeOfResource(self):
        return self.__typeOfResource
    
    def setKeyOfResource(self,keyOfResource):
        if isinstance(keyOfResource,str):
            self.__keyOfResource = keyOfResource
        else:
            raise ValueError('Parameter \'keyOfResource\' must be string.')
    
    def getKeyOfResource(self):
        return self.__keyOfResource
    
    def setOptions(self, options):
        if isinstance(options,ExtendedObject):
            try:
                self.__attributes = options.attributes
            except KeyError, e:
                self.logger.debug('Attributes do not defined. ' + str(e))
            try:
                self.__failIf = options.failIf
            except KeyError, e:
                self.logger.debug('FailIf options do not defined. ' + str(e))
            try:
                self.__update = options.update
            except KeyError, e:
                self.logger.debug('Update options do not defined. ' + str(e))
            try:
                self.__mbeanPaths = options.mbeanPaths
            except KeyError, e:
                self.logger.debug('MbeanPaths options do not defined. ' + str(e))
        else:
            raise ValueError('Parameter \'options\' must be ExtendedObject.')
    
    def getChangeCompleted(self):
        return self.__changeCompleted
    
    def inceraseChangeCompleted(self):
        self.__changeCompleted =+ 1
        
    def convertAttributesObjectToWLAttributesObject(self):
        self.convertAttrObjToWLAttrObj()
    
    def convertAttrObjToWLAttrObj(self):
        raise NotImplementedError('Not yet implemented.')
        
    def setAttributesInWL(self):
        wlst.cd('/')
        