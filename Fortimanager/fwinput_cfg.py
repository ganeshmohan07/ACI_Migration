vlan_list =[{
    "device_name": "FortiGate-VM01v",
    "adom": "FGT_6_2",
    "scope": "vdom/root",
    "vdom_name": "root",
    "l3out_int_name": "WEB",
    "vlan_id": "101",
    "aci_l3out_nexthop": "172.16.1.1",
    "l3out_ipadd": "172.16.1.2/30",
    "gw_network" : "192.168.1.0",
    "gw_mask" : "255.255.255.0",
    "l3out_phy_interface":"port3",
    "current_phy_interface":"port2",
    "current_vlan_interface":"WEB",
    "l3out_rm_name":"DSS_RM_L3out",

    },
    {
    "device_name": "FortiGate-VM01v",
    "adom": "FGT_6_2",
    "scope": "vdom/root",
    "vdom_name": "root",
    "l3out_int_name": "APP",
    "vlan_id": "102",
    "aci_l3out_nexthop": "172.16.1.5",
    "l3out_ipadd": "172.16.1.6/30",
    "gw_network" : "192.168.2.0",
    "gw_mask" : "255.255.255.0",
    "l3out_phy_interface":"port3",
    "current_phy_interface":"port2",
    "current_vlan_interface":"APP",
    "l3out_rm_name":"DSS_RM_L3out",
    }]