import socket
import ssl


def send(byte_str):
    client_socket_ssl.sendall(byte_str)
    recv = client_socket_ssl.recv(1024)
    print(recv.decode())
    return recv


mail_server = 'smtp.mail.ru'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket_ssl = ssl.wrap_socket(client_socket)
client_socket_ssl.connect((mail_server, 465))

recv = client_socket_ssl.recv(1024)

send(b'EHLO Test\n')

send(b'AUTH LOGIN\n')

send(b'login\n')

send(b'password\n')

send(b'mail from: titovstepan@mail.ru\n')

send(b'rcpt to: {mail_to}\n')
send(b'rcpt to: {mail_to}}\n')

send(b'data\n')
with open('letter.eml') as letter:
    send(bytes(f'{letter.read()}\n.\n'.encode('utf-8')))
