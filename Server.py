#This is a Server side Code to listen for a Client connection on a specific port

# first of all import the socket library
import socket
import json
reply = {}

#This is the reply which shall be sent to the user on successful connection
reply['CONNECTED'] = 'Thank you for Connecting'
reply = json.dumps(reply, ensure_ascii=False).encode('utf-8')

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 3000

def startListening():
	try:
		#Create a Socket Object
		s = socket.socket()
		print("\nCreating Socket..")
		# Next bind to the port
		# we have not typed any ip in the ip field
		# instead we have inputted an empty string
		# this makes the server listen to requests
		# coming from other computers on the network
		s.bind(('', port))
		print("\nSocket binded to {}" .format(port))

		# Put the socket into listening mode
		s.listen(5)
		print("Socket is listening")
		# Forever loop until we interrupt it or until an error occurs
		while True:
			# Establish connection with client
			connection, addr = s.accept()
			print("Received Connection request from:\t{}".format(addr))
		   	# send a thank you message to the client.
			data = connection.recv(1024)
			#Decode the Received data from utf-8 format
			data = data.decode('utf-8')
			a = len(data)
			print("Length of Data:\t{}".format(a))
			#Check if Data received is in Valid JSON format
			if(data[0:1] != '{'):
				print("Valid Data not found\nClosing this Connection")
				connection.close()
				continue
			else:
				print("Received data from Client:\t{}".format(data))
				connection.send(reply)

			# Close the connection with the client
			#connection.close()
	except KeyboardInterrupt:
		print("\nStopping all connections.\nClosing Server Socket on port:\t{}".format(port))
		connection.close()
	except socket.error:
		print("Socket Connection Faced problems before listening to Clients\n")
		print("Please Check if some other process is running on the same port")


try:
	startListening()
except UnboundLocalError:
	print("Server stopped unexpectedly before connecting to Clients")
