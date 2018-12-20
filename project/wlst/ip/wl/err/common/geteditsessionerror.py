'''
Created on 20.12.2018

@author: Istvan Percsi
'''
from ip.wl.err.wlCommonError import WLCommonError

class GetEditSessionError(WLCommonError):
    '''
    @doc Class of errors of editsession
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'GetEditSessionFailed: ' + msg
        WLCommonError.__init__(self,msg,2)