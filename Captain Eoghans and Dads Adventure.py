# -*- coding: utf-8 -*-
"""
Spyder Editor

Adventure game 

https://github.com/ericclack/python-text-adventure/blob/main/adventure3c.py
"""

from IPython import get_ipython
import time
get_ipython().magic('clear')

def dots(number):

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

from IPython import get_ipython
get_ipython().magic('clear')

dots(6)
           
print("\n\nHello " + person.Name +".  You are a guest.  People enter this hotel but never leave!!!!\n")



def reception():
  print("\n")
  print("You are standing in the reception of a boutique hotel.  \
There is no door and you do not know how you got into the reception.")
  print("On the reception desk, there is a brass lamp with a green shade and \
underneath stands a sign saying go WEST")
  print("To the North you can see a gloomy room with a yellowish light in one corner.  ")
  print("\nTo the South you can see a gloomy room with a orangeish light in one corner.\nTo the East is a wall covered with moss and snakes.  \nTo the West you can see a gloomy room with a orangeish light in one corner.  ")

      
def player_action(directions )     :
    
    x=10
    
reception()    