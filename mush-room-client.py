# Python program to implement client side of chat room. 
import socket 
import select 
import sys
import threading
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("mush.png")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP_address = "3.145.82.81" #server IP goes here
Port = 8080

server.connect((IP_address, Port))
print("welcome to the mush-room")
username = str(input("enter your name, or alias, whatever: "))
server.send(username.encode())

def handle_messages():
    while True:
        msg = server.recv(2048).decode()
        print(msg)

def input_handler():
    while True:
        server.send((username+":"+input("> ")).encode())

message_handler = threading.Thread(target=handle_messages,args=())
message_handler.start()

input_handler = threading.Thread(target=input_handler,args=())
input_handler.start()
