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

    lnumbers = ("L12345" , "L54321")
    module_list = ["java_programming" , "python_scripting"]

    student1_grade = input("enter student1 grade ")
    student2_grade = input("Enter student2 grade ")

    

    student1_details = {student1_grade , lnumbers[0] , module_list[0]}
    student2_details = {student2_grade , lnumbers[1] , module_list[1]}

    print(student1_details , student2_details)








