import os
import re                            # поиск
import sys
from pysnmp.hlapi import *           # библиотека для snmp соединения
# from pingtest import ping            # файл с функцией пинга
from const import *                  # данные для подключения

comm_ip = '10.11.1.228'              # ip-адрес для проверочного запроса
oid_test = '1.3.6.1.2.1.1.1'  # описание коммутатора


# vendor  *************************************************************************************************************

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


# """
# Открываем текстовый файл и построчно передаем строку с ip в функцию pingtest(),
# если пинг проходит, отдаем этот ip в функцию vendor().
# p.s: line() - передает строку с переносом строки(\n), line.strip() - передает строку съедая знак переноса.
# """
# f = open('ip.txt')
# line = f.readline()
# while line:
#     if ping(line.strip()):
#         print('ping ' + line.strip() + ' yes')  # вывод сообщения о том, что пинг есть
#         vendor(line.strip(), oid_test)
#
#     else:
#         print('ping ' + line.strip() + ' no')  # вывод сообщения о том, что пинга нет
#     line = f.readline()
# f.close()

# name  ***************************************************************************************************************

oid_name = '1.3.6.1.2.1.1.5'
oid_uptime = '1.3.6.1.2.1.1.3'


def sys_name(host, oid):
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


# sys_name('10.11.1.228', oid_name)

# interface  **********************************************************************************************************

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


# interface_list(ip_address, oid_des)

# mac-address *********************************************************************************************************

oid_arp_mac = '1.3.6.1.2.1.4.22.1.2'


def arp_mac(host, oid):
    #database = open('database.txt', 'a')
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

                #database.writelines(ip_all + ';' + mac_all + '\n')

                print(ip_all, ' = ', mac_all)
    #database.close()


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


# arp_mac(ip_address, oid_arp_mac)
# print('\nМой мак-адрес =', my_mac(ip_address, oid_arp_mac))

# pingtest ************************************************************************************************************

def ping(ip):
    response = os.system("ping -n 1 -w 100 " + ip)
    if response == 0:
        b = True
    else:
        b = False
    return b

# mysql ***************************************************************************************************************


# автодополнение ip адреса ********************************************************************************************
f = open('ip.txt')
line = f.readline()
file = open('ip2.txt', 'w')
while line:
    line2 = line.strip()
    if '*' in line2:
        a = 0
        while a < 5:
            a += 1
            #with open("ip2.txt", "a") as file:
            file.write(line2.replace('*', str(a)) + '\n')
            # print(line2.replace('*', str(a)))

    elif '-' in line2:
        s_start = '.'.join(line2.split('-')[0].split('.')[:-1])
        s_middle = line2.split('.')[-1].split('-')[0]
        s_end = line2.split('-')[1]
        for i in range(int(s_middle), int(s_end) + 1):
            #with open("ip2.txt", "a") as file:
            file.write('{}.{}'.format(s_start, i) + '\n')
            # print('{}.{}'.format(s_start, i))

    else:
        #with open("ip2.txt", "a") as file:
        file.write(line)
        #print(line.strip())
    line = f.readline()
file.close()
f.close()

# lines = ["first", "second", "third"]
# with open(r"D:\test.txt", "w") as file:
#     for  line in lines:
#         file.write(line + '\n')

# исполнить код *******************************************************************************************************
"""
Открываем текстовый файл и построчно передаем строку с ip в функцию pingtest(),
если пинг проходит, отдаем этот ip в функцию vendor().
p.s: line() - передает строку с переносом строки(\n), line.strip() - передает строку съедая знак переноса.
"""
p = open('ip2.txt')
line22 = p.readline()
while line22:
    if ping(line22.strip()):
        #print('ping ' + line22.strip() + ' yes')  # вывод сообщения о том, что пинг есть
        vendor(line22.strip(), oid_test)
        sys_name(line22.strip(), oid_name)
        #interface_list(line22.strip(), oid_des)
        arp_mac(line22.strip(), oid_arp_mac)
        ip_address = line22.strip()
        print('\nМой мак-адрес =', my_mac(line22.strip(), oid_arp_mac))
    else:
        print('ping ' + line22.strip() + ' no')  # вывод сообщения о том, что пинга нет
    line22 = p.readline()
p.close()
