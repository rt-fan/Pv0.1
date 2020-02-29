import re                            # поиск
import sys
from pysnmp.hlapi import *           # библиотека для snmp соединения
from pingtest import ping            # файл с функцией пинга
from const import *                  # данные для подключения

ip = ''                              # ip-адрес для проверочного запроса
oid_test = '1.3.6.1.2.1.1.1'         # описание коммутатора


def vendor(host, oid):
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
                text = str(varBind)
                if re.search(r'DES', text):
                    print('>>> D-Link DES')
                elif re.search(r'DGS', text):
                    print('>>> D-Link DGS')
                elif re.search(r'Cisco', text):
                    print('>>> Cisco')
                elif re.search(r'SNR', text):
                    print('>>> SNR')
                elif re.search(r'MES', text):
                    print('>>> Eltex')
                elif re.search(r'Huawei', text):
                    print('>>> Huawei')
                else:
                    print('unknown vendor')

                """
                elif re.search(r'\bHuawei\b', text):   ---  \b учитывается знак пробела до и после искомого слова
                    print('>>> Huawei')
                """


"""
Открываем текстовый файл и построчно передаем строку с ip в функцию pingtest(),
если пинг проходит, отдаем этот ip в функцию vendor().
p.s: line() - передает строку с переносом строки(\n), line.strip() - передает строку съедая знак переноса.
"""
f = open('ip.txt')
line = f.readline()
while line:
    if ping(line.strip()):
        print('ping ' + line.strip() + ' yes')  # вывод сообщения о том, что пинг есть
        vendor(line.strip(), oid_test)

    else:
        print('ping ' + line.strip() + ' no')  # вывод сообщения о том, что пинга нет
    line = f.readline()
f.close()
