''' WAP to input name, marks and phone number of a student
and format it using the format function like below 

"The name of the student is xyz , his marks are 12 and phone numner is 
000000000"
'''

name = input("enter your name : ")
marks =input("Enter your marks : ")
phone = input("enter your phone number : ")

temp = "The name of the student is {}, his marks are {} and phone number is {}" 
output = temp.format(name,marks,phone)
input(output)
