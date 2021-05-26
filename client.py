# -*- coding: utf-8 -*-
"""
Student ID: 40019093
@author: HUY TRAN
Python version: Python 3.6.4
"""



""" method for clients"""
# databaseMenu() method will provide Menu for user 
def databaseMenu():
    print("\nPython DB Menu\n")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit\n")






# this is the client socket part 

"""REFERENCE: 
https://pythontips.com/2013/08/06/python-socket-network-programming/
https://docs.python.org/3/library/socketserver.html
"""

import socket
import sys

# default port for socket
PORT = 9999

while True:
    # print Menu for user to choose 
    databaseMenu()
    
    # prompt input from user
    number = input("Select: ") 
    
    # creating 4 variables to store input data
    name = ""
    age = ""
    address = ""
    phone = ""
    
    # Prompting data from user according to option number
    if number == "1":
        name = input("Customer Name: ")   
        
    elif number == "2":
        name = input("Customer Name: ")
        age = input("Customer Age: ")
        address = input("Customer Address: ")
        phone = input("Customer Phone Number: ")
    
    elif number == "3":
        name = input("Customer Name: ")
        
    elif number == "4":
        name = input("Customer Name: ")
        age = input("Customer Age: ")
        
    elif number == "5":
        name = input("Customer Name: ")
        address = input("Customer Address: ")
      
    elif number == "6":
        name = input("Customer Name: ")
        phone = input("Customer Phone Number: ")  
        
    elif number == "7":
        number = number
        
    elif number == "8" :
        # "Goodbye" message when exit client
        print("\n-----------------GOODBYE-----------------")
        sys.exit(0)  
    else :
        number = number
    

    # Prepare data 
    data = str(number)+ ","+ str(name)+ ","+ str(age)+ "," + str(address)+ "," + str(phone)
    

    # Create a socket 
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as e:
        print ("Try again! Your socket creation just failed with error %s",e)
    try:
        HOST = socket.gethostbyname("localhost")
    # HOST is not resolved
    except socket.gaierror:
        print("Error in resolving the host")
        sys.exit()
     

    # Connect to server and send data
    clientSocket.connect((HOST, PORT))
    clientSocket.sendall(bytes(data + "\n", "utf-8"))
    
    # Receive data from the server and shut down
    received = str(clientSocket.recv(1024),"utf-8")
    
    print("Server response: ", received)  
