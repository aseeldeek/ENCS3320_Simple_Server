from socket import *
from datetime  import *
Server_name = input("Please Enter the site name:\n")
#made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. 
Client = socket(AF_INET , SOCK_STREAM)
# default port for socket
prot_Server = 80
# connecting to the server
Client.connect((Server_name , prot_Server))
#time before sending request
print (datetime.now())
 # send a HEAD / HTTP/1.1 to the client. encoding to send byte type.
Client.send("HEAD / HTTP/1.1 \r\n".encode())
Client.send("Hostname: {name_Server} \r\n\r\n".encode())
#time response befor the response
time=datetime.now()
modified_sentence = Client.recv(1024)
#time response after the 
time_next=datetime.now()response
finaltime=time_next - time
print("response time:",finaltime)
# receive data from the server 
print("From server :)", modified_sentence.decode())
# Close the connection with the client
Client.close()