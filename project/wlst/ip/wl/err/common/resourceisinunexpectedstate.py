'''
Created on 24.12.2018

@author: istva
'''
from ip.wl.err.wlCommonError import WLCommonError

class ResourceIsInUnexpectedState(WLCommonError):
    '''
    @doc Resource is in unexpected state.
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'Resource is in unexpected state: ' + msg
        WLCommonError.__init__(self,msg,208)