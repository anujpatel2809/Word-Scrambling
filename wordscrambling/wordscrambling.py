'''
Created on Dec 26, 2016

@author: Anuj
'''
import scramblingModule
import sys
ip_file_name = input("Enter File name(Specify full path of file if it is not in current directory) : ")
try :
    print("Output File : ",scramblingModule.WordScrambling().scrambleFile(ip_file_name))
except :
    print(sys.exc_info()[1])
   


