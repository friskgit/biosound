import socket
import re

localIP     = "127.0.0.1"
localPort   = 3333
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = format(message)

    gate = re.findall('[0-9]+', clientMsg)
    print(gate[0])

    clientIP  = "Client IP Address:{}".format(address)
    
