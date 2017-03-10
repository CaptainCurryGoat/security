import argparse, sys, datetime, time, re
from socket import *

#Create socket object
maxPort=7000
minPort=1

#The following methods give you two options:
#specific_ports scan selected ports
#port_range to scan a range of ports
#These will be called using a dictionary as a menu for the user.


#Specify ports
def specific_ports(host, port):

    try:
        print("")
    except:
        print("")

#Scan a range of ports
def port_range(host, min, max):
    try:
        print("")
    except:
        print("")

#This menu will be displayed to the user.
def display_menu(select):
    scan_menu={'selected': specific_ports(),
           'range':port_range()}

    print("Choose a port scan type\n_____________________\n")
    print("1) Targeted Ports: Specify the ports you want to scan\n 2) Scan a range of ports")

    if select == 1:
        dict['selected']
    elif select == 2:
        dict['range']

def _con_scan(host, port):
    try:

        test_ip=re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host)

        while True:
            if test_ip:
                global sock
                sock = socket(AF_INET, socket.SOCK_STREAM)
                sock = socket.connect(host, port)
                results = sock.recv(1024); #Receive no more than 1024 bytes

                print("TCP Port: ", port, " open")
        else:
            print("\nINVALID FORMAT ERROR: Please enter the ip address in the 0.0.0.0 format: ")

    except:
        print("TCP Port: ", port, "closed")

    finally:
        sock.close()

#After connecting to target, scan target.
def _scan_port(host, port):

    _con_scan(host, port)
    try:
        host_ip = gethostbyname(host) #takes host name, returns host ip
        print("Host: ", host_ip, "\n")
        print("Scan initiated @ ", time.strftime("%H:%M:%S"), "\n")

        startTime=datetime.now()
    except:
        print("ERROR. Unknown host ", host)


def main():
    parser = argparse.ArgumentParser('usage -h <target host> -p <target port>')
    parser.add_argument('-H', dest='tgtPort', required=True, type=str, help='specify target host')
    parser.add_argument('-p', dest='tgtHost', required=True, type=str, help='specify target port[s] separated by commas')

    #Gets the target host and target port
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPorts = str(args.tgtPort).split(',')

   #Loop through the port range
    for port in range(minPort, maxPort):
        try:
            result = _scan_port(tgtHost, tgtPorts)

            if result == 0:
                print("[*] Port %d: Open" % (tgtPorts[port]))

        except:
            pass

    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
    exit(0)
if __name__ == '__main__':
    main()
