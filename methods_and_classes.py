
# -*- coding: utf-8 -*-
"""
@author: HUY TRAN
Python version: Python 3.6.4
"""



"""class CustomerData"""

class EmployeesData:
    # default constructor with 2 instance variables
    def __init__(self, employeeNumber, employeeName):
        self.employeeName = employeeName
        self.employeeNumber = employeeNumber
      


    # 2 getters
    def getEmployeeName(self):
        return self.employeeName
    
    def getEmployeeNumber(self):
        return self.employeeNumber

   

    # this is my toString() method just like in Java
     # this is DOUBLE-CHECK just in case employee name is given wrongly formatted
    def __str__(self):
        # format output of employee name
        comma = ","
        for comma in self.employeeName:
            self.employeeName = ",".join(self.employeeName.split(" "))
        # return the complete formatted string for output purpose
        return self.employeeName+"," + self.employeeNumber 
    

    
    # 2 setters
    def setName(self, name):
        self.employeeName = name
        return self.employeeName
    
    def setAge(self, age):
        self.employeeNumber = employeeNumber
        return self.employeeNumber
    
   
    
              
    
    
    



""" methods for server """
# creating an empty list to store all the tuples which contain data of each customer    
listOfTuples=[] 

# readFile() method will read file employees.dat and check for additional leading or trailing spaces
def readFile():
    file = open("employees.dat", 'r')
    for line in file:
        # if line is empty, skip the entire line
        if line != '':
            # strip off the "\n" in each String line and split into each element in a list
            lineList = line.strip().split(',') 
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
    employeeNumber, employeeName = item
    # creating eachCustomer which is the object containing 4 fields
    eachEmployee = EmployeesData(employeeNumber, employeeName)
    listOfObjects.append(eachEmployee)



























  
    
    
    
    
  
    
    
    




    
        




