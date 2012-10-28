=================================
ZenPacks.skills1st.snmpExtend
=================================


Description
===========

A ZenPack that works with the NET-SNMP-EXTEND-MIB which runs operating system commands when queried.
The snmpd.conf must be configured on a target device to specify commands to be run and snmpd recycled.

The MIB provides two different output tables.  nsExtendOutput1 provides:
    * nsExtendOutput1Line
    * nsExtendOutputFull
    * nsExtendOutNumLines
    * nsExtendResult

for each command.  This type of output works well when commands typically return a single line
of output.  For commands delivering multi-line output nsExtendOutputFull delivers all the lines
concatenated together.  If you use the nsExtendOutput1 form then the multi-line output can be
viewed sensibly using the Details option from the Display menu when viewing a command component.

For environments where commands typically produce multi-line output, the nsExtendOutput2 table
delivers command / output pairs where each command line has an instance qualifier.  Please see
the screenshots for further enlightenment.

The ZenPack code includes code to cater for either format.  The only elements that need to
be modified are under the resources directory and the modeler/plugins directory:
    * resources/snmpExtend.js.output1          )  one of these should be copied to snmpExtend.js
    * resources/snmpExtend.js.output1          )
    * modeler/plugins/snmpCommandMap.py.output1    )  one of these should be copied to snmpCommandMap.py
    * modeler/plugins/snmpCommandMap.py.output2    )

Components
==========

The ZenPack has the following relevant files:
    * __init__.py adds an snmpCommand relationship to the standard code for OperatingSystem relations.  It also ensures that relations are rebuilt when this ZenPack is installed / removed.
    * snmpExtend.py defines the new component type and defines the relation with the standard os object.


Requirements & Dependencies
===========================

    * Zenoss Versions Supported: 3.x and 4.2
    * External Dependencies: The net-snmp agent must be installed and configured on target systems, including extend stanzas.  For example:
        * extend testcmd_bad_exit /usr/local/zenoss/zenoss/local/testcmd.sh
        * Note that an snmp agent must be recycled if an extend command is added / changed
    * ZenPack Dependencies: None
    * Installation Notes: A full zenoss stop / zenoss start should be executed when the ZenPack is first installed and a browser refresh performed.
    * Configuration:  The modeler plugin snmpCommandMap is introduced by the ZenPack.  It should be configured for relevant devices and the devices remodeled.  For example, to model a single device with the new modeler use:
        * zenmodeler run -v 10 -d zenoss.class.example.org --collect snmpCommandMap
        * Refresh the browser window

Download
========
Download the appropriate package for your Zenoss version from the list
below.

* Zenoss 3.0+ `Latest Package for Python 2.6`_
* Zenoss 4.0+ `Latest Package for Python 2.7`_

Installation
============

Normal Installation (packaged egg)
----------------------------------
Copy the downloaded .egg to your Zenoss server and run the following commands as the zenoss
user::

   zenpack --install <package.egg>
   zenoss stop
   zenoss start

Developer Installation (link mode)
----------------------------------
If you wish to further develop and possibly contribute back to this 
ZenPack you should clone the git repository, then install the ZenPack in
developer mode::

   zenpack --link --install <package>
   zenoss stop
   zenoss start

Configuration
=============

Tested with Zenoss 3.2 and Zenoss 4.2

Change History
==============
* 1.0.0
   * Initial Release

Screenshots
===========
|snmp_extend_output1|
SNMP Command component with single commands with multi-line output

|snmp_extend_output2|
SNMP Command component with multiple command lines each with a single line of output


.. External References Below. Nothing Below This Line Should Be Rendered


.. _Latest Package for Python 2.6: https://github.com/downloads/jcurry/ZenPacks.skills1st.snmpExtend/ZenPacks.skills1st.snmpExtend-1.0.0-py2.6.egg
.. _Latest Package for Python 2.7: https://github.com/downloads/jcurry/ZenPacks.skills1st.snmpExtend/ZenPacks.skills1st.snmpExtend-1.0.0-py2.7.egg


.. |snmp_extend_output1| image:: http://github.com/jcurry/ZenPacks.skills1st.snmpExtend/raw/master/screenshots/snmp_extend_output1_screenshot.jpg
.. |snmp_extend_output2| image:: http://github.com/jcurry/ZenPacks.skills1st.snmpExtend/raw/master/screenshots/snmp_extend_output2_screenshot.jpg

                                                                        

