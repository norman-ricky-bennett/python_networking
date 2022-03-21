import socket
from multiprocessing.dummy import Pool as ThreadPool

data = input("enter :")
ip = socket.gethostbyname(data)

print(ip)
#create conncection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start = input("starting port : ")
end = input("ending port : ")

userPorts = [ ]
for portNum in range(int(start),int(end)+1):
    userPorts.append(portNum)
  
openPorts = [ ]

def checkPort(portNum):
        status = s.connect_ex((ip,portNum))
        if status == 0:
           openPorts.append(portNum)

pool = ThreadPool(15)

results = pool.map(checkPort, userPorts)

pool.close()
pool.join()
if len(openPorts) == 0:
    print("nothing")
for i in range(len(openPorts)):
    print("PORT %s : OPEN" % (openPorts[i]))