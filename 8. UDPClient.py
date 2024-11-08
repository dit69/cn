import socket


def send_file(filename, server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with open(filename, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.sendto(data, (server_ip, server_port))
            data = file.read(1024)

    client_socket.sendto(b"FileSent", (server_ip, server_port))  # Send a confirmation message
    client_socket.close()
    print(f"File {filename} sent to {server_ip}:{server_port}")


if __name__ == '__main__':
    server_ip = "192.168.10.1"  # replace with ip
    server_port = 12345  # Replace with the same port number used on the server
    send_file("script.py", server_ip, server_port)
    send_file("text.txt", server_ip, server_port)
    send_file("audio.mp3", server_ip, server_port)
    send_file("video.mp4", server_ip, server_port)
