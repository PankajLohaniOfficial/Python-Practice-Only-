# Write a Program to find the greatest of the 4 number entered by the user:

a = int ( input ( " Enter the First Number :- " ))
b = int ( input ( " Enter the Second Number :- " ))
c = int ( input ( " Enter the Third Number :- " ))
d = int ( input ( " Enter the Fourth Number :- " ))

if ( a > b and a > c and a >d ):
  print ( "A is the highest" )

if ( b > a and b > c and b >d ):
  print ( "B is the highest" )

if ( c > b and c > a and c > d ):
  print ( "C is the highest" )

if ( d > b and a > c and d < a ):
  print ( "D is the highest" )
