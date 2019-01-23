import os
from time import sleep
import operator
import sys
sys.path.append('E:\\TxtRpg\\Modules')
from Locations import *

forest = Forest

def Talk(text):
  print(text)

def start():
  loadStuff = input("Would you like to Load a Save? y/n: ")
  if loadStuff == 'y':
    print("WIP")
    start()
  elif loadStuff == 'n':
    newCharacter()
  else:
    print("Listen Here you little shit how hard is it to type in y or n?!")
    start()
  

def debug():
  print("Debug Mode Activated")

def newCharacter():
  nameInput = input("Enter your name: ")
  if nameInput == "debug":
    debug()
  else:
    global selfPlayer
    selfPlayer = None
    raceInput = input("Enter your characters race: ")
    if raceInput == "Sc" or raceInput == "Elf" or raceInput == "Dark Elf" or raceInput == "Khajit" or raceInput == "Dragonborn" or raceInput == "Demon":
      selfPlayer = Character(nameInput,raceInput,"None",1,1,1,1,1)
      global skillPoints
      skillPoints = 0
      setPlayerForest(4)
      return
    else:
      print("Invalid Class Please Try Again")
      newCharacter()
 


class Character:
  def __init__(self, name, race, Class, Str, Mag, Def, Spd, Luck):
    self.name = name
    self.race = race
    self.Class = Class
    self.Str = Str
    self.Mag = Mag
    self.Def = Def
    self.Spd = Spd
    self.Luck = Luck
    self.level = 1
    self.Location = None
    self.position = None
    self.Pos = None
  def LevelUp(self):
    self.level = self.level + 1
    return self.level
  def setStatInc(self):
    #Class Increase
    if self.Class == "Swordsman":
      self.lvlStats = [3,1,2,2,1]
    elif self.Class == "Rouge":
      self.lvlStats = [1,2,1,3,2]
    elif self.Class == "Wizard":
      self.lvlStats = [1,3,1,2,2]
    elif self.Class == "Healer":
      self.lvlStats = [1,2,1,2,2]
    elif self.Class == "Tank":
      self.lvlStats = [2,1,3,2,1]
    elif self.Class == "Ranger":
      self.lvlStats = [2,1,1,2,3]
    else:
      print("ERROR:\nClass is Invalid")
    #Race Increase
    if self.race == "Sc":
      self.lvlStats = map(operator.add,self.lvlStats,[0,1,2,0,0])
    elif self.race == "Elf":
      self.lvlStats = map(operator.add,self.lvlStats,[2,0,0,1,0])
    elif self.race == "Dark Elf": 
      self.lvlStats = map(operator.add,self.lvlStats,[0,0,0,2,1])
    elif self.race == "Khajit":
      self.lvlStats = map(operator.add,self.lvlStats,[1,0,1,0,1])
    elif self.race == "Dragonborn":
      self.lvlStats = map(operator.add,self.lvlStats,[0,2,1,0,0])
    elif self.race == "Demon":
      self.lvlStats = map(operator.add,self.lvlStats,[0,1.0,0,2])
    else:
      print("\nERROR:\nRace is Invalid Please Restart\n")
      sleep(10000000)
    return self.lvlStats
  def setLocation(self, location, ent, pos):
    self.Location = location
    selfPlayer.setPosition(ent,pos)
  def setPosition(self,d,pos):
    if d == 'u':
        self.position = forest.allForest[pos-11]
        pos = pos-11
    elif d == 'd':
        self.position = forest.allForest[pos+11]
        pos = pos+11
        print(pos + 11)
    elif d == 'l':
        self.position = self.position[pos-1]
        pos = pos-1
    elif d == 'r':
        self.position = self.position[pos+1]
        pos = pos+1
    else:
      self.position = d
    return self.position
  
def pickClass():
  classTxt = input("Which Class Would You Like To Choose? Type /help Class to learn about the classes and /help (class name) for a more in depth look into a class: ")
  if classTxt == "/help Class": 
    print("The Classes Are: \nSwordsman\nRouge\nWizard\nNecromancer\nDruid\nPaladin\n")
    sleep(0.5)
    pickClass()
  elif classTxt == "/help Swordsman":
    print("Swordsman:\nStarting Stats\nStrength:\nMagic:\nDefence:\nSpeed:\nLuck:\nWeapon Of Choice:\nFor More Information Open the Class Tree In the Download Folder")
    pickClass()
  elif classTxt == "/help Rouge":
    print("Rouge:\nStarting Stats\nStrength:\nMagic:\nDefence:\nSpeed:\nLuck:\nWeapon Of Choice:\nFor More Information Open the Class Tree In the Download Folder")
    pickClass()
  elif classTxt == "/help Wizard":
    print("Wizard:\nStarting Stats\nStrength:\nMagic:\nDefence:\nSpeed:\nLuck:\nWeapon Of Choice:\nFor More Information Open the Class Tree In the Download Folder")
    pickClass()
  elif classTxt == "/help Tank":
    print("Swordsman:\nStarting Stats\nStrength:\nMagic:\nDefence:\nSpeed:\nLuck:\nWeapon Of Choice:\nFor More Information Open the Class Tree In the Download Folder")
    pickClass()
  elif classTxt == "/help Healer":
    print("Swordsman:\nStarting Stats\nStrength:\nMagic:\nDefence:\nSpeed:\nLuck:\nWeapon Of Choice:\nFor More Information Open the Class Tree In the Download Folder")
    pickClass()
  elif classTxt == "/help Ranger":
    print("Swordsman:\nStarting Stats\nStrength:\nMagic:\nDefence:\nSpeed:\nLuck:\nWeapon Of Choice:\nFor More Information Open the Class Tree In the Download Folder")
    pickClass()
  elif classTxt == "Swordsman":
    selfPlayer.Class = "Swordsman"
    return
  elif classTxt == "Rouge": 
    selfPlayer.Class = "Rouge"
    return
  elif classTxt == "Wizard": 
    selfPlayer.Class = "Wizard"
    return
  elif classTxt == "Healer": 
    selfPlayer.Class = "Healer"
    return
  elif classTxt == "Tank":
    selfPlayer.Class = "Tank"
    return
  elif classTxt == "Ranger":
    selfPlayer.Class = "Ranger"
    return
  else:
    print("Not Valid Command Or Class")
    pickClass()

def increaseStats(stre,mag,dfc,spd,luck):
  print("Your Stats Have Changed!");
  nStr = selfPlayer.Str + stre
  nMag = selfPlayer.Mag + mag
  nDef = selfPlayer.Def + dfc
  nSpd = selfPlayer.Spd + spd
  nLuck = selfPlayer.Luck + luck
  print("Strength: %d -> %d ") % (selfPlayer.Str, nStr)
  print("Magic: %d -> %d ") % (selfPlayer.Mag, nMag)
  print("Defence: %d -> %d ") % (selfPlayer.Def, nDef)
  print("Speed: %d -> %d ") % (selfPlayer.Spd, nSpd)
  print("Luck: %d -> %d ") % (selfPlayer.Luck, nLuck)
  selfPlayer.Str = selfPlayer.Str + stre
  selfPlayer.Mag = selfPlayer.Mag + mag
  selfPlayer.Def = selfPlayer.Def + dfc
  selfPlayer.Spd = selfPlayer.Spd + spd
  selfPlayer.Luck = selfPlayer.Luck + luck
  return

def selfStats():
  print("Strength: ");print(selfPlayer.Str)
  print("Magic: ");print(selfPlayer.Mag)
  print("Defence: ");print(selfPlayer.Def)
  print("Speed: ");print(selfPlayer.Spd)
  print("Luck ");print(selfPlayer.Luck)
  txtInput()

def levelUp():
  print("You Are Now Level %s!" % selfPlayer.LevelUp())
  determineIncrease()
  increaseStats(addStr,addMag,addDfc,addSpd,addLuck)
  print("You have %s Skill Points type /upStats to increase stats" % skillPoints)
  txtInput()
  
def determineIncrease():
  selfPlayer.setStatInc()
  return

#THIS IS TEXT INPUT --------------------------------------------------------------
def txtInput():
  if selfPlayer.position[5:9] == [0,0,0,0]:
    print("How did you end up on this position?")
#Right
  elif selfPlayer.position[5:9] == [0,0,0,1]:
    print("You Can Move: Right")
#Up Down
  elif selfPlayer.position[5:9] == [1,1,0,0]:
    print("You Can Move: Up & Down")
#Up Left
  elif selfPlayer.position[5:9] == [1,0,1,0]:
    print("You Can Move: Up & Left")
#Up Right
  elif selfPlayer.position[5:9] == [1,0,0,1]:
    print("You Can Move: Up & Right")
#Up Down Left
  elif selfPlayer.position[5:9] == [1,1,1,0]:
    print("You Can Move: Up, Down, & Left")
#Up Down Right
  elif selfPlayer.position[5:9] == [1,1,0,1]:
    print("You Can Move: Up, Down, & Right")
#Up Left Right
  elif selfPlayer.position[5:9] == [1,0,1,1]:
    print("You Can Move: Up, Left & Right")
#Down Left Right
  elif selfPlayer.position[5:9] == [1,0,1,1]:
    print("You Can Move: Down, Left, & Right")
#Down Left
  elif selfPlayer.position[5:9] == [0,1,1,0]:
    print("You Can Move: Down & Left")
#Down Right
  elif selfPlayer.position[5:9] == [0,1,0,1]:
    print("You Can Move: Down & Right")
#Right Left
  elif selfPlayer.position[5:9] == [0,0,1,1]:
    print("You Can Move: Left & Right")
#Up Down Left Right
  elif selfPlayer.position[5:9] == [0,0,1,1]:
    print("You Can Move: Up, Down, Left, & Right")
#Error
  else:
    print("Ok this was my fault")
  inpt = input(">")
  if inpt == "/upStats":
    upStats()
  elif inpt == "/debug mode":
    print("Debug Mode Activated")
  elif inpt == '/save':
    num = input('Where Would You Like To Save It?: ')
    f = open('save'+num+'.txt','w')
    #Dont Forget To Add Location To Here Once It Works
    savingThing = [selfPlayer.name,selfPlayer.race,selfPlayer.Class,selfPlayer.Str,selfPlayer.Mag,selfPlayer.Def,selfPlayer.Spd,selfPlayer.Luck,]
    f.write(str(savingThing))
    f.close()
#Movement
  elif inpt == 'U':
    if selfPlayer.position[5] == 1:
      playerMove("U")
    else:
      print("You cannot Go Up")
      txtInput()

  elif inpt == 'D':
    if selfPlayer.position[6] == 1:
      playerMove("D")
    else:
      print("You cannot Go Down")
      txtInput()

  elif inpt == 'L':
    if selfPlayer .position[7] == 1:
      playerMove("L")
    else:
      print("You cannot Go Left")
      txtInput()

  elif inpt == 'R':
    if selfPlayer.position[8] == 1:
      playerMove("R")
    else:
      print("You cannot Go Right")
      txtInput()

  else:
    print(inpt)
    txtInput()

def checkMovement(cordCodes):
  print(cordCodes[5:9])

def playerMove(d):
  position = selfPlayer.pos
  if d == 'U':
    selfPlayer.setPosition('u',position)
  if d == 'D':
    selfPlayer.setPosition('d',position)
  if d == 'L':
    selfPlayer.setPosition('l',position)
  if d == 'R':
    selfPlayer.setPosition('r',position)
  

def setPlayerForest(e):
  if e == 1:
    return selfPlayer.setLocation(Forest,Forest.allForest[5],5)
  elif e == 2:
    return selfPlayer.setLocation(Forest,Forest.allForest[45],45)
  elif e == 3:
    return selfPlayer.setLocation(Forest,Forest.allForest[55],55)
  elif e == 4:
    return selfPlayer.setLocation(Forest,Forest.allForest[115],115)
  else:
      print("Error No Entrance Defined in Parapeters")
        
start()
pickClass()
determineIncrease()
txtInput()
