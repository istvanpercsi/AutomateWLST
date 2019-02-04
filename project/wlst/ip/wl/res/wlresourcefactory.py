'''
Created on 27.01.2019

@author: istva
'''
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger

class WLResourceFactory(ExtendedObject):
    '''
    classdocs
    '''

    def createResources(resources):
        logger = Logger('WLResourceFactory')
        logger.debug('Resources: ' + str(resources))
        logger.debug('Resoruces type: ' + str(type(resources)))
        logger.debug(resources.resources.res01.name)
        for k,resource in resources.iterEOItems():
            logger.debug('Key: ' + str(k))
            logger.debug('Type: ' + str(type(resource)))
    
    createResources = staticmethod(createResources)
            
            
            