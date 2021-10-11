# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................

'''

   Main method of application



   Linear programming only presented here wrt demo of lists



   Parameters:

    none



   Returns:

    none

  '''

if __name__ == "__main__":

    #tuple for student Lnumbers
    lnumbers = ("L1234" , "L4321")

    #list for module subjects
    modules_subjects = ["java programming" , "python scripting"]

    #dictionary for grades
    grades1 = {"java programming" : {"L1234" : 50, "L4321" : 56}}
    grades2 = {"python scripting" : {"L1234" : 45 , "L4321" : 65 }}

    #print grades for each subjects
    print("The mark obtained in java programming is : {}".format(grades1["java programming"]))
    print("The mark obtained in python scripting is : {}" .format(grades2["python scripting"]))












