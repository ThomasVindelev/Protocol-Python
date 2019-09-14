import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

server_address = (IPAddr, 10000)


synReq = 'com-0: %s' % IPAddr
ack = 'com-0: accept'

try:
    # Send data
    print('Sending your message')
    sent = sock.sendto(synReq.encode(), server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
    print(data)
    inputData = 'com-0: accept %s' % IPAddr
    if data == inputData.encode():
        print('Sending accept')
        sock.sendto(ack.encode(), server_address)
        Request = input()
        while Request != 'Disconnect':
            sock.sendto(Request.encode(), server_address)
            data, address = sock.recvfrom(4096)
            print(data)
            Request = input()

finally:
    print('closing socket')
