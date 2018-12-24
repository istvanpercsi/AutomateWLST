'''
Created on 21.12.2018

@author: istva
'''
from ip.wl.err.wlCommonError import WLCommonError

class AttributeHasAnInvalidValueError(WLCommonError):
    '''
    @doc Attribute has an invalid value
    
    @param msg: Error message
    
    '''
    def __init__(self, msg):
        msg = 'Attribute has an invalid value: ' + msg
        WLCommonError.__init__(self,msg,102)
