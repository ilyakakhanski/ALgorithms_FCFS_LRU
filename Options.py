import os
import numpy as n
def rand():#completes an array with random numbers from a range
   processes=[]
   length=int(input("The length of the range(from 1 to 9):"))
   while length <=0:
      length=int(input("The length of the range(from 1 to 9):"))
   amount=int(input("The amount of numbers you want to draw:"))
   while amount <=0:
      amount=int(input("The amount of numbers you want to draw:"))
   for i in range(amount):
      processes.append(n.random.randint(1,length))
   return processes

def own():#reading numbers into an array
    processes = list(map(int,input("Enter the reference string: ").strip()))
    return processes
    
def cells():#providing frame values for creating the algorithm
    cell= int(input("Enter the number of cells: "))
    while cell<=0:
       os.system("cls")
       cell= int(input("Enter the number of cells: "))
    return cell

def choice():#choice of options (random numbers or your own range of numbers)
    print("Choose from 2 options: \n1.Random parametrs\n2.Your own parametrs")
    option=int(input("Your option:"))
    while option!=1 or option!=2:
      if option==1:
        processes=rand()
        return processes
        break
      if option==2:
        processes=own()
        return processes
        break
      option=int(input("Your option:"))
      

         
