'''
Created on 20.12.2018

@author: istva
'''
from ip.wl.err.wlCommonError import WLCommonError


class ActivationFailedError(WLCommonError):
    '''
        @doc Class of activation errors
        @param msg: Error message
    '''
    def __init__(self, msg):
        msg = 'ActivationFailed: ' + msg
        WLCommonError.__init__(self,msg,3)