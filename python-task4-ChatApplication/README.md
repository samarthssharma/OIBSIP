# Real-Time Chat Application

A command-line, real-time messaging application built using Python. This project utilizes a client-server architecture to enable bidirectional communication between multiple users across a network.

## Features

* **Server-Client Architecture:** Utilizes Python's `socket` library to establish reliable TCP connections.
* **Concurrent Connections:** Implements `threading` to handle multiple clients simultaneously without blocking the main execution.
* **Real-Time Messaging:** Allows users to send and receive messages instantly.
* **Timestamp Integration:** Automatically prefixes all incoming and outgoing messages with a timestamp (e.g., [14:35]).
* **Graceful Disconnections:** Detects when a user leaves the chat and automatically broadcasts a departure notification to all remaining clients.

## Tech Stack

* Python 3
* `socket` module
* `threading` module
* `datetime` module

## How to Run (Localhost)

This application requires running multiple terminal instances.

1. **Start the Server:** Open a terminal in the project directory and run the server script first.
   ```bash
   python server.py