import socket
import math
import errno
import sys
from multiprocessing import Process

def ProcessStart(server):

     while True:
            ch = server.recv(1024).decode()

            if ch == '1':
                #To caculate log 
                numb, b = [float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
                calc = math.log(float(numb),float(b))

            elif ch  == '2':
                #To calculate square root
                numb = server.recv(1024).decode()
                calc = math.sqrt(float(numb))

            elif ch  == '3':
                #To calculate exponential 
                numb = server.recv(1024).decode()
                calc = math.exp(float(numb))

            elif ch == '4':
                #To calculate Power Of a number 
                numb, p = [float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
                calc = math.pow(numb,p)
            elif ch == '9':
                server.close()
                break

            server.sendall(str(calc).encode())


if __name__ == '__main__':
    
    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 5050

    try:
        S.bind((host,port))
    except socket.error as e:
        print (str(e))
        sys.exit()

    S.listen(5)
    while True:
        try:
            server, addr = S.accept()
            print ('\n Sucessfully Connected to client! Continue at client <3 ')
        
            p = Process(target = ProcessStart, args=(server,))
            p.start()

        except socket.error:
            print ('an error has occurred!')

    S.close()
