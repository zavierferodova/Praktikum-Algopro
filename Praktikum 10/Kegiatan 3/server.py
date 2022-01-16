import socket
from inspect import cleandoc
from math import sqrt

HOST = 'localhost'
PORT = 50001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f'Socket listen on {HOST}:{PORT}')
    print('Waiting clients connection ...')

    while True: 
        conn, addr = s.accept() # accept client connection
        print(f'Connected by {addr}')
        command_data = ''

        base_width = 0
        pyramid_height = 0
        triangle_height = 0

        while True:
            bytes_data = conn.recv(1024) # receive data
            command_data = bytes_data.decode()

            if ('set-params' in command_data.lower()):
                params = command_data.lower().split()
                for index, option in enumerate(params):
                    if index > 0:
                        if 's=' in option:
                            input_value = option.strip()[2:]
                            if input_value.isnumeric():
                                base_width = int(input_value)
                        elif 't=' in option:
                            input_value = option.strip()[2:]
                            if input_value.isnumeric():
                                pyramid_height = int(input_value)
                        elif 'h=' in option:
                            input_value = option.strip()[2:]
                            if input_value.isnumeric():
                                triangle_height = int(input_value)
                if base_width > 0 and pyramid_height > 0:
                    triangle_height = sqrt(((base_width/2)**2) + (pyramid_height**2))
                elif base_width > 0 and triangle_height > 0:
                    pyramid_height = sqrt((triangle_height**2) - ((base_width/2)**2))
                conn.send('Completed'.encode())
            elif ('help-params' in command_data.lower()):
                conn.send(cleandoc("""
                    s = Panjang sisi alas piramid
                    t = Tinggi piramid
                    h = Tinggi sisi tegak piramid
                """).encode())
            elif ('show-params' in command_data.lower()):
                conn.send(cleandoc(f"""
                    s = {base_width}
                    t = {pyramid_height}
                    h = {triangle_height}
                """).encode())
            elif ('count' in command_data.lower()):
                area = (base_width**2) + (4 * (0.5 * base_width * triangle_height))
                conn.send(f'{area}'.encode())
            elif command_data.lower() == 'exit':
                conn.close()
                print(f'Connection {addr} closed')
                break
            else:
                conn.send('Unknown command !'.encode())