import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Bind the socket to the port
server_address = (IPAddr, 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

SynAck = False
res = -1

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    inputData = 'com-0: %s' % IPAddr

    if data == inputData.encode():
        reply = 'com-0: accept %s' % IPAddr
        sent = sock.sendto(reply.encode(), address)
        print('sent {} bytes back to {}'.format(sent, address))
        data, address = sock.recvfrom(4096)
        print()
        if data == 'com-0: accept'.encode():
            print(data)
            SynAck = True
    else:
        reply = 'SynAck Denied'
        sent = sock.sendto(reply.encode(), address)
        print('sent {} bytes back to {}'.format(sent, address))
        SynAck = False

    while SynAck:
        print('Waiting for input...')
        data, address = sock.recvfrom(4096)
        res += 1
        message = 'msg-%s %s' % (res, data)
        res += 1
        response = 'res-%s - I am server' % res
        print(message)
        sock.sendto(response.encode(), address)
