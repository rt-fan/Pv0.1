# -*- coding: utf-8 -*-
import sys
from pysnmp.hlapi import *
from const import *

oid_arp_mac = '1.3.6.1.2.1.4.22.1.2'


def arp_mac(host, oid):
    database = open('database.txt', 'a')
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData(community),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lexicographicMode=False):
        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'),
                  file=sys.stderr)
            break

        else:
            for varBind in varBinds:
                # собираем по индексам портов из varBind части мак-адреса в десятичном представл (4.191.109.13.203.235)
                aa_10 = varBind[-1][-6]
                bb_10 = varBind[-1][-5]
                cc_10 = varBind[-1][-4]
                dd_10 = varBind[-1][-3]
                ee_10 = varBind[-1][-2]
                ff_10 = varBind[-1][-1]

                # переводим дясятичные части в 16-тиричные (04:bf:6d:0d:cb:eb)
                aa = format(aa_10, '02x')
                bb = format(bb_10, '02x')
                cc = format(cc_10, '02x')
                dd = format(dd_10, '02x')
                ee = format(ee_10, '02x')
                ff = format(ff_10, '02x')

                # собираем по индексам ip-адреса для каждого мак-адреса
                ip_1 = varBind[0][-4]
                ip_2 = varBind[0][-3]
                ip_3 = varBind[0][-2]
                ip_4 = varBind[0][-1]

                ip_all = '{0}.{1}.{2}.{3}'.format(ip_1, ip_2, ip_3, ip_4)
                mac_all = '{0}:{1}:{2}:{3}:{4}:{5}'.format(aa, bb, cc, dd, ee, ff)

                database.writelines(ip_all + ';' + mac_all + '\n')

                print(ip_all, ' = ', mac_all)
    database.close()




def my_mac(host, oid):
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData(community),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lexicographicMode=False):
        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'),
                  file=sys.stderr)
            break

        else:
            for varBind in varBinds:
                # собираем по индексам портов из varBind части мак-адреса в десятичном представл (4.191.109.13.203.235)
                aa_10 = varBind[-1][-6]
                bb_10 = varBind[-1][-5]
                cc_10 = varBind[-1][-4]
                dd_10 = varBind[-1][-3]
                ee_10 = varBind[-1][-2]
                ff_10 = varBind[-1][-1]

                # переводим дясятичные части в 16-тиричные (04:bf:6d:0d:cb:eb)
                aa = format(aa_10, '02x')
                bb = format(bb_10, '02x')
                cc = format(cc_10, '02x')
                dd = format(dd_10, '02x')
                ee = format(ee_10, '02x')
                ff = format(ff_10, '02x')

                # собираем по индексам ip-адреса для каждого мак-адреса
                ip_1 = varBind[0][-4]
                ip_2 = varBind[0][-3]
                ip_3 = varBind[0][-2]
                ip_4 = varBind[0][-1]

                ip_all = '{0}.{1}.{2}.{3}'.format(ip_1, ip_2, ip_3, ip_4)
                mac_all = '{0}:{1}:{2}:{3}:{4}:{5}'.format(aa, bb, cc, dd, ee, ff)

                if ip_all == ip_address:
                    return mac_all


arp_mac(ip_address, oid_arp_mac)
print('\nМой мак-адрес =', my_mac(ip_address, oid_arp_mac))
