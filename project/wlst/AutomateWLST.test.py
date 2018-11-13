import sys

from ip.common.common import Common
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger
from ip.common.properties import Properties


Logger.setLogLevel('trace')

p = Properties()
p.readPropertiesFromFile(sys.argv[1])