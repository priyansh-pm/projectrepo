import socket                   
import re
s = socket.socket()             
host = socket.gethostname()     
port = 60000                    

s.connect((host, port))
s.send("Hello server!")
p = int(raw_input("Enter P:"))
q = int(raw_input("Enter Q:"))
n = p*q
phi = (p-1)*(q-1)
e = 17
d= int((15*phi + 1)/e)
with open('received_file.txt', 'wb') as f:
    print 'file opened'
    s.send(str(n))
    s.send(str(e))
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

f = open('received_file.txt', 'rb')
f2 = open('decoded.txt', 'wb')
code = f.readline()
writeup = ""
setx = re.findall('....?', code)
print setx
for _ in setx:
    res = (int(_)**d)%n
    print (str(res))
    writeup = writeup + str(chr(res))
f2.write(writeup)
f2.close()
f.close
    
