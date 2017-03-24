import argparse, sys, datetime, time, re, socket
#from socket import *

#global socket

def con_scan(host, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect_ex((host, port))
        sock.send('ViolentPython\r\n')
        results = sock.recv(100)
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
        return

    try:
        hostname=socket.gethostbyaddr(host_ip)
        print("\n$ Hostname Results: " + hostname)
    except:
        print("\n$ IP Results: " + host_ip)


    for port in ports:
        print("\n$ Scanning Port: " + port)
        con_scan(host,port)


def main():
    try:
        parser = argparse.ArgumentParser('usage -help <target host> -p <target port(s)>')
        parser.add_argument('-H', dest='tgtHost', required=True, type=str, help='specify target host')
        parser.add_argument('-p', dest='tgtPort', required=True, type=str)

        #Gets the target host and target port
        global tgtHost, tgtPorts
        args = parser.parse_args()
        tgtHost = args.tgtHost
        tgtPorts = str(args.tgtPort).split(',')

        while True:
            #global ip
            #tgtHost = input("Enter IP Address: ")
            """if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", tgtHost): #Validates correct format.
                octet = tgtHost.split(".")  # Split each octet by the period.
                if 1<= int(octet[0]) <= 223 and int(octet[0]) != 127:
                    if int(octet[0]) != 169 or int(octet[0]) != 254:
                        if 0 <= int(octet[1]) <= 255 and 0 <= int(octet[2]) <= 255 and 0 <= int(octet[3]) <= 255:
                            print("SUCCESS!\n")
                            break
                        else:
                            print("The remaining octets must be between 0 and 255")
                    else:
                        print("First octet cannot be 169 or 254.")
                else:
                    print("First octet must be between 1 and 223 and cannot equal 127.")
            else:
                print("INVALID FORMAT ERROR. Please enter IP Address in correct format." )
                tgtHost = input("Enter IP Address: ")"""

        scan_port(tgtHost, tgtPorts)
    except:
        if tgtHost is None or tgtPorts[0] is None:
            print(parser.usage)
        exit(0)

if __name__ == '__main__':
    main()
