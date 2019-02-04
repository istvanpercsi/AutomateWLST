'''
Created on 25.12.2018

@author: Istvan Percsi
'''
import re
import wlstModule as wlst

from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger
from ip.common.common import Common
from ip.wl.res.mbeanpaths import MBeanPaths

class WLBasicResource(ExtendedObject):
    
    def __init__(self, nameOfResource, typeOfResource, keyOfResource = 'all', options = ExtendedObject()):
        self.logger = Logger.getInstance()
        self.__changeCompleted = 0
        
        self.setNameOfResource(nameOfResource)
        self.setTypeOfResource(typeOfResource)
        self.setKeyOfResource(keyOfResource)
        self.setOptions(options)
        
        #self.checkExistanceOfResourceInWL()
        
    
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
                self.__editMethod = options.editMethod
            except KeyError, e:
                self.logger.debug('Edit options do not defined. ' + str(e))
            try:
                self.__mbeanPaths = MBeanPaths(options.mbeanPaths)
            except KeyError, e:
                self.logger.debug('MbeanPaths options do not defined. ' + str(e))
        else:
            raise ValueError('Parameter \'options\' must be ExtendedObject.')
    
    def getOptionUpdateEnabled(self):
        try:
            return Common.toBoolean(self.__editMethod.updateEnabled)
        except KeyError, e:
            self.logger.debug('Key: self.__editMethod.updateEnabled has not been set. Return with true. ' + str(e))
            return True
            
    def getOptionCreateEnabled(self):
        try:
            return Common.toBoolean(self.__editMethod.createEnabled)
        except KeyError, e:
            self.logger.debug('Key: self.__editMethod.createEnabled has not been set. Return with true. ' + str(e))
            return True
    
    def checkExistanceOfResourceInWL(self):
        try:
            self.logger.debug('Check existance of resource \'' + self.getNameOfResource() + '\' in WebLogic. ')
            self.logger.trace('Command: cd edit:/' + self.getTypeOfResources() + '/' + self.getNameOfResource())
            wlst.cd('edit:/' + self.getTypeOfResources() + '/' + self.getNameOfResource())
            wlst.cd('/')
            self.__existsInWeblogic = True
            self.logger.debug('Resource \'' + self.getTypeOfResource() + '\' with name \'' + self.getNameOfResource() + '\' exists in Weblogic')
        except:
            self.__existsInWeblogic = False
            self.log.debug('Resource \'' + self.getTypeOfResource() + '\' with name \'' + self.getNameOfResource() + '\' does not exist in Weblogic')
    
    def getExistsInWeblogic(self):
        return self.__existsInWeblogic
    
    def getChangeCompleted(self):
        return self.__changeCompleted
    
    def inceraseChangeCompleted(self):
        self.__changeCompleted =+ 1
        
    def convertAttributesObjectToMBeanPaths(self):
        self.convertAttrObjToMBeanPath()
    
    def convertAttrObjToMBeanPath(self):
        raise NotImplementedError('Not yet implemented.')
        
    def setAttributesInWL(self):
        wlst.cd('edit:/')
        if self.getExistsInWeblogic() and self.getOptionEditEnabled():
            self.logger.debug('Resource with name exists in WebLogic, and edit is enabled. Editing attributes of resource...')
            #todo edit
        elif not self.getExistsInWeblogic() and self.getOptionEditEnabled():
            self.logger.debug('Resource with name does not exist in WebLoic, but edit is enabled. Create new resource...')
            #tod create
        elif self.getExistsInWeblogic() and self.getOptionEditEnabled():
            self.logger.debug('Resource with name exists in Weblogic but edit is not enabled. Exiting...')
        elif not self.getExistsInWeblogic() and not self.getOptionEditEnabled():
            self.logger.debug('Resource with name does not exist in WebLogic, and edit is not enabled. Exiting...')
        
        
        