import socket


my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))

request = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

my_sock.send(request)

while True:
    receive = my_sock.recv(512)
    if len(receive) < 1:
        break
    print(receive.decode())

my_sock.close()