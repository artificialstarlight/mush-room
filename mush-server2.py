import time, socket, sys
import threading
import random
import os

spells = [[],[],[],[]]
for i in spells:
    for k in range(3):
        i.append(str(random.randint(0,99)))

str_spells0 = ",".join(spells[0])
str_spells1 = ",".join(spells[1])
str_spells2 = ",".join(spells[2])
cmds = ["!Online"]
str_spells = [str_spells0,str_spells1,str_spells2]


    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = "0.0.0.0"
    
#IP_address = "0.0.0.0" #server IP goes here 
port = 8080
 
server.bind((ip, port))
print("Binding successful!")
server.listen(35) 
clients = []
username_lookup = {}
def gobrrr():   
    while True:
        conn, addr = server.accept()
        print("Received connection from ", addr[0])
        print('Connection Established. Connected From: ',addr[0])
        username = conn.recv(512).decode()
        print('New connection. Username: '+str(username))
        broadcast('New person joined the room. Username: '+username)
        num_online = len(clients)
        broadcast("There are " + str(num_online) + " users online")
        clients.append(conn)
        username_lookup[conn] = username
        threading.Thread(target=handle_client,args=(conn,addr,)).start()

def broadcast(message):
     for connection in clients:
            connection.send(message.encode())
  
def handle_client(conn,addr):
    while True:
        try:
            msg = conn.recv(1024)

            if msg.decode() != '':
                print('New message: '+str(msg.decode()))
                for connection in clients:
                    if connection != conn:
                        connection.send(msg)
                    
            if "!TRY" in msg.decode() and msg.decode() in str_spells:
                broadcast(str_spells0 + " was a Key..")
                spell_reading()
            if "!TRY" in msg.decode() and msg.decode() not in cmds:
                attempt = msg.decode()
                broadcast(attempt + " was not a correct Key.")
            
        except:
            conn.shutdown(socket.SHUT_RDWR)
            clients.remove(conn)
            
            print(str(username_lookup[conn])+' left the room.')
            broadcast(str(username_lookup[conn])+' has left the room.')

            break

        """if msg.decode() != '':
            print('New message: '+str(msg.decode()))
            for connection in clients:
                if connection != conn:
                    connection.send(msg)"""

def spell_reading():
    broadcast(r"""
                      .-'~~~-.
                     .'o  oOOOo`.
                    :~~~-.oOo   o`.
                     `. \ ~-.  oOOo.
                       `.; / ~.  OO:
                       .'  ;-- `.o.'
                      ,'  ; ~~--'~
                      ;  ;
_______\|/__________\\;_\\//___\|/________
""")
    figures = ["Fortuna Major","Fortuna Minor","Populus","Via","Albus","Conjunctio","Puella","Amissio","Puer","Rubeus","Acquisitio","Laetitia","Tristitia","Carcer","Caput Draconis","Cauda Draconis"]
    randfig1 = random.choice(figures)
    randfig2 = random.choice(figures)
    randfig3 = random.choice(figures)
               
    txt = "Three figures, chosen for you: " + randfig1 + ", " + randfig2 + ", "+ randfig3 + "."
    broadcast(txt)
    return

print("Starting...")
gobrrr()
