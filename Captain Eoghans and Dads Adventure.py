# -*- coding: utf-8 -*-
"""
Spyder Editor

Adventure game 

https://github.com/ericclack/python-text-adventure/blob/main/adventure3c.py
"""

import os

# This clears the terminal screen (uses 'cls' for Windows and 'clear' for Mac/Linux)
os.system('cls' if os.name == 'nt' else 'clear')

import time



def dots(number):
    
    os.system('cls' if os.name == 'nt' else 'clear')

    dotis = "..........."
    
    dotis = dotis[:number]
    
    for i in range(0,number,1):
        time.sleep(.1)
        print("\n." + dotis)
        
        dotis = dotis[:-1]
    
dots(5)
print("\nWelcome to the haunted hotel of wonders!!!!!!!!!!!!!!!!!!!!!!!!!!")

class Adventurer:
        health = 100
        def __init__(self, name):
            self.Name =name
    

spung = input("what is your name? \n")

person =Adventurer(spung)

dots(6)
           
print("\n\nHello " + person.Name +".  You are a guest.  People enter this hotel but never leave!!!!\n")



def reception():
  print("\n")
  print("You are standing in the reception of a boutique hotel.  \
There is no entrance door and you do not know how you got into the reception.")
  print("On the reception desk, there is a brass lamp with a green shade and \
underneath stands a sign saying go WEST")
  print("To the North you can see a gloomy room with a yellowish light in one corner.  ")
  print("\nTo the South you can see a gloomy room with a orangeish light in one corner.\nTo the East is a wall covered with moss and snakes.  \nTo the West you can see a gloomy room with a orangeish light in one corner.  ")

  direction = input("What way would you like to go?(N S E W) \n")
  
  if direction == "N":
      marvellousroom()
  elif direction == "E":
      snakeroom()
  elif direction == "S":
      orange()
  else :
      print("Gaboom! You put in a wrong letter!  ")
      reception()
      

def marvellousroom():
    dots(2)
    print("\n")
    print("You are standing in the most marvellous room.  You understand life the universe and everything. Your life is complete!  ")

def orange():
    print("There are 3 differnt doors 1 of the doors ")

def snakeroom():
    print("\n")
    print("You are eaten by snakes.  you are dead!  ")
    

def player_action(directions )     :
    
    x=10
    
reception()    
