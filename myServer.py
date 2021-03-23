import threading
import socket
import sys

#Host and port declaration (uses localhost)
host = '127.0.0.1'
port = 8080

#Creates socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Server binding
server.bind((host, port))
server.listen()

#Handles the client messeges
def clientHandler(client, address):
    #Constanlty checks for incoming messages
    while True:
        #Brodcasts message to client
        try:
            message = client.recv(1024).decode('ascii')
            #Checks for client request to disconect
            if message == '#exit':
                #Sends disconect confirmation to client
                client.send(f"You have been disconecded".encode('ascii'))
                client.close()
                #Prints disconected message on server
                print(f"Client({address}) has chosen to disconect")
                break
            #Runs the normal message reciver
            else:
                #Prints client message confirmation on server
                print(f"recived '{message}' from Client({address})")
                #Sends message confirmation to client
                client.send(f"SERVER : '{message}' recived by server".encode('ascii'))
        #Closes connection on error
        except:
            client.close()
            print(f"Client({address}) has disconected // ERROR occured!")
            break
    #Closes thread
    else:
        sys.exit()

#Runs the server (accepts new connections and creates a thread for client handler function)
def runServer():
    #Prints confirmation message
    print("The server is running")

    #port = input("Give port : ")

    while True:
        #Acnoleges and accepts client connection
        client, address = server.accept()
        print(f"Connection achived with Client({str(address)})")

        #Gives client the connection confirmation
        client.send('You have been connected to the server'.encode('ascii'))

        #Creates a thread to handle the connected client
        thread = threading.Thread(target = clientHandler, args = (client, address))
        thread.start()

#Call to the runServer main method
runServer()