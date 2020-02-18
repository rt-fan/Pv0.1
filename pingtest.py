import os

def pingtest(ip):
    response = os.system("ping -n 1 -w 20 " + ip)
    if response == 0:
        b = True
    else:
        b = False
    return b
