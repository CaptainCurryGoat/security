import parser, sys, datetime, time
from socket import *

#Create socket object
maxPort=7000
minPort=1

def _con_target_(host, port):
    try:
        sock = socket(AF_INET, socket.SOCK_STREAM)
        sock = socket.connect(host, port)
        results = sock.recv(1024); #Receive no more than 1024 bytes

        print("TCP Port: ", port, " open")

    except:
        print("TCP Port: ", port, "closed")

    finally:
        sock.close()

#After connecting to target, scan target.
def _scan_target(host, port):
    try:
        host_ip = gethostbyname(host) #takes host name, returns host ip
        print("Host: ", host_ip, "\n")
        print("Scan initiated @ ", time.strftime("%H:%M:%S"), "\n")

        startTime=datetime.now()
    except:
        print("ERROR. Unknown host ", host)


def main():