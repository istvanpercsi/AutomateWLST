'''
Created on 20.12.2018

@author: Istvan Percsi
'''

class WLBasicError(Exception):
    '''
    Basic Error exception for Weblogic lib.
    @author: Istvan Percsi
    @version: 1.0
    '''

    def __init__(self, msg, errCode):
        '''
        Constructor
        '''
        self.msg = msg
        self.errCode = errCode

    def __str__(self):
        '''
        ToString function
        '''
        return repr('(' + str(self.errCode) + ') ' + self.msg)

    def updateClassOfErrCode(self,minValue,maxValue,shift):
        '''
        Shift error code to the right error class
        '''
        if (self.errCode <= maxValue and self.errCode >= minValue):
            self.errCode = self.errCode + shift
        else:
            raise OverflowError('Error code is out of range')
        