import telnetlib
import time
import ipaddress


host = '10.11.1.228'
login = 'sbnt'
password = 'sbnt@911'

ip2 = host.split('.')
ip3 = ip2[0] + '.' + ip2[1] + '.' + ip2[2] + '.0/24'
ip0 = ip2[0] + '.' + ip2[1] + '.' + ip2[2] + '.0'
subnet1 = ipaddress.ip_network(ip3)

telnet = telnetlib.Telnet(host)
time.sleep(0.1)
telnet.write(b'\n')
telnet.write(login.encode('ascii') + b'\n')
telnet.write(password.encode('ascii') + b'\n')

for ip in subnet1:
    if str(ip) != str(ip0):
        command = 'ping ' + str(ip)
        telnet.write(command.encode('ascii') + b'\n')
        print(ip)
        time.sleep(5)

time.sleep(0.2)
telnet.close()
