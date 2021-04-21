import socket
import pickle
from info import _send_msg, _recv_msg
from info import storage_ip, MSG_SIZE

STORAGE_ID = 1
	 
s = socket.socket()         
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port =  storage_ip[STORAGE_ID]["port"]   
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening...")            
  
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
	print("Waiting for Connections .. ")
	# Establish connection with client. 
	c, addr = s.accept()     
	print ('Got connection from', addr )
	  
	# send a thank you message to the client. 
	msg = _recv_msg(c, MSG_SIZE)
	print(f"Got some message from {addr}")

	if msg ==None :
		print("No Packet Recieved at all...[ERROR]")
	
	elif(msg["type"] == "WRITE"):
		print("Recieved file...")
		
		file = open("./data/" + str(msg["client_username"]) +"_"+ str(msg["file"]), 'wb')
		file.write(msg["data"])
		file.close()
		print("Saved !!")

		_send_msg(c, {"error":False, "error_type":None})


	elif msg["type"] == "READ":
		print("Sending file...")
		file = open("./data/"+ str(msg["client_username"]) +"_"+ str(msg["file"]), 'rb')

		pg = file.read()

		file.close()
		# print(pg)
		msg = {"error":False, "error_type": None, "data":pg}
		print("Sent !!")

		_send_msg(c, msg)

	print("Closing Socket..\n")
	c.close()


s.close()
# Close the connection with the client 
#c.close()

