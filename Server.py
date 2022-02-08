from socket import *
import csv ,operator # for reading csv file
import datetime # for displaying the time and date 
# ! NOTE : This Ptoject Was Bulid Using The Last Version Of Python 3.10.0
# function to deal with wrong requests and
def not_found(file):
    print("this is the not_found function")
    content = '<!DOCTYPE html><html><head><title>Error</title> </head><body><h1><span style="color:red;">The file is not found </span></h1><p id=par>Aseel Deek &#8211 1190587 &emsp; Lojain Abdalrazaq &#8211 1190707 &emsp;Mariam Taweel &#8211 1192099<style>p#par{font-weight: bold;}</style></p><p>The IP is &#8594 '+ str(ip)+'</p><p>The Port number is &#8594 '+str(port)+'</p></body></html>'
    connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
    print("HTTP/1.1 200 OK \r\n")
    connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
    print("Content-Type: text/html\r\n")
    connectionSocket.send(bytes("\r\n", "UTF-8"))
    print("\r\n")
    connectionSocket.sendall(bytes(content, "UTF-8"))
    x = datetime.datetime.now()
    print("Date:", x.strftime("%c")) # showing the date&time  

# end of the function 

# function for reading the csv file 
def printTohtml(Alist, htmlfile):   
    html =  "<html>\n<head> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;After Sorting</head>\n<style>p { margin: 0 !important; }</style>\n<body>\n"

    title = "&emsp; No. &emsp;&emsp;&emsp;&emsp; Name &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Price " 
    deco= "------------------------------------------------------------\n"
    
    html += '\n<p>' + title + '</p>\n'+ deco
    
    strat = '<ol>\n'
    html +=strat
    for line in Alist:
        para = '<li>&emsp;' + '&nbsp; | &nbsp; $'.join(line) + '</li>\n'
        html += para
    end ='</ol>' 
    html +=end 
    
    with open(htmlfile, 'w') as f:
        f.write(html + "\n</body>\n</html>")
# end of reading csv file 

# the strart of the project 
serverPort = 6500
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("the server is ready to receive")
while True:
    connectionSocket, address = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode()
    print(address)
    print(sentence)
    ip = address[0] # used in file not found function
    #print("the Ip address", ip)
    port = address[1] # used in file not found function
    #print("the port address", port)
    headers = sentence.split('\n')
    print(headers) # These the headers  ['GET /file.css HTTP/1.1\r', 'Host: localhost:6500\r'.... 
    file = headers[0].split()[1] 
    #print("\n--> the splitter is -->",file)   the pointer that i split the request using it 
    match file:
         case '/' | '/index.html' : # when requesting / or /index.html 
            file = 'main.html'
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))
            x = datetime.datetime.now() # to print the date and time 
            print(x.strftime("%c")) # print the date and time in the terminal 
            
         case '/Network1.jpg' :  # when requesting /Network1.jpg
              fin = open("images/FirstPic.jpg", "rb") # pic path 
              connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
              print("HTTP/1.1 200 OK \r\n")
              connectionSocket.send(bytes("Content-Type: image/jpg\r\n\r\n", "UTF-8"))
              print("Content-Type: image/jpg\r\n\r\n")
              connectionSocket.send(fin.read())
              print(str(fin.read()))
              x = datetime.datetime.now() # to print the date and time 
              print("Date:", x.strftime("%c")) # print the date and time in the terminal 
              
         case '/other.html' : # # when requesting /other.html
            file = 'other.html'
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8")) 
            x = datetime.datetime.now() # to print the date and time 
            print("Date:", x.strftime("%c"))# print the date and time in the terminal     
                   
         case '/Network1.png' : # when requesting /Network1.png
              fin = open("images/SecPic.png", "rb")
              connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
              print("HTTP/1.1 200 OK \r\n")
              connectionSocket.send(bytes("Content-Type: image/png\r\n\r\n", "UTF-8"))
              print("Content-Type: image/png\r\n\r\n")
              connectionSocket.send(fin.read())  # send the contents of the picture
              print(str(fin.read()))  
              x = datetime.datetime.now() # to print the date and time 
              print("Date:", x.strftime("%c")) # print the date and time in the terminal     
         
         case '/file.css' :  # when requesting /file.css
             file = 'style.css'
             fin = open(file)
             content = fin.read()
             fin.close()
             connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
             print("HTTP/1.1 200 OK \r\n")
             connectionSocket.send(bytes("Content-Type: text/css\r\n", "UTF-8"))
             print("Content-Type: text/css\r\n")
             connectionSocket.send(bytes("\r\n", "UTF-8"))
             print("\r\n")
             connectionSocket.sendall(bytes(content, "UTF-8"))
             x = datetime.datetime.now() # to print the date and time 
             print("Date:", x.strftime("%c")) # print the date and time in the terminal 
               
         case '/SortByName': # when requesting /SortByName
            sample = open('Cars.csv','r')
            csv1 = csv.reader(sample, delimiter=',')
            sorted_prices = sorted(csv1,key=operator.itemgetter(0))
            printTohtml(sorted_prices, 'SortedData.html')
            file = 'SortedData.html'
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8")) # should be always html 
            print("Content-Type: text/plain\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8")) 
            x = datetime.datetime.now() # to print the date and time 
            print("Date:", x.strftime("%c")) # print the date and time in the terminal            
             
         case '/SortByPrice': # when requesting /SortByPrice
            sample = open('Cars.csv','r')
            csv1 = csv.reader(sample, delimiter=',')
            sorted_prices = sorted(csv1,key=operator.itemgetter(1))
            printTohtml(sorted_prices, 'SortedData.html')
            file = 'SortedData.html'
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8")) # should be always html 
            print("Content-Type: text/plain\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))
            x = datetime.datetime.now() # to print the date and time 
            print("Date:", x.strftime("%c")) # print the date and time in the terminal 
            
         case'/linked.html':
            file = 'linked.html'
            fin = open(file)
            content = fin.read()
            fin.close()
            connectionSocket.send(bytes("HTTP/1.1 200 OK \r\n", "UTF-8"))
            print("HTTP/1.1 200 OK \r\n")
            connectionSocket.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
            print("Content-Type: text/html\r\n")
            connectionSocket.send(bytes("\r\n", "UTF-8"))
            print("\r\n")
            connectionSocket.sendall(bytes(content, "UTF-8"))     
            
                                       
         case unknown_command: # when requesting Wrong file 
              connectionSocket.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
              print("HTTP/1.1 404 Not Found \r\n")
              not_found(file)
            
    
            