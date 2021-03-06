#!/usr/bin/env python

import socket
BUFFER_SIZE = 1024
HOST = ""
PORT =  8001

def get_remote_ip(host):
    remote_ip = socket.gethostbyname( host )
    return remote_ip

def main():
    host = 'www.google.com'
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)
        while True: 
            conn, addr = proxy_start.accept()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip,port))
                send_full_data = conn.recv(BUFFER_SIZE)
                proxy_end.sendall(send_full_data)
                proxy_end.shutdown(socket.SHUT_WR)

                data = proxy_end.recv(BUFFER_SIZE)
                conn.send(data)
            conn.close()


if __name__ == '__main__':
    main()
