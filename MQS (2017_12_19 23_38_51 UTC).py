
#Name: Yash Bhushan Ambre
#Student_ID:1001535797
#Login_ID: ya5797
from xmlrpc.server import SimpleXMLRPCServer       #server using Remote Procedure call    
import xmlrpc.client                               #imports Remote Procedure call using XML
import ast                                         #Abstract Syntax treemodule helps Python applications to process trees of the Python abstract syntax grammar

filename='try.txt'                                 #sets text file as filename
data = open(filename,'r+')                         #reads the contents of the file and saves the contents to data
file_queue = data.read()                           #reads the data and puts in file_queue
m = ast.literal_eval(file_queue)                   
#print(m)

def mqs(y):                                        #function of the Message queueing server
	m.insert(0,y)                                  #inserts the input of student to the list
	filename='try.txt'
	data=open('try.txt','r+')
	#for item in m:
		#data.write("%s\n" % item)
	data.seek(0)                                   #move the internal result pointer		
	data.write(str(m))                             #writes the list to the file		
	print(m)                                      
	

def advisor1():                                    #creates the function of advisor
	if len(m) == 0:                                #checks the length of the list
		return('message not found')                #shows no message present
	else:
		i=len(m)-1                                 #sets the value i to the second last element
	while i >= 0:
		#for i in range (len(list1)):
		if m[i][-1] == 'student':                  #check the last value of the list if student
			AD=m[i]                                #sets the list to variable to 'AD'
			print (AD)
			del m[i]                               #delets the last element from the list
			data.seek (0)                          #move the internal result pointer
			data.write(str(m))                     #writes the list to the file 
			print(m)
			return AD                          
		else:
			return ('message not found')           #returns that no message is available 
		i=i-1

def out(y):
	m.append(y)
	print ("This is out",m)
	
	data.seek (0)                                  #move the internal result pointer
	data.write(str(m))                             #writes the list to the file 
	
	
def notify():                                      #create the function of notification
	if len(m) == 0:                                #checks the lenght of the list
		return('message not found')
	else:
		i=len(m)-1                                 #sets the value i to the second last element
		while i >= 0:
		#for i in range (len(m)):
			if m[i][-1] == 'advisor':              #check the last value of the list if advisor
				z=m[i]
				del m[i]
				data.seek (0)                      #move the internal result pointer
				data.write(str(m))                 #writes the list to the file  
				print("this is notify:",z)         #notifies if the message is present 
				return z                       
			else:
				return ('message not found')       #if ther is no message
			i=i-1
				
def Not1(h):                                       #takes the result from the notification
	print(h)
	
server = SimpleXMLRPCServer(("localhost", 8000),allow_none=True)   #Opens the connection for all the clients
print("Listening on port 8000...")
server.register_function(mqs, "mqs")                                 #Registers the function that can respond to XML-RPC requests   
server.register_function(advisor1, "advisor1")                     #Register a function that can respond to XML-RPC requests
server.register_function(out, "out")                               #Register a function that can respond to XML-RPC requests
server.register_function(notify, "notify")                         #Register a function that can respond to XML-RPC requests 
server.register_function(Not1, "Not1")                             #Register a function that can respond to XML-RPC requests
server.serve_forever()                                             #Handle requests until an explicit shutdown() request.