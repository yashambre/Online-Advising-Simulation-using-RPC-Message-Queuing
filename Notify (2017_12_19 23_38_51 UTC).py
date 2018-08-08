
#Name: Yash Bhushan Ambre
#Student_ID:1001535797
#Login_ID: ya5797
import xmlrpc.client                 #imports Remote Procedure call using XML
from time import sleep               #Used to make the code sleep for a particular time

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")  #manages communication from the server


while (True):
	p=proxy.notify()                   #calls the function notify from the server
	if p != 'message not found':       #checks if any message available
		del p[-1]                      #deletes the last conetent from p
	print(p)
	proxy.Not1(p)                      #sends the result to the server
	sleep(3)                           #sleeps for 7