
from ip.logger.logger import Logger
from ip.common.attributes import Attributes
from ip.wl.res.wlresourcefactory import WLResourceFactory

Logger.setLogLevel('trace')
attr = Attributes()
attr.readAttributesFromFile("config.properties")
WLResourceFactory.createResources(attr)