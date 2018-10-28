'''
Created on Oct 27, 2018

@author: peris
'''
import re
from ip.logger.logger import Logger


class ExtendedObject(object):
    '''
    Extended Object - this is an extension for jython base object. 
    This object implements some useful functions. For Example:
    - recursive object creation
    - recursive object update if input is Extended Object
    - handle simple dictionary input, in this fall convert it to Extended Object.
    - handle extended object input
    etc.
    '''
    logger = Logger.getInstance('ExtendedObject')

    def __init__(self,attributes = dict()):
        '''
        Constructor it has two function
        1, convert dict input to an Extended Object
        2, init this object with values of external ExtendedObject. !!!WARNING!!! ONLY WITH VALUES !!!WARNING!!!
        '''
        try:
            self.__initWithDict(attributes)
            self.logger.trace('Parameter \'attributes\' is a dictionary')
        except ValueError, e:
            self.logger.trace('Parameter \'attributes\' is not a dictionary. ' + str(e))
            try:
                self.__initWithExtendedObject(attributes)
                self.logger.trace('Parameter \'attributes\' is an ExtendedObject')
            except ValueError, e:
                self.logger.trace('Parameter \'attributes\' is not an ExtendedObject.' + str(e))
                raise ValueError('Parameter \'attributes\' must be dictionary or ExtendedObject, but it is '+str(type(attributes)))
            
       
    def __initWithDict(self, attributes):
        if not isinstance(attributes,dict):
            raise ValueError('Parameter \'attributes\' must be dict')
        for key in attributes:
            self.__setattr__(key,attributes[key])
        
    def __initWithExtendedObject(self,attributes):
        if not isinstance(attributes,ExtendedObject):
            raise ValueError('Parameter \'attributes\' must be ExtendedObject')
        for key in attributes.__dict__:
            self.__setattr__(key,attributes.__dict__[key])
            
    
    def __setattr__(self, key, value, update = False):
        '''
        __setattr__ function of object. With this extension it can process point separated keys
        '''
        self.logger.setNameOfFunction('__setattr__')
        self.__testKeyValidity(key)
        keys = key.split('.')
        self.logger.trace('Keys are: ' + str(keys))
        if keys[0] in self.__dict__:
            self.logger.trace('Key \'' + keys[0] + '\' is in \'self.__dict__\'')
            if len(keys) > 1:
                self.logger.trace('There are more rest keys. They are: ' + str(keys[1:]))
                if isinstance(self.__dict__[keys[0]],ExtendedObject):
                    self.__dict__[keys[0]].__setattr__('.'.join(keys[1:]),value)
                else:
                    self.__dict__[keys[0]] = ExtendedObject('.'.join(keys[1:]),value)
            else:
                self.logger.trace('There is no more rest key. Last key is: ' + str(key))
                if isinstance(value,dict):
                    self.logger.trace('Value of parameter \'value\' is a dictionary.')
                    if isinstance(self.__dict__[keys[0]],ExtendedObject) and update:
                        self.logger.trace('Value of key \'' + keys[0] + '\' in actual object is an ExtendedObject')
                        self.__dict__[keys[0]] = self.__convertDictToExtendedObject(value, self.__dict__[keys[0]])
                    else:
                        self.logger.trace('Value of key \'' + keys[0] + '\' in actual object is not an ExtendedObject')
                        self.__dict__[keys[0]] = self.__convertDictToExtendedObject(value, ExtendedObject())
                elif isinstance(value,ExtendedObject):
                    self.logger.trace('Value of parameter \'value\' is an ExtendedObject')
                    if isinstance(self.__dict__[keys[0]],ExtendedObject) and update:
                        self.logger.trace('Value of key \'' + keys[0] + '\' in actual object is an ExtendedObject')
                        self.__dict__[keys[0]] = self.__convertDictToExtendedObject(value.__dict__, self.__dict__[keys[0]])
                    else:
                        self.logger.trace('Value of key \'' + keys[0] + '\' in actual object is not an ExtendedObject')
                        self.__dict__[keys[0]] = value
                else:
                    self.logger.trace('Value of Parameter \'value\' is not a dictionary or an ExtendedObject.')
                    self.__dict__[keys[0]] = value
        else:
            self.logger.trace('Key \'' + keys[0] + '\' is not in \'self.__dict__\'')
            if len(keys) > 1:
                self.logger.trace('There are more rest keys. They are: ' + str(keys[1:]))
                self.__dict__[keys[0]] = ExtendedObject({'.'.join(keys[1:]):value})
            else:
                self.logger.trace('There is no more rest key. Last key is: ' + str(key))
                if isinstance(value,dict):
                    self.logger.trace('Value of parameter \'value\' is a dictionary.')
                    self.__dict__[keys[0]] = self.__convertDictToExtendedObject(value, ExtendedObject())
                else:
                    self.logger.trace('Value of parameter \'value\' is not a dictionary.')
                    self.__dict__[keys[0]] = value
        self.logger.setNameOfFunction('')
            
    
    def __convertDictToExtendedObject(self,d,e):
        self.logger.setNameOfFunction('__convertDictToExtendedObject')
        if not isinstance(e,ExtendedObject):
            raise ValueError('Parameter \'e\' must be ExtendedObject')
        for k in d:
            self.logger.trace('Adding key: \'' + str(k) + '\' - value: \'' + str(d[k]) + '\' to ExtendedObject')
            e.__setattr__(k, d[k])
        self.logger.setNameOfFunction('')
        return e
    
    def __testKeyValidity(self,key):
        regexPattern = '^[a-zA-Z]?[a-zA-Z0-9\.]*$'
        compliedRegex = re.compile(regexPattern)
        if not compliedRegex.match(key):
            self.logger.trace('Key cannot be contain special characters, only english letters and arabic numbers. This key is invalid: \'' + str(key) + '\'')
            raise KeyError('Key cannot be contain special characters, only english letters and arabic numbers. This key is invalid: \'' + str(key) + '\'')
        
        
        