import sys
from pysnmp.hlapi import *
from const import *
from datetime import *

oid_name = '1.3.6.1.2.1.1.5'
oid_uptime = '1.3.6.1.2.1.1.3'

def name(host, oid):
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
                print(varBind[1])


def uptime(host, oid):
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
                x = int(varBind[1])
                d = timedelta(milliseconds=x)  # 4th argument - milliseconds
                print(d)


name('10.11.1.228', oid_name)
uptime('10.11.1.228', oid_uptime)


