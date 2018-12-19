'''
Created on 06.08.2018

@author: percsii
'''
from ip.logger.logger import Logger

class Common(object):
    
    
    
    def __init__(self):
        self.logger = Logger.getInstance()

    
    def toBoolean(booleanString):
        if booleanString.lower() == 'yes' or booleanString.lower() == 'true' or str(booleanString) == '1':
            return True
        elif booleanString.lower() == 'no' or booleanString.lower() == 'false' or str(booleanString) == '0' or str(booleanString) == '':
            return False
        raise ValueError('Invalid boolean string: %' % booleanString)
    
    toBoolean = staticmethod(toBoolean)
    
    def booleanToString(boolValue,returnType='tf'):
        if not isinstance(boolValue,int):
            raise ValueError('Parameter \'boolValue\' must be boolean')            
        if str(returnType) == 'tf':
            if boolValue:
                return 'true'
            else:
                return 'false'
        elif str(returnType) == 'yn':
            if boolValue:
                return 'yes'
            else:
                return 'no'
        elif str(returnType) == '10':
            if boolValue:
                return 1
            else:
                return 0
        else:
            raise ValueError('Parameter \'returnType\' must be \'tf\', \'yn\', \'10\' ')
        
    booleanToString = staticmethod(booleanToString)