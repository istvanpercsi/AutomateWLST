'''
Created on 19.10.2018

@author: Istvan Percsi
@contact: istvanpercsi@gmail.com
@license: MIT
'''

import sys

class Logger(object):
    '''
    This is a Standard logger class. It logs messages on console based on errorlevel (0-5) and enabled name of class/function.
    Default error logLevel is: ERROR (4)
    Default class is: *
    Default function is: *
    '''
       
    logLevel = 4
    logClassFunction = ['*.*']
    
    def __init__(self,nameOfInvokerClass):
        self.__nameOfClass = nameOfInvokerClass
        self.__nameOfFunction = ''
        
    def getInstance():
        return Logger(sys._getframe().f_back.f_locals['self'].__class__.__name__)
    
    getInstance = staticmethod(getInstance)
        
    def appendClassFunction(self,cf = '*.*'):
        if not cf in Logger.logClassFunction:
            self.logClassFunction.append(cf)

    def removeClassFunction(self,cf):
        self.logClassFunction.remove(cf)
        
    def clearClassFunction(self):
        self.logClassFunction = []
    
    def getClassFunction(self):
        return self.logClassFunction
        
    def setLogLevel(logLevel):
        if not isinstance(logLevel,str):
            raise ValueError('Parameter \'logLevel\' must be string.')
        if logLevel.lower() == 'trace':
            Logger.logLevel = 0
        elif logLevel.lower() == 'debug':
            Logger.logLevel = 1
        elif logLevel.lower() == 'info':
            Logger.logLevel = 2
        elif logLevel.lower() == 'warn':
            Logger.logLevel = 3
        elif logLevel.lower() == 'error':
            Logger.logLevel = 4
        elif logLevel.lower() == 'fatal':
            Logger.logLevel = 5
        else:
            raise ValueError('Parameter \'logLevel\' must be: trace, debug, info, warn, error, fatal')
            
    setLogLevel = staticmethod(setLogLevel)
            
    def trace(self,message):
        self.__nameOfFunction = sys._getframe().f_back.f_code.co_name
        if self.logLevel == 0:
            self.__printMsg('TRACE', message)
            
    def debug(self,message):
        self.__nameOfFunction = sys._getframe().f_back.f_code.co_name
        if self.logLevel <= 1:
            self.__printMsg('DEBUG', message)
    
    def info(self,message):
        self.__nameOfFunction = sys._getframe().f_back.f_code.co_name
        if self.logLevel <= 2:
            self.__printMsg('INFO', message)
    
    def warn(self,message):
        self.__nameOfFunction = sys._getframe().f_back.f_code.co_name
        if self.logLevel <= 3:
            self.__printMsg('WARN', message)
            
    def error(self,message):
        self.__nameOfFunction = sys._getframe().f_back.f_code.co_name
        if self.logLevel <= 4:
            self.__printMsg('ERROR', message)
    
    def fatal(self,message):
        self.__nameOfFunction = sys._getframe().f_back.f_code.co_name
        if self.logLevel <= 5:
            self.__printMsg('FATAL', message)
            
    def __printMsg(self,level,message):
        cf = self.__nameOfClass + '.' + self.__nameOfFunction
        if [x for x in Logger.logClassFunction if x in [cf, '*.*', self.__nameOfClass + '.*']]:
            fullLogMessage = '['+level+'] ('+self.__nameOfClass
            if self.__nameOfFunction != '':
                fullLogMessage += '.' + self.__nameOfFunction
            fullLogMessage += '): ' + message
            print(fullLogMessage)
        