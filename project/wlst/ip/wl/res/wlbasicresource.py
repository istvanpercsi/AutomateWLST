'''
Created on 25.12.2018

@author: Istvan Percsi
'''
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger

class WLBasicResource(ExtendedObject):
    
    def __init__(self, nameOfResource, typeOfResource, keyOfResource = 'all', attributes = ExtendedObject()):
        self.logger = Logger.getInstance()
        self.__changeCompleted = 0
        self.__wlAttributesObject = ExtendedObject()
        
        self.setNameOfResource(nameOfResource)
        self.setTypeOfResource(typeOfResource)
        self.setKeyOfResource(keyOfResource)
        self.setAttributes(attributes)
        
    
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
    
    def setAttributes(self, attributes):
        if isinstance(attributes,ExtendedObject):
            self.__attributes = attributes
        else:
            raise ValueError('Parameter \'attributes\' must be ExtendedObject.')
    
    def getChangeCompleted(self):
        return self.__changeCompleted
    
    def inceraseChangeCompleted(self):
        self.__changeCompleted =+ 1
        
    def convertAttributesObjectToWLAttributesObject(self):
        self.convertAttrObjToWLAttrObj()
    
    def convertAttrObjToWLAttrObj(self):
        raise NotImplementedError('Not yet implemented.')
        
        
        