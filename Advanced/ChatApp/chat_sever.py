import socket
import threading

HOST = "127.0.0.1"  # Use "0.0.0.0" to allow connections from any network
PORT = 5000

clients = []


def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print("Error broadcasting message:", e)
                remove_client(client)


def remove_client(client):
    if client in clients:
        clients.remove(client)
        client.close()


def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message:
                broadcast(f"{message}\n", client)
            else:
                remove_client(client)
                break
        except Exception as e:
            print("Error handling client:", e)
            remove_client(client)
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Server is listening on {}:{}".format(HOST, PORT))

    while True:
        client_socket, client_address = server.accept()
        print("New connection from:", client_address)
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    start_server()
