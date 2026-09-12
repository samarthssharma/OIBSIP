import socket
import threading
from datetime import datetime

print("Starting the Chat Server...")

# Setup the server on localhost
HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

# Send a message to all connected clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            pass

# Handle messages from a single client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # If a client disconnects, gracefully remove them and notify others
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                
                username = usernames[index]
                usernames.remove(username)
                
                # Create timestamp
                now = datetime.now()
                timestamp = now.strftime("%H:%M")
                
                disconnect_msg = f"[{timestamp}] {username} has left the chat.".encode('utf-8')
                broadcast(disconnect_msg)
                print(f"{username} disconnected.")
            break

# Accept new connections
def receive_connections():
    print("Server is listening on localhost...")
    while True:
        client, address = server.accept()
        
        # Ask the new client for their username
        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        
        usernames.append(username)
        clients.append(client)
        
        # Create timestamp and notify everyone
        now = datetime.now()
        timestamp = now.strftime("%H:%M")
        join_msg = f"[{timestamp}] {username} has joined the chat!".encode('utf-8')
        broadcast(join_msg)
        
        # Start a thread to listen to this specific client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()