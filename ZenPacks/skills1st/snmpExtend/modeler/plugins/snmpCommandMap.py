"""
snmpCommandMap SNMP plugin
"""
# SnmpPlugin is the base class that provides lots of help in modeling data
# that's available over SNMP.
from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetMap, GetTableMap

# Classes we'll need for returning proper results from our modeler plugin's
# process method.
from Products.DataCollector.plugins.DataMaps import ObjectMap

def decToAscii(decName):
    """ Convert list of decimal numbers to ASCII string"""
    ascList = []
    for i in decName:
        ascList.append(chr(int(i)))
    return ''.join(ascList)

class snmpCommandMap(SnmpPlugin):
    """Map SNMP Commands table to device """
    modname = "ZenPacks.skills1st.snmpExtend.snmpExtend"
    relname = "snmpCommand" 
    # It is a component of the os component of a device that we want to populate
    compname = "os"

    # If you don't want to use the nsExtendOutput2Entry (1 command per output line) then
    #  it will be much more efficient to comment out references to nsExtendOutput2Entry and commandTable
    # Similarly, if you only want the nsExtendOutput2Entry output, comment out references
    #  to nsExtendOutput1Entry and output1Table

    snmpGetTableMaps = (
        GetTableMap('nsExtendOutput2Entry', '.1.3.6.1.4.1.8072.1.3.2.4.1', {
            '.2': 'outputLine',
            }),
        GetTableMap('nsExtendOutput1Entry', '.1.3.6.1.4.1.8072.1.3.2.3.1', {
            '.1': 'nsExtendOutput1Line',
            '.2': 'nsExtendOutputFull',
            '.3': 'nsExtendOutNumLines',
            '.4': 'nsExtendResult',
            }),
        )


    def process(self, device, results, log):
        """Collect SNMP information for this device"""
        log.info("Modeler %s processing data for device %s", self.name(), device.id)
        getdata, tabledata = results

        commandTable = tabledata.get('nsExtendOutput2Entry')
        # If no data then simply return
        if not commandTable:
            log.warn('No SNMP response from %s for the %s plugin', device.id, self.name())
            log.warn(  "Data = %s", tabledata )
            return

        output1Table = tabledata.get('nsExtendOutput1Entry')
        # If no data then simply return
        if not output1Table:
            log.warn('No SNMP response from %s for the %s plugin', device.id, self.name())
            log.warn(  "Data = %s", tabledata )
            return

        rm = self.relMap()
        #for oid, data in commandTable.items():
        for oid, data in output1Table.items():
            try:
                om = self.objectMap(data)
                # Command Line is the OID after .1.3.6.1.4.1.8072.1.3.2.4.1.2 converted to ASCII
                cmdOid = oid.split('.')
                cmdLen = int(cmdOid[0]) + 1
                cmd = decToAscii(cmdOid[1:cmdLen])
                # last element of OID is the instance - .1, .2, .3 etc
                # Only needed if use Output2Entry
                # cmdInst = cmdOid[-1]
                #om.commandLine = cmd + '.' + cmdInst
                om.commandLine = cmd
                om.snmpindex = oid.strip('.')
                om.id = self.prepId( om.commandLine.replace('.','_') )
                # log.info(' om.id is %s, om.snmpindex is %s, om.commandLine is %s, om.outputLine is %s ' % (om.id, om.snmpindex, om.commandLine, om.outputLine ))
                log.info(' om.id is %s, om.snmpindex is %s, om.commandLine is %s ' % (om.id, om.snmpindex, om.commandLine ))
                rm.append(om)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in %s modeler plugin %s' % ( self.name(), errorInfo))
                continue
        return rm

