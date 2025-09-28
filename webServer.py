#Import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)   # listen for incoming connections...
  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = connectionSocket, addr = serverSocket.accept()   #Fill in start -are you accepting connections? (Yes)   #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode()   #Fill in start -a client is sending you a message   #Fill in end 
      filename = message.split()[1] 
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "rb")     #fill in start              #fill in end   
      
      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      header = "HTTP/1.1 200 OK\r\n"
      header += "Content-Type: text/html; charset=UTF-8\r\n\r\n"
      header = header.encode()
      #Fill in end
               
      outputdata = f.read()  # read file content as bytes
      f.close()
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!
      # Fill in start
      connectionSocket.send(header + outputdata)
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      header = "HTTP/1.1 404 Not Found\r\n"
      header += "Content-Type: text/html; charset=UTF-8\r\n\r\n"
      body = "<html><body><h1>404 Not Found</h1></body></html>"
      connectionSocket.send(header.encode() + body.encode())
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  #serverSocket.close()
  #sys.exit()

if __name__ == "__main__":
  webServer(13331)