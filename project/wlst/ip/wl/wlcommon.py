'''
Created on 20.12.2018

@author: istva
'''
import wlstModule as wlst
from wlstModule import WLSTException as WLSTException

from ip.logger.logger import Logger
from ip.wl.err.common.connectionfailederror import ConnectionFailedError

class WLCommon(object):
    
    def connect(username, password, url):
        logger = Logger("[static] WLCommon")
        logger.debug('Username: ' + username)
        logger.debug('Password: ' + '*****')
        logger.debug('URL: ' + url)
        if not username or not password or not url:
            raise ValueError('Parameters are mandatory. Please check.')
        try:
            wlst.connect(username, password, url)
        except WLSTException, e:
            raise ConnectionFailedError('Connection to server has been failed. Please check parameters and availability of AdminServer. Nested exception: ' + str(e))
        
    connect = staticmethod(connect)
    