##########################################################################
# Author:               Jane Curry,  jane.curry@skills-1st.co.uk
# Date:                 October 19th, 2012
# Revised:
#
# info.py for snmpExtend ZenPack
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of snmpExtend components.

$Id: info.py,v 1.2 2010/12/14 20:45:46 jc Exp $"""

__version__ = "$Revision: 1.4 $"[11:-2]

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.skills1st.snmpExtend import interfaces


class snmpExtendInfo(ComponentInfo):
    implements(interfaces.IsnmpExtendInfo)

    commandLine = ProxyProperty("commandLine")
    outputLine = ProxyProperty("outputLine")
    nsExtendOutput1Line = ProxyProperty("nsExtendOutput1Line")
    nsExtendOutputFull = ProxyProperty("nsExtendOutputFull")
    nsExtendOutNumLines = ProxyProperty("nsExtendOutNumLines")
    nsExtendResult = ProxyProperty("nsExtendResult")

