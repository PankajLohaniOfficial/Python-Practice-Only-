# Write a program to find out whether the student is pass or fail , if it requires a total of 40 percent and atleast 33 percent in each subject to pass , assume 3 subjects and take input from the user


num1 = int ( input ( " Enter the 1st mark :- "))
num2 = int ( input ( " Enter the 2nd mark :- " ))
num3 = int ( input ( " Enter the 3rd Mark :- " ))

#check for the total percentage
total_percentage = (100 * (num1 + num2 + num3))/300 
if ( total_percentage and num1 >= 33 and num1 >= 33 and num2 >= 33):
  print ( " You are pass" , total_percentage )
else:
  print ( " You are fail, Try again next year " , total_percentage )
