#Store your Name, Age, Weight, Whether you are a student or not (True for yes, False for no) in respective variables.
#  What do you think is the data type of each variable? 
# Print the data type of every variable. 
# Change the datatype of Age to string and Weight to an integer.


nam="samira"
age="20"
weight=55
isStudent=True

#before typecasting
print("Datatype of",nam,"before typecasting is",type(nam))
print("Datatype of",age,"before typecasting is",type(age))
print("Datatype of",weight,"before typecasting is",type(weight))
print("Datatype of",isStudent,"before typecasting is",type(isStudent))

#after typecasting

isStudent=str(isStudent)
weight=int(weight)
age=float(age)

print("Datatype of",age,"after typecasting is",type(age))
print("Datatype of",weight,"after typecasting is",type(weight))
print("Datatype of",isStudent,"after typecasting is",type(isStudent))
