'''
Created on 24.12.2018

@author: istva
'''
from ip.wl.err.wlCommonError import WLCommonError

class ResourceIsInInvalidState(WLCommonError):
    '''
    @doc Resource is in invalid state. Start/Stop etc.
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'Resource is in invalid state: ' + msg
        WLCommonError.__init__(self,msg,207)