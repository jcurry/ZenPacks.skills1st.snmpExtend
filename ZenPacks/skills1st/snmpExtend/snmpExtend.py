from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.OSComponent import OSComponent
from Globals import InitializeClass

class snmpExtend(OSComponent, ManagedEntity):

    """
    snmpExtend object
    """

    meta_type = portal_type = "snmpExtend"

    # The NET-SNMP-EXTEND-MIB can either report multiple command lines when the output is multi-line
    # eg. 
    #     NET-SNMP-EXTEND-MIB::nsExtendOutLine."system_model_tag".1 = STRING: PowerEdge R610
    #     NET-SNMP-EXTEND-MIB::nsExtendOutLine."system_model_tag".2 = STRING: CWV2R4J 
    # This is from the nsExtendOutput2 table.
    #
    # Alternatively the nsExtendOutput1 table can be queried which delivers 4 attributes for
    # each command, where nsExtendOutputFull may be a very long entry embracing multiple output lines
    # This option delivers one set of attributes for each command.
    #
    commandLine = ""
    # outputLine comes from nsExtendOutput2 entry - multiple output lines result in multiple command lines
    outputLine = ""
    # next 4 values comes from nsExtendOutput1 entry - 1 set of attributes per command
    nsExtendOutput1Line = ""
    nsExtendOutputFull = ""
    nsExtendOutNumLines = 0
    nsExtendResult = 0

    _properties = OSComponent._properties + (
        {'id': 'commandLine', 'type': 'string', 'mode': ''},
        {'id': 'outputLine', 'type': 'string', 'mode': ''},
        {'id': 'nsExtendOutput1Line', 'type': 'string', 'mode': ''},
        {'id': 'nsExtendOutputFull', 'type': 'string', 'mode': ''},
        {'id': 'nsExtendOutNumLines', 'type': 'int', 'mode': ''},
        {'id': 'nsExtendResult', 'type': 'int', 'mode': ''},
    )

    # The snmpCommand relationship does not exist in the default Products.ZenModel.OperatingSystem
    # It is monkey-patched in the __init__.py of this zenpack

    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont,
            'Products.ZenModel.OperatingSystem', 'snmpCommand')),
    )

InitializeClass(snmpExtend)



