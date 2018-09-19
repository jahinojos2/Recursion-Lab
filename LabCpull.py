import itertools
import hashlib
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:07:50 2018
@author: Jaime A Hinojos
ID: 80590883
Date: 9/12/18
Lab C
"""
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
def reader(): #opens the file and returns an array with the length of lines
    with open('password_file.txt') as f:
        line = f.read().splitlines()
        return line
def compare(file,password):#takes in the file array and password array created to compare 
     for i in range(len(password)): #for loop that will use every possible password to be compared
         for j in range(len(file)):#for loop that will use every possible hash password of the file to be compared
             element = file[j].split(',') #array that will store the elements when splitting each line
             test = ''.join(map(str,password[i])) #since the password creation is a cartesian product it will be joined together to create a string
             if len(element) != 3: #case to check if the file was set up correctly
                 print("line is not set up correctly")
                return
             elif element[2] == hash_with_sha256(test+element[1]):#checks the 3 element which is the hashed passcodeand compares it to the concatenation of the created password with the salt value of the user 
                 print("Password: "+test+" unlocks "+element[0]+"'s account") 
             elif j+1 == 100: #deterimnes that the password was ot found in the list
                 print("Password: "+test+" not found")
def createPass(num, num2, fileArray):     
    if num > num2:
        return print("the first parameter is larger than the second")
    if fileArray is None:
        return print("file is empty")
    passwords = []
    passwords = list(itertools.product(range(10), repeat=num))
    compare(fileArray, passwords)
    createPass(num+1, num2, fileArray)
    
                 
try:
    fileArray = []
    fileArray = reader()
    num1 = int(input("Enter smallest length of password to be created: "))
    num2 = int(input("Enter largest length of password to be created: "))
except IOError: #file not found exception
    print("file not found")
except Exception: #since we'll be evaluating the inputs simple exception is able to be used
    print("Invalid parameters")
else:
    pass
    createPass(num1,num2,fileArray)
# Test Case 1: file with name password.txt this is just to see if it catches the file not found exception
# Test Case 2: either parameter input h to see if it catches the invalid input exception
# Test Case 3: both parameters set to the same number (Ex: num1=4 num2=4) to just call the method once and return the results of that one
# Test Case 4: Empty file to execute and return that the file given is empty so it doesn't call the method password creation method and just returns the message
# Test Case 5: first number is greater than the second and it to be able to not run the program and print that the parameters were not set correctly
# Test Case 6: Try different and correct variations of string length so it returns all possible combinations along with comparison of the passwords in the file
