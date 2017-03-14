import argparse, sys, datetime, time, re
from socket import *

#Create socket object
global maxPort, minPort
maxPort=7000
minPort=1


def _con_scan(host, port):
    print("BUT I CAN'T SEE YOU!!")
    try:
        #global sock
        sock = socket(AF_INET, socket.SOCK_STREAM)
        sock = socket.connect(host, port)
        results = sock.recv(1024); #Receive no more than 1024 bytes

        print("TCP Port: ", port, " open")
        print(str(results))

    except:
        print("TCP Port: ", port, "closed")

    finally:
        sock.close()

#After connecting to target, scan target.
def _scan_port(host, port):
    print("IDK IF THAT'S YOU!!!!")
    _con_scan(host, port)
    try:
        host_ip = gethostbyname(host) #takes host name, returns host ip
        print("Host: ", host_ip, "\n")
        print("Scan initiated @ ", time.strftime("%H:%M:%S"), "\n")

        startTime=datetime.now()
    except:
        print("ERROR. Unknown host ", host)


def main():
    print("CAN YOU SEE ME???")
    parser = argparse.ArgumentParser('usage -h <target host> -p <target port>')
    parser.add_argument('-H', dest='tgtPort', required=True, type=str, help='specify target host')
    parser.add_argument('-p', dest='tgtHost', required=True, type=str, help='specify target port[s] separated by commas')

    #Gets the target host and target port
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPorts = str(args.tgtPort).split(',')
    _scan_port(tgtHost, tgtPorts)


    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
    exit(0)
if __name__ == '__main__':
    main()
