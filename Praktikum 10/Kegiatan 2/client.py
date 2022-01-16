import socket

HOST = 'localhost'
PORT = 50001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f'Connecting with {HOST}:{PORT} ...')
    s.connect((HOST, PORT))
    print('Connected ! \n')

    while True:
        command = input('> ')
        s.send(bytes(command.encode())) # send command

        bytes_data = s.recv(1024) # receive server response
        str_data = bytes_data.decode()
        print(str_data)

        if (command.lower() == 'quit'):
            s.close()
            exit(0)