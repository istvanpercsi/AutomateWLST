'''
Created on 27.01.2019

@author: Istvan Percsi
'''
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger
from ip.wl.res.wlresourcetypes import WLResourceTypes

class WLResourceFactory(ExtendedObject):
    '''
    WLResourceFactory - this class will create resources from Attribute object.
    '''

    def createResources(resources,typeOfResource = None):
        logger = Logger('WLResourceFactory')
        for resKey,resValue in resources.iterEOItems():
            if typeOfResource == None or str(resKey).lower() == str(WLResourceTypes.getTypeOfResources(typeOfResource)).lower():
                if str(resKey).lower() == str(WLResourceTypes.getTypeOfResources(WLResourceTypes.CLUSTER)).lower():
                    logger.debug('Create resource: ' + WLResourceTypes.CLUSTER)
                elif str(resKey).lower() == str(WLResourceTypes.getTypeOfResources(WLResourceTypes.SERVER)).lower():
                    logger.debug('Create resource: ' + WLResourceTypes.SERVER)
                elif str(resKey).lower() == str(WLResourceTypes.getTypeOfResources(WLResourceTypes.DATASOURCE)).lower():
                    logger.debug('Create resource: ' + WLResourceTypes.DATASOURCE)
                # ONLY for TEST BEGIN
                elif str(resKey).lower() == str(WLResourceTypes.getTypeOfResources(WLResourceTypes.RESOURCE)).lower():
                    logger.debug('Create resource: ' + WLResourceTypes.RESOURCE)
                # ONLY for TEST END    
                else:
                    logger.debug('Key: ' + str(resKey))
                    logger.debug('Type: ' + str(type(resValue)))

    createResources = staticmethod(createResources)

            
            
            