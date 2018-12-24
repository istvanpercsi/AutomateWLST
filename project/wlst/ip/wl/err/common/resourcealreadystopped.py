'''
Created on 24.12.2018

@author: istva
'''
from ip.wl.err.wlCommonError import WLCommonError

class ResourceAlreadyStopped(WLCommonError):
    '''
    @doc Attribute has an invalid value
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'Resource already stopped: ' + msg
        WLCommonError.__init__(self,msg,205)