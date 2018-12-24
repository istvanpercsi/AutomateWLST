'''
Created on 21.12.2018

@author: Istvan Percsi
'''
from ip.wl.err.wlCommonError import WLCommonError

class ResourceCouldNotBeStartedError(WLCommonError):
    '''
    @doc Attribute has an invalid value
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'Resource could not be started: ' + msg
        WLCommonError.__init__(self,msg,204)