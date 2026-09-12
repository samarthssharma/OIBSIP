import socket
import threading
from datetime import datetime
import sys

# Get username before connecting
username = input("Enter your username: ")

# Setup the connection to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('127.0.0.1', 5555))
except:
    print("Error: Could not connect to the server. Make sure server.py is running first!")
    sys.exit()

# Listen for incoming messages
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            # If server asks for username, send it
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred. Disconnected from server.")
            client.close()
            break

# Send typed messages
def write_messages():
    while True:
        text = input("")
        
        if text.lower() == 'quit':
            client.close()
            break
            
        # Format the message with a timestamp
        now = datetime.now()
        timestamp = now.strftime("%H:%M")
        message = f"[{timestamp}] {username}: {text}"
        
        client.send(message.encode('utf-8'))

# Start two threads: one to read messages, one to type messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()