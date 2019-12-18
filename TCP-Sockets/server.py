#!usr/bin/python3 
import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host can be directly specified to the id address but the fn. here 
#automates and make the code intelligent
host = socket.gethostbyname()
port = 998

#binding to socket
serversocket.bind((host,port)) #host will be replaced with IP,

#starting the TCP listener
serversocket.listen(3)

while True:
    #starting the conncection
    clientsocket,address = serversocket.accept()
    
    print('Connection recieved from: ' % str(address))
    
    message = 'You have successfully connected to the server!' + '\r\n'
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()