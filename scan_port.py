import socket
from datetime import datetime

def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        connect = sock.connect(((ip,port)))
        print("Port : ", port, " its open.")
        sock.close()
    except:
        pass

ip = #inset ip
start = datetime.now()
for i in range(1000):
    scan_port(ip,i)

ends = datetime.now()
print("Time: start - ", start, "end - ", ends)
print("Time: {}".format(ends-start))

