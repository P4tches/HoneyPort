import socket,os,ipaddress as ipa
s = socket.socket()
s.bind(('', 23))
s.listen(10)
while 1:
        conn, addr = s.accept()
        print(addr[0])
        if ipa.ip_address(addr[0]) not in ipa.ip_network('192.168.1.0/24'):
                f = open("bips.txt","a")
                f.write(addr[0]+"\n")
                f.close
                os.system(str('iptables -I INPUT -s {} -j DROP').format(addr[0]))
s.close()
