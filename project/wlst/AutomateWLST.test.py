import sys

from ip.common.common import Common
from ip.common.extendedobject import ExtendedObject

x = ExtendedObject()















#Conditionally import wlstModule only when script is executed with jython
'''
if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport

print 'starting the script ....'
username = 'weblogic'
password = 'welcome1'
url='t3://localhost:7001'

connect(username,password,url)


edit()
startEdit()




try:
    save()
    activate(block="true")
    print "script returns SUCCESS"   
except Exception, e:
    print e 
    print "Error while trying to save and/or activate!!!"
    dumpStack()
    raise 
    
'''