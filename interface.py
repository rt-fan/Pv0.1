# -*- coding: utf-8 -*-
import re
import sys
from pysnmp.hlapi import *
from const import *
import mysql.connector
from mysql.connector import errorcode  # для работы с mysql неоходимо поставить mysql.connector для python3

oid_ind = '1.3.6.1.2.1.2.2.1.1'
oid_des = '1.3.6.1.2.1.2.2.1.2'
oid_stat = '1.3.6.1.2.1.2.2.1.8'
oid_speed = '1.3.6.1.2.1.2.2.1.5'
oid_upt = '1.3.6.1.2.1.2.2.1.9'
oid_inErr = '1.3.6.1.2.1.2.2.1.14'
oid_outErr = '1.3.6.1.2.1.2.2.1.20'


def interface_list(host, oid):
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
                index = varBind[0][-1]
                descr = str(varBind[-1])

                # номер порта (интерфейса) по индексу (10001 => 1 порт)
                if index == 10001:
                    port = '1'
                elif index == 10002:
                    port = '2'
                elif index == 10003:
                    port = '3'
                elif index == 10004:
                    port = '4'
                elif index == 10005:
                    port = '5'
                elif index == 10006:
                    port = '6'
                elif index == 10007:
                    port = '7'
                elif index == 10008:
                    port = '8'
                elif index == 10009:
                    port = '9'
                elif index == 10010:
                    port = '10'
                elif index == 10011:
                    port = '11'
                elif index == 10012:
                    port = '12'
                elif index == 10013:
                    port = '13'
                elif index == 10014:
                    port = '14'
                elif index == 10015:
                    port = '15'
                elif index == 10016:
                    port = '16'
                elif index == 10017:
                    port = '17'
                elif index == 10018:
                    port = '18'
                elif index == 10019:
                    port = '19'
                elif index == 10020:
                    port = '20'
                elif index == 10021:
                    port = '21'
                elif index == 10022:
                    port = '22'
                elif index == 10023:
                    port = '23'
                elif index == 10024:
                    port = '24'
                elif index == 10025:
                    port = '25'
                elif index == 10026:
                    port = '26'
                elif index == 10027:
                    port = '27'
                elif index == 10028:
                    port = '28'
                elif index == 10029:
                    port = '29'
                elif index == 10030:
                    port = '30'
                elif index == 10031:
                    port = '31'
                elif index == 10032:
                    port = '32'
                elif index == 10033:
                    port = '33'
                elif index == 10034:
                    port = '34'
                elif index == 10035:
                    port = '35'
                elif index == 10036:
                    port = '36'
                elif index == 10037:
                    port = '37'
                elif index == 10038:
                    port = '38'
                elif index == 10039:
                    port = '39'
                elif index == 10040:
                    port = '40'
                elif index == 10041:
                    port = '41'
                elif index == 10042:
                    port = '42'
                elif index == 10043:
                    port = '43'
                elif index == 10044:
                    port = '44'
                elif index == 10045:
                    port = '45'
                elif index == 10046:
                    port = '46'
                elif index == 10047:
                    port = '47'
                elif index == 10048:
                    port = '48'
                elif index == 10101:
                    port = '49'
                elif index == 10102:
                    port = '50'
                elif index == 10103:
                    port = '51'
                elif index == 10104:
                    port = '52'
                else:
                    port = 'unknown'

                if re.search(r'Ethernet', descr):
                    print(port, descr)


interface_list(ip_address, oid_des)

