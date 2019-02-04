'''
Created on 22.01.2019

@author: istva
'''
import re

class WLResourceTypes(object):
    '''
    Static class for resource types
    '''
    SERVER          = 'Server'
    CLUSTER         = 'Cluster'
    DATASOURCE      = 'Datasource'
    APPLICATION     = 'Application'
    LIBRARY         = 'Library'
    
    #this resource 'resource' is only for test of abstract
    RESOURCE        = 'Resource'
    
    
    def getTypeOfResources(typeOfResource):
        return re.sub(r'y$','ie',typeOfResource) + 's'

    getTypeOfResources = staticmethod(getTypeOfResources)
