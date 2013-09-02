import socket
import sys
from sets import Set
old_server_address = ('localhost', 9998) # eski server
new_server_address = ('localhost', 9999) # yeni server

def main():
    f  = open("input")
    wOld  = open("outputEski","w") #eski server
    wNew  = open("output","w") #yeni server
    lines = f.readlines()
    f.close()
    print len(lines)
    ipler = Set()
    connectionsOld = {}
    connectionsNew = {}
    try:
        for line in lines:
            data = line.split(":")
            ip = data[3].strip()[1:len(data[3].strip())-1]
            ipler.add(ip)
            request = data[4].strip()
            #Eski servera request
            if not connectionsOld.has_key(ip):
                sockOld = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connectionsOld[ip] = sockOld
                connectionsOld[ip].connect(old_server_address)
                print "connectionCount is: " + str(len(connectionsOld))
            connectionsOld[ip].sendall(request)
            dataOld = connectionsOld[ip].recv(200)
            wOld.write(request + " : " + dataOld)
            #yeni servera request
            if not connectionsNew.has_key(ip):
                sockNew = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connectionsNew[ip] = sockNew
                connectionsNew[ip].connect(new_server_address)
                print "connectionCount is: " + str(len(connectionsNew))
            connectionsNew[ip].sendall(request)
            dataNew = connectionsNew[ip].recv(150)
            wNew.write(request + " : " + dataNew)
    except Exception, e:
        print e
    finally:
        print "bitti"


main()


# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock9 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect the socket to the port where the server is listening
# server_address = ('localhost', 9999)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
# sock.connect(server_address)
# sock2.connect(server_address)
# sock3.connect(server_address)
# sock4.connect(server_address)
# sock5.connect(server_address)
# sock6.connect(server_address)
# sock7.connect(server_address)
# sock8.connect(server_address)
# sock9.connect(server_address)
# sock0.connect(server_address)
# sock11.connect(server_address)

# try:
    
#     # Send data
#     message = 'k,123123123,ID64'
#     print >>sys.stderr, 'sending "%s"' % message
#     sock.sendall(message)

#     # Look for the response
#     amount_received = 0
#     amount_expected = 3
    
#     while amount_received < amount_expected:
#         data = sock.recv(2)
#         amount_received += len(data)
#         print >>sys.stderr, 'received "%s"' % data

# finally:
#     print >>sys.stderr, 'closing socket'
#     sock.close()
