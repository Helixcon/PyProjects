import socket
import threading

HOST = "127.0.0.1"  # Change this to the server's IP if connecting to a remote server
PORT = 5000


def receive_message(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            print(message, end="")
        except Exception as e:
            print("Error receiving message:", e)
            break


def send_message(client):
    while True:
        message = input()
        if message == "exit":
            break

        try:
            client.send(message.encode("utf-8"))
        except Exception as e:
            print("Error sending message:", e)
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except Exception as e:
        print("Error connecting to the server:", e)
        return

    receive_thread = threading.Thread(target=receive_message, args=(client,))
    send_thread = threading.Thread(target=send_message, args=(client,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client.close()


if __name__ == "__main__":
    start_client()
