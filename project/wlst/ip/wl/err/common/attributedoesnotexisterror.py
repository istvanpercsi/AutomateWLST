'''
Created on 21.12.2018

@author: istva
'''
from ip.wl.err.wlCommonError import WLCommonError

class AttributeDoesNotExistError(WLCommonError):
    '''
    @doc Attribute does not exists error
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'Attribute does not exist: ' + msg
        WLCommonError.__init__(self,msg,101)
