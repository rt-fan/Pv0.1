import telnetlib
import time

host = ''
login = ''
password = ''
command = 'ping ...'

telnet = telnetlib.Telnet(host)
time.sleep(0.1)
telnet.write(b'\n')
telnet.write(login.encode('ascii') + b'\n')
telnet.write(password.encode('ascii') + b'\n')
telnet.write(command.encode('ascii') + b'\n')
time.sleep(0.2)
telnet.close()
