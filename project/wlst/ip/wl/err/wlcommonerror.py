'''
Created on 20.12.2018

@author: Istvan Percsi
'''
from ip.wl.err.wlbasicerror import WLBasicError


class WLCommonError(WLBasicError):
    '''
    Base class of common errors. 
    '''
    def __init__(self, msg, errCode):
        '''
        Consturctor
        '''
        WLBasicError.__init__(self,msg,errCode)
        self.updateClassOfErrCode(1,999,1000)