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

    # tuple data

    lnumbers = ("L12345" , "L54321")

    #module list data

    module_list = ["java_programming" , "python_scripting"]

    student1 = {"L12345":module_list}
    student2 = {"L54321":module_list}

    print(student1)
    print(student2)

    # read grades of the student

    student1_grade = input("enter student1 grade ")
    student2_grade = input("Enter student2 grade ")

    

    #creating dictionary for students


    student1_details = {lnumbers[0] , student1_grade , module_list[0]}
    student2_details = {lnumbers[1] , student2_grade , module_list[1]}

    print(student1_details , student2_details)








