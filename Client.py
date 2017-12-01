#This is a Client side Code to connect to a Server which is listening on a specific port

# Import socket module
import socket
import json
data = {}

url = "127.0.0.1"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Object successfully Created and Initialized")
except socket.error as err:
    print("Socket Creation failed with error {}" .format(err))

# default port for socket
port = 3000

try:
    host_ip = socket.gethostbyname(url)
    print("IP Address for {} is:\t{}".format(url, host_ip))
except socket.gaierror:
    # this means could not resolve the host
    print("There was an error resolving the Host")
    sys.exit()

# connecting to the server
s.connect((host_ip,port))

#Data to sent to Server as a JSON Object
data['Milk_Temperature'] = '-30'

#Create JSON data object
json_data = json.dumps(data, ensure_ascii=False)

#Convert JSON Data Object to Bytes to send it over HTTP
json_data = json_data.encode('utf-8')

#Send JSON Data encoded in utf-8 to Server
s.send(json_data)
print("Socket successfully connected to {} on port:\t {}" .format(url, port))

#Store the received byte
received = s.recv(1024)

#Decode the Received byte from utf-8 string format
received = received.decode('utf-8')
print(received)
