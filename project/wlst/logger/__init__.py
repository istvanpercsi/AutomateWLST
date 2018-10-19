'''
Created on 19.10.2018

@author: Istvan Percsi
@contact: istvanpercsi@gmail.com
@license: MIT
'''

class Logger(object):
    '''
    This is a Standard logger class. It logs messages on console based on errorlevel (0-5) and enabled name of class/function.
    Default error level is: ERROR (4)
    Default class is: *
    Default function is: *
    '''
       
    level = 4
    
    def __init__(self,nameOfClass,nameOfFunction = ''):
        self.nameOfClass = nameOfClass
        self.nameOfFunction = nameOfFunction
        
    def getInstance(className, functionName = ''):
        return Logger(className, functionName)
    
    getInstance = staticmethod(getInstance)
    
    def setNameOfFunction(self,nameOfFunction):
        self.nameOfFunction = nameOfFunction
        
    def setLogLevel(logLevel):
        if not isinstance(logLevel,str):
            raise ValueError('Parameter \'logLevel\' must be string.')
        if logLevel.lower() == 'trace':
            Logger.level = 0
        elif logLevel.lower() == 'debug':
            Logger.level = 1
        elif logLevel.lower() == 'info':
            Logger.level = 2
        elif logLevel.lower() == 'warn':
            Logger.level = 3
        elif logLevel.lower() == 'error':
            Logger.level = 4
        elif logLevel.lower() == 'fatal':
            Logger.level = 5
        else:
            raise ValueError('Parameter \'logLevel\' must be: trace, debug, info, warn, error, fatal')
            
    setLogLevel = staticmethod(setLogLevel)
            
    def trace(self,message):
        if self.level == 0:
            self.__printMsg('TRACE', message)
            
    def debug(self,message):
        if self.level <= 1:
            self.__printMsg('DEBUG', message)
    
    def info(self,message):
        if self.level <= 2:
            self.__printMsg('INFO', message)
    
    def warn(self,message):
        if self.level <= 3:
            self.__printMsg('WARN', message)
            
    def error(self,message):
        if self.level <= 4:
            self.__printMsg('ERROR', message)
    
    def fatal(self,message):
        if self.level <= 5:
            self.__printMsg('FATAL', message)
            
    def __printMsg(self,level,message):
        fullLogMessage = '['+level+'] ('+self.nameOfClass
        if self.nameOfFunction != '':
            fullLogMessage =+ '.' + self.nameOfFunction
        fullLogMessage =+ '): ' + message
        print(fullLogMessage)
        