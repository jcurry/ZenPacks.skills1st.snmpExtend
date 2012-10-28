##########################################################################
# Author:               Jane Curry,  jane.curry@skills-1st.co.uk
# Date:                 October 19th, 2012
# Revised:
#
# interfaces.py for snmpExtend ZenPack
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field to the user interface.

$Id: interfaces.py,v 1.2 2010/12/14 20:46:34 jc Exp $"""

__version__ = "$Revision: 1.4 $"[11:-2]

from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IsnmpExtendInfo(IComponentInfo):
    """
Info adapter for snmpExtend component
"""
    commandLine = schema.Text(title=u"Command Name", readonly=True, group='Details')
    outputLine = schema.Text(title=u"Output", readonly=True, group='Details')
    nsExtendOutput1Line = schema.Text(title=u"Output Line 1", readonly=True, group='Details')
    nsExtendOutputFull = schema.Text(title=u"Full Output", readonly=True, group='Details')
    nsExtendOutNumLines = schema.Int(title=u"Num Lines", readonly=True, group='Details')
    nsExtendResult = schema.Int(title=u"Result ", readonly=True, group='Details')

