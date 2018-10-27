'''
Created on Oct 27, 2018

@author: peris
'''
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
        try:
            self.__initWithDict(attributes)
        except ValueError, e:
            self.logger.trace('Parameter \'attributes\' is not a dict.' + str(e))
            try:
                self.__initWithExtendedObject(attributes)
            except ValueError, e:
                self.logger.trace('Parameter \'attributes\' is not an ExtendedObject.' + str(e))
                raise ValueError('Parameter \'attributes\' must be dict or ExtendedObject, but it is '+str(type(attributes)))
            
       
    def __initWithDict(self, attributes):
        if not isinstance(attributes,dict):
            raise ValueError('Parameter \'attributes\' must be dict')
        
    def __initWithExtendedObject(self,attributes):
        if not isinstance(attributes,ExtendedObject):
            raise ValueError('Parameter \'attributes\' must be ExtendedObject')
    
   