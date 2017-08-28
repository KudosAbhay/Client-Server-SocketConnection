#This is a Server side Code to listen for a Client connection on a specific port

# first of all import the socket library
import socket

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 8000

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
			c, addr = s.accept()
			print("Received Connection request from:\t{}".format(addr))
		   	# send a thank you message to the client.
			c.send(b'Thank you for connecting')
			#d = c.recv(1024)
			#print(d)

			# Close the connection with the client
			#c.close()
	except KeyboardInterrupt:
		print("\nStopping all connections.\nClosing Server Socket on port:\t{}".format(port))
		c.close()
	except socket.error:
		print("Socket Connection Faced problems before listening to Clients")


try:
	startListening()
except UnboundLocalError:
	print("Server stopped unexpectedly before connecting to Clients")
