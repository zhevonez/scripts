import os
import random
import subprocess
import sys

def get_current_mac(interface):
    result = subprocess.run(['getmac', '/v', '/fo', 'list'], capture_output=True, text=True)
    lines = result.stdout.split('\n')
    for line in lines:
        if "Physical Address" in line and interface in line: #PA poshalkoooooooooooo ya dayn
            return line.split(': ')[1].strip() 
    return None # except esli ne naideno 

def generate_random_mac():  # буду писать на русском теперь крч генерируется рандомный мак адрес, а не определенный (берется из ретурна, его можно переделать если надо чтото еще)
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),     
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def change_mac(interface, new_mac):
    if sys.platform != "win32":
        raise EnvironmentError("This script only works on Windows")

    cmd = f'netsh interface set interface "{interface}" admin=disable'
    os.system(cmd)
    cmd = f'netsh interface set interface "{interface}" admin=enable'  # просто проверка предыдущего 
    os.system(cmd) 
    cmd = f'reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001 /v NetworkAddress /d {new_mac} /f'   #собственно замена
    os.system(cmd)
    print(f"MAC address changed to {new_mac}")

# usage karoche
interface = input("Enter the name of the network interface: ")     # 10l
current_mac = get_current_mac(interface)
print(f"Current MAC Address: {current_mac}")

new_mac = generate_random_mac()
print(f"New MAC Address: {new_mac}")

change_mac(interface, new_mac)

# // made by zhevonez //
