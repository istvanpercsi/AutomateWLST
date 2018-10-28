import sys

from ip.common.common import Common
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger


Logger.setLogLevel('trace')

d = dict()
d['x.y'] = 'z'
x = ExtendedObject(d)
print(x.x.y)
x.k = 'f'
print(x.k)
x.x = 'z'
print(x.x)

d = {'s':{'t':'V'}}
x = ExtendedObject(d)
print(x.s.t)
x.s.update(ExtendedObject({'z':{'k':'o','t':'tt'}}))
print(x.s.z.k)

print(x.s.z.t) 
print(x.s.t)

x.s.update(ExtendedObject({'z':{'k':'i'}}))
print(x.s.z.k)

print(x.s.z.t) 
print(x.s.t)













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