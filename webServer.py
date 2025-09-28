# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    # Prepare a server socket
    serverSocket.bind(("", port))
    
    # Fill in start
    serverSocket.listen(1)  # server should listen for incoming connections
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()   # Fill in start - accepting connections   # Fill in end
        
        try:
            message = connectionSocket.recv(1024).decode()   # Fill in start - receive client message   # Fill in end 
            filename = message.split()[1]
            
            # opens the client requested file. 
            f = open(filename[1:], "rb")     # fill in start              # fill in end   
            
            # This variable stores headers for a valid request (200 OK)    
            # Fill in start 
            header = "HTTP/1.1 200 OK\r\n"
            header += "Server: MyFirstPythonServer\r\n"
            header += "Content-Type: text/html; charset=UTF-8\r\n"
            header += "Connection: close\r\n\r\n"
            header = header.encode()
            # Fill in end
                   
            outputdata = f.read()  # read file content as bytes
            f.close()
            
            # Send the complete response
            # Fill in start
            connectionSocket.send(header + outputdata)
            # Fill in end
            
            connectionSocket.close()  # closing the connection socket
        
        except Exception as e:
            # Send response message for invalid request (404)
            # Fill in start
            header = "HTTP/1.1 404 Not Found\r\n"
            header += "Server: MyFirstPythonServer\r\n"
            header += "Content-Type: text/html; charset=UTF-8\r\n"
            header += "Connection: close\r\n\r\n"
            body = "<html><body><h1>404 Not Found</h1></body></html>"
            connectionSocket.send(header.encode() + body.encode())
            # Fill in end

            # Close client socket
            # Fill in start
            connectionSocket.close()
            # Fill in end

    # Do NOT uncomment these lines for Gradescope
    # serverSocket.close()
    # sys.exit()


if __name__ == "__main__":
    webServer(13331)
