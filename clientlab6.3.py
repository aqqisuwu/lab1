import socket
import sys

Client = socket.socket()
host = '192.168.56.104'
port = 5050

try:
    Client.connect((host,port))
    print (' Successfull Connect! ')
except socket.error as e:
    print ( str(e) )

loop = True

while loop:
    print ('\n Hi! lets calculate! Choose what you want to do below')
    print (' 1. Do Logarithmic expression ')
    print (' 2. Do Square Root ')
    print (' 3. Do Exponential expression ')
    print (' 4. Do Power Of ')
    print (' 5. Exit Calculator ')
    
    ans = input ('\n Enter number : ' )
    Client.send(ans.encode())

    if ans == '1':
        #log
        print ('\n [+] Log Function ')
        numb = input('\n Enter Number : ')
        b = input('\n Enter base : ')
        Client.sendall(str.encode('\n'.join([str(numb), str(b)])))
        tot = Client.recv(1024)
        print ( 'The answer for log ' + numb + ' base ' + b + ' : ' + str(tot.decode()))

    elif ans == '2':
        #Suare Root
        root = True
        while root:
            print ('\n [+] Square Root Function ')
            numb = input ('\n Enter Number : ')
            if float(numb) <  0:
                print('\n Error!  Negative Number Cannot Be A Square Root')
            else:
                root = False
                Client.send(numb.encode())
                tot = Client.recv(1024)

        print ( 'The  answer for sqrt ' + numb +' : ' + str(tot.decode()))


    elif ans == '3':
        #exponen
        print ('\n [+] Exponential Function ')
        numb = input ('\n Enter Number : ')
        Client.send(numb.encode())
        tot = Client.recv(1024)

        print ( ' The answer for exponential ' + numb + ' : ' + str(tot.decode()))

    elif ans == '4':
        #Power Of
        print ('\n [+] Power Of Number ')
        numb = input('\n Enter Number : ')
        p = input('\n Enter Power Of Number : ')
        Client.sendall(str.encode('\n'.join([str(numb), str(p)])))
        tot = Client.recv(1024)
        print ( 'The  answer for ' + numb + ' power of ' + p + ' : ' + str(tot.decode()))

    elif ans == '5':
        #exit
        Client.close()
        sys.exit()
    else:
        print ('\nError!  Invalid input please enter again ')

    input ( '\n To Continue, press enter ')
