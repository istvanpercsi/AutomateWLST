'''
Created on 24.12.2018

@author: Istvan Percsi
'''
from ip.wl.err.wlCommonError import WLCommonError

class ResourceCouldNotBeStopped(WLCommonError):
    '''
    @doc Resource could not be stopped.
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'Resource could not be stopped: ' + msg
        WLCommonError.__init__(self,msg,206)