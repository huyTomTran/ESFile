# -*- coding: utf-8 -*-
"""
Student ID: 40019093
@author: HUY TRAN
Python version: Python 3.6.4
"""




""" methods for choosing options"""

# we need to import methods_and_classes module
import methods_and_classes

""" 
In ALL cases, we will lookup customers by name (these are CASE SENSITIVE matches).
Otherwise, by adding lower() method will take care of the NON-CASE SENSITIVE matches.
According to the instructions from the professor, I did NOT put check NON-CASE SENSITIVE matches  
""" 

# I am using listOfObjects to MANIPULATE the customer information 
# which CAN be found in  methods_and_classes module



# findCustomer() method   
def findCustomer(name):
    for i in range(len(methods_and_classes.listOfObjects)):
         if methods_and_classes.listOfObjects[i].getName() == name:
             # return the information of when the specified customer is found
             return str(methods_and_classes.listOfObjects[i])
    return (name + " not found in database")   
    
 
    
    
# addCustomer() method will add one specified customer to the list
def addCustomer(name, age, address, phone) : 
    for i in range(len(methods_and_classes.listOfObjects)):
        # check if a customer's name is already exist
        if methods_and_classes.listOfObjects[i].getName() == name:
            return name + " already exists"
    # creating a new object Customer  
    newCustomer = methods_and_classes.CustomerData(name, age, address, phone)
    # adding new customer with his/her information into the list of objects
    methods_and_classes.listOfObjects.append(newCustomer)
    return (name + " information has been successfully added in database")      




# deleteCustomer() method will delete one specified customer in the list
def deleteCustomer(name):
    for i in range(len(methods_and_classes.listOfObjects)):
        if methods_and_classes.listOfObjects[i].getName() == name:
            # using pop() method to delete Customer in my database
            methods_and_classes.listOfObjects.pop(i)
            return (name + "'s information has been successfully removed in database")
            # break out of the loop once the specified customer is removed from the list
            break                              
    return (name + " does not exist")   
    

    

# updateAge() method will update one specified customer's age in the list
def updateAge(name, age):
    for i in range(len(methods_and_classes.listOfObjects)):
        if methods_and_classes.listOfObjects[i].getName() == name:
            methods_and_classes.listOfObjects[i].setAge(age)                
            return (name + "'s age has been successfully updated in database")
            # break out of the loop once the specified customer's age is updated from the list
            break                
    return (name + " not found in database")         




# updateAddress() method will update one specified customer's address in the list
def updateAddress(name, address):
    for i in range(len(methods_and_classes.listOfObjects)):
         if methods_and_classes.listOfObjects[i].getName() == name:
             methods_and_classes.listOfObjects[i].setAddress(address)                
             return (name + "'s address has been successfully updated in database")
             # break out of the loop once the specified customer's address is updated from the list   
             break
    return (name + " not found in database")      




# updatePhone() method will update one specified customer's phone in the list
def updatePhone(name, phone):
    for i in range(len(methods_and_classes.listOfObjects)):
        if methods_and_classes.listOfObjects[i].getName() == name:
            methods_and_classes.listOfObjects[i].setPhoneNum(phone)                
            return (name + "'s phone has been successfully updated in database")
            # break out of the loop once the specified customer's phone is updated from the list   
            break
    return (name + " not found in database")         




# printReport() method
def printReport():
    info = ""
    for i in range(len(methods_and_classes.listOfObjects)):
        info = info + str(methods_and_classes.listOfObjects[i]) + '\n'
    info = "\n** Python DB contents **\n" + info
    return(info)
        
  
    
    
    
    
    
    

#  this is the socketserver part 

# REFERENCE: https://docs.python.org/3/library/socketserver.html
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """  
    def handle(self):
      
        # self.request is the TCP socket connected to the client and decode data received from client
        self.data = self.request.recv(1024).strip().decode("utf-8")
        print("{} wrote:".format(self.client_address[0]))
        
        # split data, and now it is a list contains 5 elements in the folowing order: number, name, age, address, phone
        self.data = self.data.split(',')
        
        
        if self.data[0] == "1" :
            toSent = findCustomer(self.data[1])
           
        elif self.data[0] == "2" :
            toSent = addCustomer(self.data[1],self.data[2], self.data[3], self.data[4])
            
        elif self.data[0] == "3" : 
            toSent = deleteCustomer(self.data[1])
             
        elif self.data[0] == "4" :
            toSent = updateAge(self.data[1], self.data[2])
            
        elif self.data[0] == "5" :
            toSent = updateAddress(self.data[1], self.data[3]) 
            
        elif self.data[0] == "6" :
            toSent = updatePhone(self.data[1], self.data[4])
            
        elif self.data[0] == "7" :
            toSent = printReport()
            
        else:
            toSent = "Invalid input. Please enter number only from 1 to 8"
            

        # send back the same data to the client
        self.request.sendall(bytes(toSent + "\n","utf-8"))
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
        
    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until we
        # kill the program 
        server.serve_forever()
        
