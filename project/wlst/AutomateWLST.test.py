import sys

from ip.common.common import Common
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger
from ip.common.attributes import Attributes
from ip.wl.err.common.activationfailederror import ActivationFailedError
from ip.wl.err.common.connectionfailederror import ConnectionFailedError
from ip.wl.wlcommon import WLCommon

Logger.setLogLevel('trace')

WLCommon.connect("weblogic","Weblogic1","t3://localhost:7001")