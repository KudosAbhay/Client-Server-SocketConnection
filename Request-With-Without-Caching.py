import httplib2
print("Importing httplib2")

import time
print("Time Library is Successfully imported")

def parsingResponse(resp,content):
	print("Response Status:\t{}".format(resp.status))
	Length_of_Received_Data = len(content)
	print("Length of Response Content:\t{}".format(Length_of_Received_Data))        #Returns HTTP Status obtained from Response
	#print("=========== Raw Data =================\n")
	#print(content[0:Length_of_Received_Data])    #Read Data content from position:0 to End of Content. Displays Raw Data
	#print("\n========= End of Raw Data ===========")
	print(dict(resp.items()))			#Displays Headers received
	print(response.fromcache)                       #TRUE: Response is Displayed from Cache
	print(content.decode('utf-8'))                  #Displays Content of the XML File in Readable Format
	print("\n\n")

url = "https://www.w3schools.com/xml/note.xml"
#url = "https://api.thingspeak.com/channels/****/feed.json"

print("***************************************************")
h = httplib2.Http('.cache')
print("Enabling Caching")
t0 = time.time()				#Initiate Timer
print("Hitting {} with caching".format(url))
response, content = h.request(url)
parsingResponse(response,content)
t1 = time.time()				#Stop Timer
total = t1 - t0
print("Total Time Taken for this Request:\t{}\tseconds".format(total))

print("***************************************************")
t0 = time.time()				#Initiate Timer
print("Hitting {} without caching".format(url))
response2, content2 = h.request( url, headers={'cache-control':'no-cache'})
parsingResponse(response2,content2)
t1=time.time()						#Stop Timer
total = t1-t0
print("Total Time taken for this Request:\t{}\tseconds".format(total))
print("***************************************************")






