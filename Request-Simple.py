#This is a Simple Connection to a WebSite using Python
#This is Compatible with Python3 / 3.5

from http.client import HTTPConnection
print("HTTP Client Library successfully Imported")

HTTPConnection.debuglevel = 1

from urllib.request import urlopen
print("URLLIB successfully imported")

#Connecting to Website
url = "https://www.w3schools.com/xml/note.xml"
print("Opening Connection to {}".format(url))
response = urlopen(url)

#Reading Response Headers sent from the Website
print("Response Headers Obtained:\n")
print(response.headers.as_string())

#Reading Data from Website
print("Reading Data\n")
data = response.read()

#Calculating Length of Data received
print("Length of Data received is:{}".format(len(data)))

#Display Data received
print("Data received:\n")
print(data)
