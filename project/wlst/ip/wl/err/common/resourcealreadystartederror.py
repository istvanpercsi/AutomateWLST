'''
Created on 21.12.2018

@author: istva
'''
from ip.wl.err.wlCommonError import WLCommonError

class ResourceAlreadyStartedError(WLCommonError):
    '''
    @doc Attribute has an invalid value
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'Resource already started: ' + msg
        WLCommonError.__init__(self,msg,203)