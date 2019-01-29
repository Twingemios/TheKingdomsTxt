import os
import random
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
    num = input("Which Save Would You Like To Load?: ")
    f = open('save'+num+'.txt','r')
    fileText = f.read()
    fileList = eval(fileText)
    global selfPlayer
    selfPlayer = Character(fileList[0],fileList[1],fileList[2],fileList[3],fileList[4],fileList[5],fileList[6],fileList[7],fileList[8],fileList[9])
    selfPlayer.setPos = fileList[10]
    selfPlayer.position = fileList[11]
    selfPlayer.currentHP = fileList[13]
    selfPlayer.currentHP = fileList[14]
    if fileList[12] == 'Forest':
      selfPlayer.Location = Forest
    else:
      print("Crap")
    txtInput()
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
      selfPlayer = Character(nameInput,raceInput,None,10,10,1,1,1,1,1)
      selfPlayer.maxHP = 10
      selfPlayer.maxMana = 10
      selfPlayer.currentHP = 10
      selfPlayer.currentMana = 10
      global skillPoints
      skillPoints = 0
      pickClass()
    else:
      print("Invalid Class Please Try Again")
      newCharacter()
 


class Character:
  def __init__(self, name, race, Class, HPMax, ManaMax, Str, Mag, Def, Spd, Luck):
    self.name = name
    self.race = race
    self.Class = Class
    self.HPMax = HPMax
    self.ManaMax = ManaMax
    self.Str = Str
    self.Mag = Mag
    self.Def = Def
    self.Spd = Spd
    self.Luck = Luck
    self.lvl = 1
    self.XP = 0
    self.Location = None
    self.position = None
    self.setPos = None
    self.magicAttacks = []
    self.nonMAttacks = []
    self.magicAttacksName = []
    self.nonMAttacksName = []
  def LevelUp(self):
    self.lvl = self.lvl + 1
    return self.lvl
  def setStatInc(self):
    #Class Increase
    if self.Class == "Swordsman":
      self.classStats = [3,1,2,2,1] 
    elif self.Class == "Rouge":
      self.classStats = [1,2,1,3,2]
    elif self.Class == "Wizard":
      self.classStats = [1,3,1,2,2]
    elif self.Class == "Healer":
      self.classStats = [1,2,1,2,2]
    elif self.Class == "Tank":
      self.classStats = [2,1,3,2,1]
    elif self.Class == "Ranger":
      self.classStats = [2,1,1,2,3]
    else:
      print("ERROR:\nClass is Invalid")
    #Race Increase
    if self.race == "Sc":
      self.startStats = list(map(operator.add,self.classStats,[0,1,2,0,0]))
    elif self.race == "Elf":
      self.startStats = list(map(operator.add,self.classStats,[2,0,0,1,0]))
    elif self.race == "Dark Elf": 
      self.startStats = list(map(operator.add,self.classStats,[0,0,0,2,1]))
    elif self.race == "Khajit":
      self.startStats = list(map(operator.add,self.classStats,[1,0,1,0,1]))
    elif self.race == "Dragonborn":
      self.startStats = list(map(operator.add,self.classStats,[0,2,1,0,0]))
    elif self.race == "Demon":
      self.startStats = list(map(operator.add,self.classStats,[0,1.0,0,2]))
    else:
      print("\nERROR:\nRace is Invalid Please Restart\n")
      sleep(10000000)
    self.Str = self.classStats[0]
    self.Mag = self.classStats[1]
    self.Def = self.classStats[2]
    self.Spd = self.classStats[3]
    self.Luck = self.classStats[4]
    print("OOF")
    return self.classStats
  def setLocation(self, location, setPos):
    self.Location = location
    self.setPos = setPos
    selfPlayer.setPosition(None, setPos)
  def setPosition(self,d,setPosition):
    if d == 'u':
        temp = self.setPos - 11
        self.position = Forest.allForest[temp]
        self.setPos = temp
        print("You are Now at %s" % (temp))
    elif d == 'd':
        temp = self.setPos + 11
        self.position = Forest.allForest[temp]
        self.setPos = temp
        print("You are Now at %s" % (temp))
    elif d == 'l':
        temp = self.setPos - 1
        self.position = Forest.allForest[temp]
        self.setPos = temp
        print("You are Now at %s" % (temp))
    elif d == 'r':
        temp = self.setPos + 1
        self.position = Forest.allForest[temp]
        self.setPos = temp
        print("You are Now at %s" % (temp))
    else:
      self.position = Forest.allForest[setPosition]
      print(self.position)
    if Forest.allForest[self.setPos][0] != '+' or Forest.allForest[self.setPos][0] != '@':
          locationEvent(Forest.allForest[self.setPos][0],Forest.allForest[self.setPos][1:3])
    else:
      txtInput()
  def addAttack(self, t, ID, name):
    if t == 'M':
      self.magicAttacks.append(ID)
      self.magicAttacksName.append(name)
    elif t == 'N':
      self.nonMAttacks.append(ID)
      self.nonMAttacksName.append(name)
      return(self.nonMAttacks)
    else:
      print("Error: Not a Valid Type")
  def showAttacks(self):
    inpt = input('What Would You Like To Do?\nAttack\nMagic\nItems\nRun\n>')
    if inpt == 'Attack' or inpt == 'attack':
      print("You Can Use %s" % (str(selfPlayer.nonMAttacksName)))
      inpt2 = input()
      for i in range(len(self.nonMAttacks)):
        if inpt2 == self.nonMAttacksName[i]:
          print("Sucess!")
          playerAttack(self.nonMAttacks)
        if inpt2 == 'Back'():
          self.showAttacks()
      print("No Valid Attacks")
  
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
    selfPlayer.setStatInc()
    setPlayerForest(4)
    txtInput()
    return
  elif classTxt == "Rouge": 
    selfPlayer.Class = "Rouge"
    selfPlayer.setStatInc()
    setPlayerForest(4)
    txtInput()
  elif classTxt == "Wizard": 
    selfPlayer.Class = "Wizard"
    selfPlayer.setStatInc()
    setPlayerForest(4)
    txtInput()
  elif classTxt == "Healer": 
    selfPlayer.Class = "Healer"
    selfPlayer.setStatInc()
    setPlayerForest(4)
  elif classTxt == "Tank":
    selfPlayer.Class = "Tank"
    selfPlayer.setStatInc()
    setPlayerForest(4)
    txtInput()
  elif classTxt == "Ranger":
    selfPlayer.Class = "Ranger"
    selfPlayer.setStatInc()
    setPlayerForest(4)
    txtInput()
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
  return determineIncrease()

def selfStats():
  print("Strength: ");print(selfPlayer.Str)
  print("Magic: ");print(selfPlayer.Mag)
  print("Defence: ");print(selfPlayer.Def)
  print("Speed: ");print(selfPlayer.Spd)
  print("Luck ");print(selfPlayer.Luck)
  txtInput()

def testLvlUp():
  xpNeeded = [None,None,100,250,500,1000]
  neededXP = xpNeeded[selfPlayer.Lvl]
  if selfPlayer.XP == neededXP
    levelUp()
  else:
    return:

def levelUp():
  selfPlayer.lvl = selfPlayer.lvl + 1
  statIncreases[[],]
  increaseStats(statIncreases[selfPlayer.lvl])
  
def determineIncrease():
  return selfPlayer.setStatInc()
  return

#THIS IS TEXT INPUT --------------------------------------------------------------
def txtInput():
  if selfPlayer.position[5:10] == [0,0,0,0]:
    print("How did you end up on this position?")
#Up
  elif selfPlayer.position[5:10] == [1,0,0,0]:
    print("You Can Move: Up")
#Down
  elif selfPlayer.position[5:10] == [0,1,0,0]:
    print("You Can Move: Down")
#Left
  elif selfPlayer.position[5:10] == [0,0,1,0]:
    print("You Can Move: Left")
#Right
  elif selfPlayer.position[5:10] == [0,0,0,1]:
    print("You Can Move: Right")
#Up Down
  elif selfPlayer.position[5:10] == [1,1,0,0]:
    print("You Can Move: Up & Down")
#Up Left
  elif selfPlayer.position[5:10] == [1,0,1,0]:
    print("You Can Move: Up & Left")
#Up Right
  elif selfPlayer.position[5:10] == [1,0,0,1]:
    print("You Can Move: Up & Right")
#Up Down Left
  elif selfPlayer.position[5:10] == [1,1,1,0]:
    print("You Can Move: Up, Down, & Left")
#Up Down Right
  elif selfPlayer.position[5:10] == [1,1,0,1]:
    print("You Can Move: Up, Down, & Right")
#Up Left Right
  elif selfPlayer.position[5:10] == [1,0,1,1]:
    print("You Can Move: Up, Left & Right")
#Down Left Right
  elif selfPlayer.position[5:10] == [1,0,1,1]:
    print("You Can Move: Down, Left, & Right")
#Down Left
  elif selfPlayer.position[5:10] == [0,1,1,0]:
    print("You Can Move: Down & Left")
#Down Right
  elif selfPlayer.position[5:10] == [0,1,0,1]:
    print("You Can Move: Down & Right")
#Right Left
  elif selfPlayer.position[5:10] == [0,0,1,1]:
    print("You Can Move: Left & Right")
#Up Down Left Right
  elif selfPlayer.position[5:10] == [1,1,1,1]:
    print("You Can Move: Up, Down, Left, & Right")
#Error
  else:
    print("Ok this was my fault")
  inpt = input(">")
  if inpt == "/upStats":
    upStats()
  elif inpt == "/debug mode":
    print("Debug Mode Activated")
#Saving
  elif inpt == '/save':
    num = input('Where Would You Like To Save It?: ')
    f = open('save'+num+'.txt','w')
    #Dont Forget To Add Location To Here Once It Works
    if selfPlayer.Location == Forest:
      welp = 'Forest'
    else:
      print("Someone Forgot To Put In a New Location!")
    savingThing = [selfPlayer.name,selfPlayer.race,selfPlayer.Class,selfPlayer.maxHP,selfPlayer.maxMana,selfPlayer.Str,selfPlayer.Mag,selfPlayer.Def,selfPlayer.Spd,selfPlayer.Luck,selfPlayer.setPos,selfPlayer.position,welp,selfPlayer.currentHP,selfPlayer.currentMana]
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
    if selfPlayer.position[7] == 1:
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
#Movement--------------------------------------------------------------------------------
def checkMovement(cordCodes):
  print(cordCodes[5:10])

def playerMove(d):
  if d == 'U':
    selfPlayer.setPosition('u',None)
  if d == 'D':
    selfPlayer.setPosition('d',None)
  if d == 'L':
    selfPlayer.setPosition('l',None)
  if d == 'R':
    selfPlayer.setPosition('r',None)
  

def setPlayerForest(e):
  if e == 1:
    return selfPlayer.setLocation(Forest,5)
  elif e == 2:
    return selfPlayer.setLocation(Forest,45)
  elif e == 3:
    return selfPlayer.setLocation(Forest,55)
  elif e == 4:
    return selfPlayer.setLocation(Forest,115)
  else:
      print("Error No Entrance Defined in Parapeters")

def locationEvent(tType,eID):
  if selfPlayer.Location == Forest:
    #if eID == [0,1]:
      #print("Event1")
    #elif eID == [0,2]:
      #print("Event2")
    if tType == '$':
      print("$")
    elif tType == '#':
      print("#")
      findEnemy(eID)
    elif tType == '!':
      print("!")
    elif tType == '@':
      print("@")
  else:
    print("We are out of Maps")
  txtInput()

#Combat Stuff------------------------------------------------------------------------------
class Enemy:
  def __init__(self,Str,Mag,Def,Spd,Luck,HPMax,Name,DropID,Atk1,Atk2,Atk3,Atk4,Atk5,Exp,Lvl):
    self.Str = Str
    self.Mag = Mag
    self.Def = Def
    self.Spd = Spd
    self.Luck = Luck
    self.HPMax = HPMax
    self.Name = Name
    self.DropID = DropID
    self.HP = HPMax
    self.XP = Exp
    self.Lvl = Lvl
    #Attacks
    self.Atk1 = Atk1
    self.Atk2 = Atk2
    self.Atk3 = Atk3
    self.Atk4 = Atk4
    self.Atk5 = Atk5
  def attack(self):
    atkList = [self.Atk1,self.Atk2,self.Atk3,self.Atk4,self.Atk5] 
    currentAttack = random.choice(atkList)
    
    
#1 Type (S - Strength|M - Magic|Def - D|E = Speed|L = Luck)
#2 Power (Base Damage)
#3 EffectID ()
#4 Magic or Non Magic
#5 Magic Cost
    
def getAttack(ID):
  if ID == ['1']:
    return([['S'],1,'00','N',0])
  if ID == ['2']:
    return([['L'],1,'00','N',0])
  if ID == ['3']:
    return([['M'],1,'00','M',5])
  if ID == ['4']:
    return([['E'],1,'00','N',0])
  if ID == ['5']:
    return([['D'],1,'00','N',0])
  else:
    print(ID)
    print("Error: Too many Attacks")

def playerAttack(ID):
  atkStats = getAttack(ID)
  print(atkStats)
  if atkStats[0] == ['S']:
    damage = int(atkStats[1])+int(selfPlayer.Str)
    currentEnemy.HP = currentEnemy.HP - damage
    if currentEnemy.HP < 1:
      sweetVictory()
      txtInput()
    else:
      print(currentEnemy.HP)
      #enemyAttack()
  elif atkStats[0] == ['L']:
    damage = int(atkStats[1])+int(selfPlayer.Luck)
    currentEnemy.HP = currentEnemy.HP - damage
    if currentEnemy.HP < 1:
      sweetVictory()
      txtInput()
    else:
      enemyAttack()
  elif atkStats[0] == ['M']:
    damage = int(atkStats[1])+int(selfPlayer.Mag)
    currentEnemy.HP = currentEnemy.HP - damage
    if currentEnemy.HP < 1:
      sweetVictory()
      txtInput()
    else:
      enemyAttack()
  elif atkStats[0] == ['E']:
    damage = int(atkStats[1])+int(selfPlayer.Spd)
    currentEnemy.HP = currentEnemy.HP - damage
    if currentEnemy.HP < 1:
      sweetVictory()
      txtInput()
    else:
      enemyAttack()
  elif atkStats[0] == ['D']:
    damage = int(atkStats[1])+int(selfPlayer.Def)
    currentEnemy.HP = currentEnemy.HP - damage
    if currentEnemy.HP < 1:
      sweetVictory()
      txtInput()
    else:
      enemyAttack()
  else:
    print("Python Sucks")

def enemyAttack():
  atacks = [currentEnemy.Atk1,currentEnemy.Atk2,currentEnemy.Atk3,currentEnemy.Atk4,currentEnemy.Atk5]
  enemysAttack = random.choice(attacks)
  eAttackStats = getAttack(enemysAttack)
  if eAttackStats[0] == ['S']:
    damage = int(atkStats[1])+int(selfPlayer.Str)
    selfPlayer.HP = selfPlayer.HP - damage
    if selfPLayer.HP < 1:
      gameOver()
    else:
      selfPlayer.showAttacks()
  elif eAttackStats[0] == ['M']:
    damage = int(atkStats[1])+int(selfPlayer.Mag)
    if selfPLayer.HP < 1:
      gameOver()
    else:
      selfPlayer.showAttacks()
    selfPlayer.HP = selfPlayer.HP - damage
  elif eAttackStats[0] == ['E']:
    damage = int(atkStats[1])+int(selfPlayer.Spd)
    selfPlayer.HP = selfPlayer.HP - damage
    if selfPLayer.HP < 1:
      gameOver()
    else:
      selfPlayer.showAttacks()
  elif eAttackStats[0] == ['D']:
    damage = int(atkStats[1])+int(selfPlayer.Def)
    selfPlayer.HP = selfPlayer.HP - damage
    if selfPLayer.HP < 1:
      gameOver()
    else:
      selfPlayer.showAttacks()
  elif eAttackStats[0] == ['L']:
    damage = int(atkStats[1])+int(selfPlayer.Luck)
    selfPlayer.HP = selfPlayer.HP - damage
    if selfPLayer.HP < 1:
      gameOver()
    else:
      selfPlayer.showAttacks()
  else:
    print("Honestly I Should Have Used C++ Or Flash")

def findEnemy(eID):
  if selfPlayer.Location == Forest:
    eRNG = random.choice(Forest.enemiesList)
    if eRNG == None:
      return
    else:
      global currentEnemy
      currentEnemy = Enemy(eRNG[0],eRNG[1],eRNG[2],eRNG[3],eRNG[4],eRNG[5],eRNG[6],eRNG[7],eRNG[8],eRNG[9],eRNG[10],eRNG[11],eRNG[12],eRNG[13],eRNG[14])
      startCombat()

def startCombat():
  if selfPlayer.Spd < currentEnemy.Spd:
    enemyAttack()
  else:
    selfPlayer.showAttacks()

def test():
  selfPlayer.addAttack('N', '1', 'Punch')
  print("Yes1")
  findEnemy(1)
  print("Yes2")
  selfPlayer.showAttacks()
  print("Yes3")

def sweetVictory():
  selfPlayer.XP = selfPlayer.XP + currentEnemy.XP
  testLvlUp()


start()
