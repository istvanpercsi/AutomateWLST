import sys

from ip.common.common import Common
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger
from ip.common.attributes import Attributes
from ip.wl.wlcommon import WLCommon
from ip.wl.err.common.resourcecouldnotbestartederror import ResourceCouldNotBeStartedError
from ip.wl.res.wlbasicresource import WLBasicResource

Logger.setLogLevel('trace')
#raise ResourceCouldNotBeStartedError('Resource busy')
#WLCommon.connect("weblogic","Weblogic1","t3://localhost:7001")

x = WLBasicResource('test','test2')
print (x.getNameOfResource())
