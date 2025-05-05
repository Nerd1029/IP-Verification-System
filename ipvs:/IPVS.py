import socket; import os; import sys

hostname1 = socket.gethostname()
sysadminip = socket.gethostbyname(hostname1)

try:
    with open("sysadminip.txt", "r") as f:
        f.read()
    os.system('clear')

except FileNotFoundError:
    with open("sysadminip.txt", "w") as f:
        f.write(sysadminip)

hostname2 = socket.gethostname()
ip = socket.gethostbyname(hostname2)

if ip != sysadminip:
    AccessDenied = print("ACCESS DENIED")
    sys.exit()

elif ip == sysadminip:
    AccessGranted = print("ACCESS GRANTED")