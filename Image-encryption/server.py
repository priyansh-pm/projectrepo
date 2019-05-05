import socket                   
import re
port = 60000                    
s = socket.socket()            
host = socket.gethostname()    
s.bind((host, port))            
s.listen(5)                     
code = 0
flag = 0
code2 = ""
print 'Server listening....'

while True:
    conn, addr = s.accept()    
    print 'Got connection from', addr
    data = conn.recv(1024)
    n = int(conn.recv(1024))
    e = int(conn.recv(1024))
    
    print('Server received', repr(data))
    
    f2='testfile.txt'
    f3='encodedfile.txt'
    fn = open(f2,'rb')
    fn3 = open(f3, 'w')
    l2 = fn.read(1024)
    for _ in l2:
        
        for ch in _:
            print "\n--\n"
            code = code + (ord(ch)*(1000**flag))
            flag += 1
            print str(code)        
    #rsa encryption
    setx = re.findall('...?', str(code))
    print setx
    for _ in setx:
        enc = (int(_)**e)%n
        print str(enc)
        if enc <1000:
            code2 = "0" + str(enc) + code2
        else:
            code2 = str(enc) + code2
        
    print(code2)
    fn3.write(code2)
    #fn3.write(str(code))
    fn3.close()
    fn.close()
    print 'here'
    filename='encodedfile.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    
    while (l):
        conn.send(l)
        print('Sent ',repr(l))
        l = f.read(1024)
    f.close()

    print('Done sending')
    
    conn.close()
