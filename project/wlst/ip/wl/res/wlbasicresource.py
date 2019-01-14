'''
Created on 25.12.2018

@author: istva
'''
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger
from ip.common.attributes import Attributes

class WLBasicResource(ExtendedObject):
    
    def __init__(self, *args, **kwargs):
        self.logger = Logger.getInstance()
        
        if 'nameOfResource' in kwargs:
            self.setNameOfResource(kwargs['nameOfResource'])
        elif len(args) >= 1:
            self.setNameOfResource(args[0])
        else:
            raise ValueError('Parameter \'nameOfResource\' must be set')
        
        if 'typeOfResource' in kwargs:
            self.setTypeOfResource(kwargs['typeOfResource'])
        elif len(args) >= 2:
            self.setTypeOfResource(args[1])
        else:
            raise ValueError('Parameter \'typeOfResource\' must be set')
        
        if 'keyOfResource' in kwargs:
            self.__keyOfResource = kwargs['keyOfResource']
        elif len(args) >= 3:
            self.__keyOfResource = args[2]
        else:
            self.__keyOfResource = 'all'
        
        if 'attributes' in kwargs:
            self.__attributes = kwargs['attributes']
        elif len(args) >= 4:
            self.__attributes = args[3]
        else:
            self.__attributes = ExtendedObject()
    
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
            