#This is a Client side Code to connect to a Server which is listening on a specific port

# Import socket module
import socket

url = "127.0.0.1"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Object successfully Created and Initialized")
except socket.error as err:
    print("Socket Creation/Initialization failed with error {}" .format(err))

# default port for socket
port = 8000

try:
    host_ip = socket.gethostbyname(url)
    print("IP Address for {} is:\t{}".format(url, host_ip))
except socket.gaierror:
    # this means could not resolve the host
    print("There was an error resolving the Host")
    sys.exit()

# connecting to the server
s.connect((host_ip,port))
s.send(b'Hello from Client')

print("Socket successfully connected to {} on port:\t {}" .format(url, host_ip))
print(s.recv(1024))
