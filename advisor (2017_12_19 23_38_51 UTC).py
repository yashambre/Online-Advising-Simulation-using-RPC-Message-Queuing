
#Name: Yash Bhushan Ambre
#Student_ID:1001535797
#Login_ID: ya5797
import xmlrpc.client                         #imports Remote Procedure call using XML
import random
from time import sleep                       #Used to make the code sleep for a particular time 

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")  #manages communication from the server

while (True):
    p=proxy.advisor1()                     #calls the function notify from the server
   
    if p != 'message not found':            #checks if any message available           
        z=(random.choice([0,1]))            # module implements pseudo-random number generators for various distributions.
        if (z):
            p.insert(1,'Not available')               #inserts the result that it is available
        else:
            p.insert(1,'available')               #inserts the result that it is not available

        #print (p)
        p[-1] = 'advisor'                   #appends advisor to the end of the result
        print(p)
        proxy.out(p)                        #sends the result to the server
    sleep(7)                                #sleeps for 7 seconds 