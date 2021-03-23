import threading
import socket
import sys

#Creating socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting client to myServer
client.connect(('127.0.0.1', 8080))

#Recives messages from server
def reciveMessage():
    #Constanlty checks for incoming messages
    while True:
        #Recives message from server
        try:
            message = client.recv(1024).decode('ascii')
            #Checks for disconected confirmation
            if message == "You have been disconecded":
                print(message)
                client.close()
                break
            #Prints normal server message
            else:
                print(message)
        #Handles error
        except:
            print("Connecion failed // ERROR occured!")
            client.close()
            break
    #Closes thread
    else:
        sys.exit()

#Sends message to server
def sendMessage():
    #Constanlty checks for input
    while True:
        message = input(">> ")
        #Sends the message to the server
        client.send(message.encode('ascii'))
        #Breaks loop if exit message has been sent
        if message == "#exit":
            break
    #Closes thread
    else:
        sys.exit()

#prints exit instructions
print("\n-- To close the connection type '#exit' --\n")

#Creates thread for reciveing method 
threadRecive = threading.Thread(target = reciveMessage)
threadRecive.start()

#Creates thread for sending method 
threadSend = threading.Thread(target = sendMessage)
threadSend.start()