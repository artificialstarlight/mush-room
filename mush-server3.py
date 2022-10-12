import socket
import threading
import random
import os


#spells = [[],[],[]]
key = []
#for i in spells:
for k in range(3):
    key.append(str(random.randint(1,9)))
string_key = ''.join(key)
##str_spells0 = ",".join(spells[0])
##str_spells1 = ",".join(spells[1])
##str_spells2 = ",".join(spells[2])
cmds = ["!Online"]
##str_spells = [str_spells0,str_spells1,str_spells2]
print("The 'secret key' is: ",string_key)
port = 8080
server = socket.gethostbyname(socket.gethostname())
ip = "0.0.0.0"

FORMAT = "utf-8"

clients, usernames = [], []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))

def startChat():

        print("server is working on ",ip," on port ",port)
        server.listen()

        while True:
                conn, addr = server.accept()
                conn.send("NAME".encode(FORMAT))
                name = conn.recv(2048).decode(FORMAT)
                
                usernames.append(name)
                clients.append(conn)

                print(f"Name is :{name}")

                broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))

                conn.send('Connection successful!'.encode(FORMAT))

                thread = threading.Thread(target=handle,
                                        args=(conn, addr))
                thread.start()
                print(f"active connections {threading.activeCount()-1}")

def handle(conn, addr):

        print(f"new connection {addr}")
        connected = True

        while connected:
                message = conn.recv(2048)
                broadcastMessage(message)
                if "!TRY" in message.decode() and string_key in message.decode():
                        broadcastMessage((string_key + " was a Key..").encode())
                        spell_reading()
                if "!TRY" in message.decode() and string_key not in message.decode():
                        attempt = message
                        broadcastMessage(attempt + " was not a correct Key.".encode())
        conn.close()
        
def broadcastMessage(message):
        for client in clients:
                client.send(message)

def spell_reading():
    broadcastMessage((r"""
                      .-'~~~-.
                     .'o  oOOOo`.
                    :~~~-.oOo   o`.
                     `. \ ~-.  oOOo.
                       `.; / ~.  OO:
                       .'  ;-- `.o.'
                      ,'  ; ~~--'~
                      ;  ;
_______\|/__________\\;_\\//___\|/________
""").encode())
    figures = ["Fortuna Major","Fortuna Minor","Populus","Via","Albus","Conjunctio","Puella","Amissio","Puer","Rubeus","Acquisitio","Laetitia","Tristitia","Carcer","Caput Draconis","Cauda Draconis"]
    randfig1 = random.choice(figures)
    randfig2 = random.choice(figures)
    randfig3 = random.choice(figures)
               
    txt = "A fortune-telling: Three geomantic figures, chosen for you: " + randfig1 + ", " + randfig2 + ", "+ randfig3 + "."
    broadcastMessage(txt.encode())
    return

startChat()
