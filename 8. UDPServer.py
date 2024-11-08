import socket


def receive_file(filename, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("192.168.10.1", port))

    with open(filename, 'wb') as file:
        print(f"Listening on port {port}...")
        while True:
            data, client_addr = server_socket.recvfrom(1024)
            if data == b"FileSent":
                print(f"Received confirmation for {filename}")
            elif not data:
                break
            else:
                file.write(data)

    server_socket.close()
    print(f"File received and saved as {filename}")


if __name__ == '__main__':
    server_ip = "192.168.10.1"  # Replace with ip
    server_port = 12345  # Replace with the desired port number
    receive_file("received_script.py", server_port)
