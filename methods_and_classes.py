# -*- coding: utf-8 -*-
"""
Student ID: 40019093
@author: HUY TRAN
Python version: Python 3.6.4
"""



"""class CustomerData"""

class CustomerData:
    # default constructor with 4 instance variables
    def __init__(self, firstName, age, address, phoneNum):
        self.firstName = firstName
        self.age = age
        self.address = address
        self.phoneNum = phoneNum


    # 4 getters
    def getName(self):
        return self.firstName
    
    def getAge(self):
        return self.age
    
    def getAddress(self):
        return self.address
    
    def getphoneNum(self):
        return self.phoneNum

   

    # this is my toString() method just like in Java
																				 
    def __str__(self):
        # format output of phone number
        whiteSpace = " "
        for whiteSpace in self.phoneNum:
            self.phoneNum = "-".join(self.phoneNum.split(" "))
        # return the complete formatted string for output purpose
        return self.firstName+"|" + self.age + "|" + self.address + "|" + self.phoneNum
    

    
    # 4 setters
    def setName(self, name):
        self.firstName = name
        return self.firstName
    
    def setAge(self, age):
        self.age = age
        return self.age
    
    def setAddress(self, address):
        self.address = address
        return self.address
    
    def setPhoneNum(self, phone):
        self.phoneNum = phone
        return self.phoneNum
    
              
    
    
    



""" methods for server """
# creating an empty list to store all the tuples which contain data of each customer    
listOfTuples=[] 

# readFile() method will read file data.txt and check for additional leading or trailing spaces
def readFile():
    file = open("data.txt", 'r')
    for line in file:
        # if line is empty, skip the entire line
        if line != '':
            # strip off the "\n" in each String line and split into each element in a list
            lineList = line.strip().split('|') 
            # removing whitespace in each element of the lineList
            for i in range(len(lineList)):
                lineList[i]= lineList[i].strip(' ')
            # check if there exists "firstName" of a client or not. 
            # If the name is missing, the record would be skipped.
            if lineList[0]!='':   
                # casting our lineList into tuple 
                tup = tuple(lineList)  
                # update each tuple in our list structure    
                listOfTuples.append(tup)        
    file.close()
    
# execute readFile() method
readFile()



# create an empty list ot store each object customer
listOfObjects = []
# unpacking each list in listOfTuples
for item in listOfTuples:
    name, age, address, phone = item
    # creating eachCustomer which is the object containing 4 fields
    eachCustomer = CustomerData(name, age, address, phone)
    listOfObjects.append(eachCustomer)























  
    
    
    
    
  
    
    
    




    
        




