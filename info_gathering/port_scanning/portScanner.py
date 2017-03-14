import argparse, sys, datetime, time, re
from socket import *

def _con_scan(host, port):

    try:
        #global sock
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(host, port)
        sock.send('ViolentPython\r\n')
        results = sock.recv(100); #Receive no more than 1024 bytes
        print("$ TCP Port: " + port + " open")
        print(results)
    except:
        print("$ TCP Port: "  + port + " closed\n")
    finally:
        sock.close()

#After connecting to target, scan target.
def _scan_port(host, ports):
    try:
        host_ip = gethostbyname(host) #takes host name, returns host ip
        print("$ Scan initiated @ " + time.strftime("%H:%M:%S") + "\n_______________________________")
        #d = date.fromordinal(730920)  # 730920th day after 1. 1. 0001

    except:
        print("ERROR. Unknown host " + host_ip)

    try:
        hostname=gethostbyaddr(host_ip)
        print("\n$ Hostname Results: " + hostname)
    except:
        print("\n$ IP Results: " + host_ip)

    for port in ports:
        print("\n$ Scanning Port: " + port)
        _con_scan(host_ip,port)


def main():
    parser = argparse.ArgumentParser('usage -help <target host> -p <target port(s)>')
    parser.add_argument('-H', dest='tgtHost', required=True, type=str, help='specify target host')
    parser.add_argument('-p', dest='tgtPort', required=True, type=str)

    #Gets the target host and target port
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPorts = str(args.tgtPort).split(',')
    _scan_port(tgtHost, tgtPorts)

    if tgtHost is None or tgtPorts[0] is None:
        print(parser.usage)
    exit(0)

if __name__ == '__main__':
    main()
