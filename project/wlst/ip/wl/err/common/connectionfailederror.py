'''
Created on 20.12.2018

@author: Istvan Percsi
'''
from ip.wl.err.wlCommonError import WLCommonError

class ConnectionFailedError(WLCommonError):
    '''
    @doc Class of connection errors
    
    @param msg: Error message
    '''
    def __init__(self, msg):
        msg = 'ConnectionFailed: ' + msg
        WLCommonError.__init__(self,msg,1)
