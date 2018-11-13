import sys

from ip.common.common import Common
from ip.common.extendedobject import ExtendedObject
from ip.logger.logger import Logger
from ip.common.properties import Attributes


Logger.setLogLevel('trace')

p = Attributes()
p.readAttributesFromFile(sys.argv[1])
print(p.parameter2)
print(p.param1.param11)