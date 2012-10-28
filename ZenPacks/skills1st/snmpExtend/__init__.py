
import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())


from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenRelations.RelSchema import *

# Monkey patch the snmpCommand relationship on to the existing OperatingSystem relationships

OperatingSystem._relations += (("snmpCommand", ToManyCont(ToOne, "ZenPacks.skills1st.snmpExtend.snmpExtend", "os")), )

from Products.ZenModel.ZenPack import ZenPackBase
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
class ZenPack(ZenPackBase):
    """ ZenPack loader
"""
    def install(self, app):
        self.dmd.Events.createOrganizer("/Change/Set/Status")
        ZenPackBase.install(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()

    def upgrade(self, app):
        self.dmd.Events.createOrganizer("/Change/Set/Status")
        ZenPackBase.upgrade(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()

    def remove(self, app, junk):
        ZenPackBase.remove(self, app, junk)
        OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in ['snmpCommand']])
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()


