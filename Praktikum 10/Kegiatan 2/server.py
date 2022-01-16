import socket
import platform

HOST = 'localhost'
PORT = 50001

LIST_COMMANDS = {
    'machine': platform.machine(),
    'release': platform.release(),
    'system': platform.system(),
    'version': platform.version(),
    'node': platform.node(),
    'quit': ''
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f'Socket listen on {HOST}:{PORT}')
    print('Waiting clients connection ...')

    while True: 
        conn, addr = s.accept() # accept client connection
        print(f'Connected by {addr}')
        command_data = ''

        while True:
            bytes_data = conn.recv(1024) # receive data
            command_data = bytes_data.decode()

            response = LIST_COMMANDS.get(command_data.lower(), 
                'Unknown command !')
            conn.send(response.encode()) # send response

            if command_data.lower() == 'quit':
                conn.close()
                print(f'Connection {addr} closed')
                break