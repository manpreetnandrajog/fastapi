#Print Syntax
#print("hello world");
#print(" Hello Coders");

#Variable Syntax
from argparse import Namespace
from ast import Name
from http.client import CONTINUE
import math
import operator
from unicodedata import name
from unittest import result


#name = "Manpreet"
#age= 21

#name= "aman"
#age= 16

#is_adult = False
#print("name",name)
#print (name)
#print (age)
#print (is_adult)

#EXERCISE
#First_Name = "Tony "
#Last_name= "Stark"
#age= 51
#is_genius= True

#print( First_Name + "" + Last_name)
#print(age)
#print(is_genius) 

#name= input ("what is your name?")
#print("Hello"+ name)

##EXERCISE##
#name= input ("Who is your favorite superhero?")
#print(name + "" + ", Amazing!!") 

##Type Conversion
#old_age= input("enter your old age:")
#new_age = int(old_age) + 2
#print(new_age)

##SUM OF TWO NUMBERS
#A= input("Enter the desired first number: ")
#B= input("Enter the desired second number: ")
#sum= int (A) + int (B)
#print("the sum is :" + str(sum))

##STRING
#name= "Tony Stark"
#print(name.upper())
#print(name)

##FIND OPERATOR
#name= "Tony Stark"
#print(name.find('S'))
#print(name.replace("Tony Stark", "Ironman"))

##KEYWORDS
#print('T' in name)
#print('Ironman' in name)

##ARITHMETIC 
#print(66//6)


##SHORTCUTS
#i=5
#i+=2
#print(i)

##PRECEDENCE
#result = 2+3*5
#print(result)

#COMPARISON
#print(3>4)
#print(3>=4)
#print(3!=4)

#LOGICAL OPERATORS
#print(2>3 or 6>3)
#print(2>3 and 6>3)
#print( not 2>3 )

##IF-ELSE STATEMENT
#age = 13
#if age>= 18: #intial condition
  #  print("you are an adult")
   # print("you can vote")
#elif age < 18 and age > 3 : #to check and jump onto the second / third/fourth condition
   #  print("you are in school")
#else: #the find sentence/condition
   # print("you are a child")     
#print("thank you")

## EXERCISE {BUILTING A CALCULATOR}
#first = input("enter the first number:")
#operator = input ("enter operator (+,-,*,/,%) : ")
#second= input("enter the second number:")

#first = int(first)
#second = int (second)

#if operator == "+":
   # print(first+ second)
#elif operator == "-":          #if checks the condition regardlesds of it being true before unlike that of elif which only checks it when the condition is fails
   # print( first- second)
#elif operator == "*":
  #  print(first * second)
#elif operator == "/":
   # print(first / second)
#elif operator == "%":
  #  print(first % second)
#else:
   # print("Invalid operation")               

## RANGE - FROM ONE POSITION TO THE NEXT
#number= range(5)
#print(number)

## LOOP
#i=1
#while i <= 5:
   # print(i)
   # i= i+1
#while i <= 5:
  #  print(i * "*")
   # i= i+1  
#i=5  
#while i >= 0 :
 #   print(i * "*")
  #  i= i-1    
 
#for i in range (5):
 #   print(i)

##LIST
#marks = [34,23,67,56]
#print(marks)

#PRINTING FROM A SPECIFIC POSITION
#marks = [34,23,67,56]
#print(marks[-1])

#MAKING ONLY FIRST TWO INDEX PRINT IN A NEW LIST
#[0:2 ] HAI TOH SIRF 0 AUR 1 HE INCLUDE HOGA,NOT 2
#marks = [34,23,67,56]
#print(marks[0:2])

#FOR LOOP IN LIST
#marks= [43,56,78]
#for score in marks:
 #   print (score)

#append()- join karna 
#marks.append(99)  
#print(marks)

#INSERT()
#marks.insert(0,99)
#print(marks)
#TO CHECK IF A CERTAIN NUMBER EXISTS IN THE STRING OR NOT
#print(99 in marks)
#LENGTH OF IT
#print(len (marks))

#WHILE LOOP
#i=0
#while i < len(marks):
 #   print(marks[i])
#    i=i+1

#marks.clear()
#print(marks)

##BREAK & CONTINUE
#BREAK
#TO PRINT TILL RADHA
#students = ["ram", "shyam", "radha", "radhika", "suresh"]

#for student in students:
 #   if student == "radha" :
  #      break
  #      print(student)

#TO PRINT EVERY NAME EXCEPT SURESH
#for student in students:
 #   if student == "SURESH" :
  #      CONTINUE
   #     print(student)

#TUPLE   - LIKE LIST BUT NOT EDITABLE USING () PARENTEHIS
#MARKS= (98,97,99, 97,97)
#print(MARKS.count(97))
#print(MARKS.index(97))

#SETS- TO SAVE UNIQUE ELEMENTS FROM A SET USING {} PARENTEHIS- CANT FIND INDEX IN IT- IS UNORDERED
#MARKS= {98,97,99, 97,97}
#print(MARKS)
#for score in MARKS:
 #   print(score)

#DICTIONARY - STORES VALUE IN PAIR
#marks= {"english": 95, "chemistry": 98}

#print(marks["chemistry"])
#marks["physics"] = 97;
#print(marks)

#marks["physics"] = 99;
#print(marks)

#FUNCTIONS
# 1. IN-BUILT FUNCTION - INT(), STR(), BOOL()

# 2. MODULE FUNCTION- WHEN RELATED FUNCTIONS AND RELATED VARIABLES ARE STORED IN SAME FILE - EX: MATH

#import math
#print(dir(math))

#SELECT A PARTICULAR FUNCTION
#from math import sqrt
#print(sqrt(16))

#SELECT ALL FUNCTIONS
#from math import *
#print (sqrt(16))

# 3. USER-DEFINED FUNCTION
# SYNTAX:
# def function_name(parameters):
def print_sum(first, second):
    print(first + second)
print_sum(1,2) 
   
