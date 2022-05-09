import socket
import re
import RPi.GPIO as GPIO
import time

localIP     = "127.0.0.1"
localPort   = 3333
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

Relay = [5, 6, 13, 16, 19, 20, 21, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(0,8):
    GPIO.setup(Relay[i], GPIO.OUT)
    GPIO.output(Relay[i], GPIO.HIGH)

print("GPIO setup and ready")

# Listen for incoming datagrams

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = format(message)

    gate = re.findall('[0-9]+', clientMsg)
    gateNdx = int(gate[0])
    print(gateNdx)
    GPIO.output(Relay[gateNdx], GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(Relay[gateNdx], GPIO.HIGH)
    
    clientIP  = "Client IP Address:{}".format(address)
    
