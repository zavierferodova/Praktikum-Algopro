import socket

HOST = 'localhost'
PORT = 50001

LIST_COMMANDS = {
    'nim': 'xxxxxxx205',
    'nama': 'Zavier Ferodova Al Fitroh',
    'angkatan': '2021',
    'keluar': 'siap!!'
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
                'Maaf, perintah tidak dimengerti !')
            conn.send(response.encode()) # send response

            if command_data.lower() == 'keluar':
                conn.close()
                print(f'Connection {addr} closed')
                break

