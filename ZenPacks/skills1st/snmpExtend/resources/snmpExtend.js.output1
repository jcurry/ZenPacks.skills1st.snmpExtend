(function(){

var ZC = Ext.ns('Zenoss.component');


function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.snmpExtendPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'snmpExtend',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'commandLine'},
                {name: 'nsExtendOutput1Line'},
                {name: 'nsExtendOutputFull'},
                {name: 'nsExtendOutNumLines'},
                {name: 'nsExtendResult'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 50
            },{
                id: 'commandLine',
                dataIndex: 'commandLine',
                header: _t('Command'),
                width: 200,
                sortable: true,
            },{
                id: 'nsExtendOutNumLines',
                dataIndex: 'nsExtendOutNumLines',
                header: _t('Num Lines'),
                width: 60,
                sortable: true,
            },{
                id: 'nsExtendResult',
                dataIndex: 'nsExtendResult',
                header: _t('Result'),
                renderer: function(pS) {
                        if (pS==0) {
                          return Zenoss.render.pingStatus('up');
                        } else {
                          return Zenoss.render.pingStatus('down');
                        }
                },

                width: 60,
                sortable: true,
            },{
                id: 'nsExtendOutputFull',
                dataIndex: 'nsExtendOutputFull',
                header: _t('Output'),
                width: 500,
                sortable: true,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 60,
                sortable: true
            }]
        });
        ZC.snmpExtendPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('snmpExtendPanel', ZC.snmpExtendPanel);
ZC.registerName('snmpExtend', _t('SNMP Command'), _t('SNMP Commands'));

})();
