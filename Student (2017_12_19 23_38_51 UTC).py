
#Name: Yash Bhushan Ambre
#Student_ID:1001535797
#Login_ID: ya5797
from xmlrpc import client                     #imports Remote Procedure call using XML

proxy = client.ServerProxy("http://localhost:8000/") #manages communication from the server
 
DET1=[]                                             #opens a list named DET1
user_input = input("Enter course and name: ")       #takes the input of course and name  
dek = user_input.split(',')                         #used to split the input with ',' 
numbers = [str(x.strip()) for x in dek]             #Strip returns the string without white space
DET1.append(numbers)                                #appends the input to the list
DET1.append("student")                              #appends the student at the end
print (DET1)
proxy.mqs(DET1)                                     #sends the list to the server
