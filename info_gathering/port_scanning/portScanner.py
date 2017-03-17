import argparse, sys, datetime, time, re, socket
#from socket import *

#global socket

def con_scan(host, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect_ex((host, port))
        sock.send('ViolentPython\r\n')
        results = sock.recv()
        print('$ TCP Port: ' + port + ' open')
        print('$ ' + results)
    except:
        print('$ TCP Port: '  + port + ' closed\n')
    finally:
        sock.close()

#After connecting to target, scan target.
def scan_port(host, ports):
    try:
        host_ip = socket.gethostbyname(host) #takes host name, returns host ip
        print("$ Scan initiated @ " + time.strftime("%H:%M:%S") + "\n_______________________________")

    except:
        print("ERROR. Unknown host " + host_ip)

    try:
        hostname=socket.gethostbyaddr(host_ip)
        print("\n$ Hostname Results: " + hostname)
    except:
        print("\n$ IP Results: " + host_ip)

    for port in ports:
        print("\n$ Scanning Port: " + port)
        con_scan(host,port)


def main():
    parser = argparse.ArgumentParser('usage -help <target host> -p <target port(s)>')
    parser.add_argument('-H', dest='tgtHost', required=True, type=str, help='specify target host')
    parser.add_argument('-p', dest='tgtPort', required=True, type=str)

    #Gets the target host and target port
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPorts = str(args.tgtPort).split(',')
    scan_port(tgtHost, tgtPorts)

    if tgtHost is None or tgtPorts[0] is None:
        print(parser.usage)
    exit(0)

if __name__ == '__main__':
    main()
