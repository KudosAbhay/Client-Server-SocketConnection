'''import urllib.request
print("URLLIB imported")

url = ""

wp = urllib.request.urlopen(url)
print("URLLIB is fetching data from the Website")

pw = wp.read()
print("Reading data sent from the Website")

print("Printing Data now:\n")
print(pw)
'''


from http.client import HTTPConnection
print("HTTP Client successfully Imported")

HTTPConnection.debuglevel = 1

from urllib.request import urlopen
print("URLLIB successfully imported")

url = "https://www.w3schools.com/xml/note.xml"
print("Opening Connection to {}".format(url))

#response = urlopen('http://diveintopython3.org/examples/feed.xml')
response = urlopen(url)

print("Response Headers Obtained:\n")
print(response.headers.as_string())

print("Reading Data\n")
data = response.read()

print("Length of Data received is:{}".format(len(data)))


print("Data received:\n")
print(data)
