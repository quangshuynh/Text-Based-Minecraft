# imports
from replit import clear # clear() to clear console
from time import sleep # sleep(x) to pause program
from getkey import getkey # getkey() to get pressed
from getkey import keys # used to compare getkey()
from random import randint # generate random number
from random import choices # used for weighted choices
from random import choice # for Quang's biomes
from math import ceil # round up no matter what
# import os
# import pickle # save files

# player attributes - inventory, health, hunger, current world
currentWorld = "overworld" # changed to nether or end
netherUnlocked = False
endUnlocked = False
global playerDied
global playerHealth
playerDied = False
playerHealth = 20
playerHunger = 20
experience = 0

# Biomes
biomes = ['Plains Biome', 'Forest Biome', 'Swamp Biome', 'Desert Biome', 'Mesa Plateau Biome', 'Jungle Biome', 'Savanna Biome', 'Extreme Hills Biome', 'Taiga Biome']

# make sure that inventory has 32 slots ( +4 slots for armor only) - after project is due
playerInventory = {
  # EACH FOLLOWING SECTION HAS ITS OWN CRAFTING LIST
  # tools and armor
  "sword": 'none',
  "pickaxe": 'none',
  "axe": 'none',
  "shovel": 'none',
  "helmet": 'none',
  "chestplate": 'none',
  "leggings": 'none',
  "boots": 'none',
  "bow": 0,
  "arrow": 0,
  # diamond tools named to get around netherite error
    # "diamondSword": 0,
    # "diamondPickaxe": 0,
    # "diamondAxe": 0,
    # "diamondShovel": 0,
    # "diamondHelmet": 0,
    # "diamondChestplate": 0,
    # "diamondLeggings": 0,
    # "diamondBoots": 0,
  # essential items and quantity - will be added later
  "dirt": 0,
  "sapling": 0,
  "wood_log": 0,
  "wood_plank": 0,
  "stick": 0,
  "leather": 0,
  "stone": 0,
  "cobblestone": 0,
  "coal": 0,
  "charcoal": 0,
  "emerald": 0,
  "iron_ore": 0,
  "iron_ingot": 0,
  "gold_ore": 0,
  "gold_ingot": 0,
  "lapis_lazuli": 0,
  "diamond": 0,
  "obsidian": 0,
  "ancient_debris": 0,
  "netherite_scrap": 0,
  "netherite_ingot": 0,
  "ender_pearls": 0,
  "gravel": 0,
  "flint": 0,
  "granite": 0,
  "furnace": 0,
  "sand": 0,
  "glass": 0,
  "match": 0,
  "chest": 0,
  "bucket": 0,
  "enchantment_table": 0,
  "book": 0,
  "paper": 0,
  "sugar_cane": 0,
  # food
  "raw_beef": 0,
  "cooked_beef": 0,
  "raw_chicken": 0,
  "cooked_chicken": 0,
  "raw_mutton": 0,
  "cooked_mutton": 0,
  "raw_porkchop": 0,
  "cooked_porkchop": 0,
  "raw_salmon": 0,
  "cooked_salmon": 0,
  "rotten_flesh": 0,
  # nether items
  "blaze_rod": 0,
  "blaze_powder": 0
  # end items
  
}
craftingTools = [
  # Wood Tools
  [["wooden_pickaxe"], ["stick", "stick", "wood_plank", "wood_plank", "wood_plank"]],
  [["wooden_axe"], ["stick", "stick", "wood_plank", "wood_plank", "wood_plank"]],
  [["wooden_sword"], ["stick", "wood_plank", "wood_plank"]],
  [["wooden_shovel"], ["stick", "stick", "wood_plank"]],
  # Stone Tools
  [["stone_pickaxe"], ["stick", "stick", "cobblestone", "cobblestone", "cobblestone"]],
  [["stone_axe"], ["stick", "stick", "cobblestone", "cobblestone", "cobblestone"]],
  [["stone_sword"], ["stick", "cobblestone", "cobblestone"]],
  [["stone_shovel"], ["stick", "stick", "cobblestone"]],
  # Iron Tools
  [["iron_pickaxe"], ["stick", "stick", "iron_ingot", "iron_ingot", "iron_ingot"]],
  [["iron_axe"], ["stick", "stick", "iron_ingot", "iron_ingot", "iron_ingot"]],
  [["iron_sword"], ["stick", "iron_ingot", "iron_ingot"]],
  [["iron_shovel"], ["stick", "stick", "iron_ingot"]],
  # Golden Tools
  [["gold_pickaxe"], ["stick", "stick", "gold_ingot", "gold_ingot", "gold_ingot"]],
  [["gold_axe"], ["stick", "stick", "gold_ingot", "gold_ingot", "gold_ingot"]],
  [["gold_sword"], ["stick", "gold_ingot", "gold_ingot"]],
  [["gold_shovel"], ["stick", "stick", "gold_ingot"]],
  # Diamond Tools
  [["diamond_pickaxe"], ["stick", "stick", "diamond", "diamond", "diamond"]],
  [["diamond_axe"], ["stick", "stick", "diamond", "diamond", "diamond"]],
  [["diamond_sword"], ["stick", "diamond", "diamond"]],
  [["diamond_shovel"], ["stick", "stick", "diamond"]]
  # Netherite Tools
  # [["netherite_pickaxe"], ["diamondPickaxe", "netherite_ingot"]],
  # [["netherite_axe"], ["diamondAxe", "netherite_ingot"]],
  # [["netherite_sword"], ["diamondSword", "netherite_ingot"]],
  # [["netherite_shovel"], ["diamondShovel", "netherite_ingot"]]
]
craftingArmor = [
  # Leather Armor
  [["leather_helmet"], ["leather", "leather", "leather", "leather", "leather"]],
  [["leather_chestplate"], ["leather", "leather", "leather", "leather", "leather", "leather", "leather", "leather"]],
  [["leather_leggings"], ["leather", "leather", "leather", "leather", "leather", "leather", "leather"]],
  [["leather_boots"], ["leather", "leather", "leather", "leather"]],
  # Iron Armor
  [["iron_helmet"], ["iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot"]],
  [["iron_chestplate"], ["iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot"]],
  [["iron_leggings"], ["iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot"]],
  [["iron_boots"], ["iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot"]],
  # Golden Armor
  [["gold_helmet"], ["gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot"]],
  [["gold_chestplte"], ["gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot"]],
  [["gold_leggings"], ["gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot"]],
  [["gold_boots"], ["gold_ingot", "gold_ingot", "gold_ingot", "gold_ingot"]],
  # Diamond Armor
  [["diamond_helmet"], ["diamond", "diamond", "diamond", "diamond", "diamond"]],
  [["diamond_chestplate"], ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]],
  [["diamond_leggings"], ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]],
  [["diamond_boots"], ["diamond", "diamond", "diamond", "diamond"]]
  # Netherite Armor
  # [["netherite_helmet"], ["diamondHelmet", "netherite_ingot"]],
  # [["netherite_chestplate"], ["diamondChestplate", "netherite_ingot"]],
  # [["netherite_leggings"], ["diamondLeggings", "netherite_ingot"]],
  # [["netherite_boots"], ["diamondBoots", "netherite_ingot"]]
]
overworldItems = [
  [["wood_plank"], ["wood_log"]],
  [["stick"], ["wood_plank", "wood_plank"]],
  [["furnace"], ["cobblestone", "cobblestone", "cobblestone", "cobblestone", "cobblestone", "cobblestone", "cobblestone", "cobblestone"]],
  [["match"], ["coal", "stick"]],
  [["chest"], ["wood_plank", "wood_plank", "wood_plank", "wood_plank", "wood_plank", "wood_plank", "wood_plank", "wood_plank"]],
  [["bucket"], ["iron_ingot", "iron_ingot", "iron_ingot"]],
  [["enchantment_table"], ["obsidian", "obsidian", "obsidian", "obsidian", "diamond", "diamond", "book"]],
  [["book"], ["paper", "paper", "paper", "leather"]],
  [["paper"], ["sugar_cane", "sugar_cane", "sugar_cane"]]
  # [["iron_block"], ["iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot", "iron_ingot"]],
  # [["anvil"]],
  # [["iron_ingot"], ["iron_block"]]
]
netherItems = [
  [["netherPortal"], ["obsidian", "obsidian", "obsidian", "obsidian", "obsidian", "obsidian", "obsidian", "obsidian", "obsidian", "obsidian"]],
  [["brewing_stand"], ["cobblestone", "cobblestone", "cobblestone", "blaze_rod"]],
  [["blaze_powder"], ["blaze_rod"]]
]
endItems = []
craftingListsCombined = [craftingTools, craftingArmor, overworldItems]

# Loading screen
def returnToHome():
  sleep(0.5)
  clear()
  print("\n[ Loading ]\n\nDo not press any keys\n[---------------              ] 47%")
  sleep(1)
  clear()
  print("\n[ Loading ]\n\nDo not press any keys\n[-----------------------------] 100%")
  sleep(0.8)
  clear()

# used to create key to be used in functions
key = 0

# main function that displays when no action provided yet
def home():
  clear()
  global playerHealth
  playerHealth = 20
  print("\n[   Action menu   ]" + '\nXP: ', str(experience) + "\n\nHold [Q] to gather wood\nHold [W] to go mining\nPress [I] to open inventory\nPress [A] to craft\nPress [S] to smelt\n")
  # print("Enchanting is currently unavailable.")

# Inventory
def inventory():
  clear()
  print("[   Inventory   ]\n")
  print("Sword: " + playerInventory["sword"])
  print("Pickaxe: " + playerInventory["pickaxe"])
  print("Axe: " + playerInventory["axe"])
  print("Shovel: " + playerInventory["shovel"])
  print("\nHelmet: " + playerInventory["helmet"])
  print("Chestplate: " + playerInventory["chestplate"])
  print("Leggings: " + playerInventory["leggings"])
  print("Boots: " + playerInventory["boots"] + '\n')
  for material in playerInventory:
    if material != 'sword' and material != 'axe' and material != 'pickaxe' and material != 'shovel' and material != 'helmet' and material != 'chestplate' and material != 'leggings' and material != 'boots':
      if playerInventory[material] > 0:
        print(material + ": " + str(playerInventory[material]))
  print("\nPress [SPACE] to exit.")
  # wait for user to exit
  while True:
    key = getkey()
    if key == keys.SPACE:
      break
      
def combat():
  # DON'T FORGET ITEM DROPS
  clear() 
  # get average level - equal to rating of player's gear
  numberOfItems = 0
  addedTotal = 0
  for i in [playerInventory["sword"], playerInventory["pickaxe"], playerInventory["axe"], playerInventory["shovel"], playerInventory["helmet"], playerInventory["chestplate"], playerInventory["leggings"], playerInventory["boots"]]:
    numberOfItems += 1
    if i == "wooden":
      addedTotal += 3
    elif i == "leather":
      addedTotal += 3
    elif i == "stone":
      addedTotal += 5
    elif i == "iron":
      addedTotal += 7
    elif i == "golden":
      addedTotal += 6
    elif i == "diamond":
      addedTotal += 8
    elif i == "netherite":
      addedTotal += 9
  average = addedTotal/numberOfItems
  # overworld combat
  if playerInventory["sword"] != "none" and currentWorld == "overworld" and average > 1:
    zombie = {
      "name": "Zombie",
      "health": 20,
      "damage": 0, # damage changes by average
      "attackSpeed": 1.8,
      "attackCounter": 0,
      "drop": ["rotten_flesh"], # 0-2
      "XP": 5
    }
    creeper = {
      "name": "Creeper",
      "health": 20,
      "damage": "22",
      "attackSpeed": 1.5, # can only attack once
      "attackCounter": 0,
      "drop": ["gunpowder"], # 0-2
      "XP": 5
    }
    skeleton = {
      "name": "Skeleton",
      "health": 20,
      "damage": 3, # constant attack
      "attackSpeed": 2,
      "attackCounter": 0,
      "drop": ["bone", "arrow"], # 0-2 each
      "XP": 5
    }
    if average <= 2.5: # wooden/leather gear - ez
      zombie["damage"] = 2
      opponents = [zombie]
    elif average <= 4.5: # stone tools
      zombie["damage"] = 3
      opponents = [zombie, skeleton]
    elif average <= 5.5: # iron/golden gear - normal
      zombie["damage"] = 3
      opponents = [zombie, zombie, skeleton]
    elif average <= 7: # diamond gear - hard
      zombie["damage"] = 4
      opponents = [zombie, zombie, skeleton, skeleton]
    elif average <= 8.5: # netherite gear
      zombie["damage"] = 5
      opponents = [zombie, zombie, zombie, skeleton, skeleton]
    playerAttackSpeed = 1.6
    playerAttackCounter = 0
    playerArmor = 0
    if playerInventory["helmet"] == "leather":
      playerArmor += 1
    elif playerInventory["helmet"] == "gold" or playerInventory["helmet"] == "iron":
      playerArmor += 2
    elif playerInventory["helmet"] == "diamond" or playerInventory["helmet"] == "netherite":
      playerArmor += 3
    if playerInventory["chestplate"] == "leather":
      playerArmor += 2
    elif playerInventory["chestplate"] == "gold":
      playerArmor += 5
    elif playerInventory["chestplate"] == "iron":
      playerArmor += 6
    elif playerInventory["chestplate"] == "diamond" or playerInventory["chestplate"] == "netherite":
      playerArmor += 8
    if playerInventory["leggings"] == "leather":
      playerArmor += 2
    elif playerInventory["leggings"] == "gold":
      playerArmor += 3
    elif playerInventory["leggings"] == 'iron':
      playerArmor += 4
    elif playerInventory["leggings"] == "diamond" or playerInventory["leggings"] == "netherite":
      playerArmor += 6
    if playerInventory["boots"] == "leather" or playerInventory["boots"] == "gold": 
      playerArmor += 1
    elif playerInventory["boots"] == "iron":
      playerArmor += 2
    elif playerInventory["boots"] == "diamond" or playerInventory['boots'] == "netherite":
      playerArmor += 3
    playerArmor = ceil(playerArmor/6)
    if playerInventory["sword"] == "wooden":
      playerDamage = 5
    elif playerInventory["sword"] == "stone":
      playerDamage = 6
    elif playerInventory["sword"] == "iron":
      playerDamage = 7
    elif playerInventory["sword"] == "gold":
      playerDamage = 5
    elif playerInventory["sword"] == "diamond":
      playerDamage = 8
    elif playerInventory["sword"] == "netherite":
      playerDamage = 10
    print("\nYou are in combat!\n")
    sleep(1)
    global playerHealth
    while len(opponents) > 0 and playerHealth > 0:
      if all(playerAttackCounter <= x["attackCounter"] for x in opponents) == True:
        print("\nChoose an opponent to attack:")
        for i in range(0, len(opponents)):
          print(str(i+1)+'.', opponents[i]["name"]+':', str(opponents[i]["health"]), "health")
        print("\n")
        global attackKey
        attackKey = "X"
        while True:
          attackKey = getkey()
          if attackKey == "1" or attackKey == "2" or attackKey == "3" or attackKey == "4" or attackKey == "5" or attackKey == "6" or attackKey == "7" or attackKey == "8" or attackKey == "9":
            attackKey = int(attackKey)
            if attackKey <= len(opponents):
              targetIndex = attackKey - 1
              opponents[targetIndex]["health"] -= playerDamage
              if opponents[targetIndex]["health"] <= 0:
                print("You killed a", opponents[targetIndex]["name"]+'.')
                rand = randint(0, 100)
                for i in opponents[targetIndex]["drop"]:
                  if rand <= 50:
                    playerInventory[i] += 1
                    print("You received 1", i+'.')
                  else:
                    playerInventory[i] += 2
                    print("You received 2", i+'.')
                global experience
                experience += 5
                print("You received 5XP!")
                  
                opponents.pop(targetIndex)
              else:
                print("You dealt", str(playerDamage), "damage!")
              playerAttackCounter += playerAttackSpeed
              sleep(0.5)
              break
      else:
        # get opponent attack
        for i in range(0, len(opponents)):
          if i == 0:
            currentLowest = opponents[i]
            currentLowest["index"] = 0
          elif opponents[i]["attackCounter"] < currentLowest["attackCounter"]:
            currentLowest = opponents[i]
            currentLowest["index"] = i
            
        print("You're opposing", currentLowest["name"], "is attacking!")
        # global playerHealth
        playerHealth -= (currentLowest["damage"] - playerArmor)
        print("You lost", str(currentLowest["damage"] - playerArmor), "health.", "You are at", playerHealth, "health.\n")
        if opponents[currentLowest["index"]]["name"] == "Zombie":
          opponents[currentLowest["index"]]["attackCounter"] += zombie["attackSpeed"]
        elif opponents[currentLowest["index"]]["name"] == "Skeleton":
          opponents[currentLowest["index"]]["attackCounter"] += skeleton["attackSpeed"]
        elif opponents[currentLowest["index"]] == "Creeper":
          opponents[currentLowest["index"]]["attackCounter"] += creeper["attackSpeed"]
        sleep(1)
        
    
    if playerHealth <= 0:
      for key in playerInventory:
        if key != 'sword' and key != "pickaxe" and key != 'axe' and key != 'shovel' and key != 'helmet' and key != 'chestplate' and key != 'leggings' and key != 'boots' and playerInventory[key] > 0:
          playerInventory[key] = 0
      playerInventory["sword"] = "none"
      playerInventory["pickaxe"] = "none"
      playerInventory["axe"] = "none"
      playerInventory["shovel"] = "none"
      playerInventory["helmet"] = "none"
      playerInventory["chestplate"] = "none"
      playerInventory["leggings"] = "none"
      playerInventory["boots"] = "none"
      global playerDied
      playerDied = True
      experience = 0
      print("\nYou died! Press [SPACE] to respawn.\n")
      while True:
        key = getkey()
        if key == keys.SPACE:
          playerHealth = 20
          return
      
  elif currentWorld == "nether":
    pass # revisit later
  elif currentWorld == "end":
    pass # revisit later
    
    
def lumbering():
  clear()
  woodToReceive = 0
  experienceToGain = 0
  while True:
    global experience, key
    key = getkey()
    if key == keys.Q:
      rand = randint(0, 100)
      if rand <= 1:
        combat()
        if playerDied == True:
          playerDied == False
          return
        else: 
          print("\nChopping lumber...\n(Press [SPACE] to stop gathering wood)\n")
      print("\nChopping lumber...\n(Press [SPACE] to stop gathering wood)\n")
      woodToReceive += 1
      experienceToGain += 3
      if playerInventory["axe"] == 'none':
        sleep(2.25)
      elif playerInventory["axe"] == 'wooden':
        sleep(1.5)
      elif playerInventory["axe"] == 'stone':
        sleep(0.75)
      elif playerInventory["axe"] == 'iron':
        sleep(0.5)
      elif playerInventory["axe"] == 'golden':
        sleep(.25)
      elif playerInventory["axe"] == 'diamond':
        sleep(.4)
      elif playerInventory["axe"] == 'netherite':
        sleep(.35)
    else:
      break
      
  woodToReceive = woodToReceive / 2
  woodToReceive = int(woodToReceive)
  playerInventory["wood_log"] = playerInventory["wood_log"] + woodToReceive
  experience += experienceToGain
  clear()
  print("You received " + str(woodToReceive) + " pieces of wood!\nYou gained " + str(experienceToGain) + "XP!")
  sleep(1.75)
  clear()
  returnToHome()

def getCraftableItems(test):
  # Get craftable items
  craftable = []
  # checks for correct input later
  acceptInput = False
  # convert to list
  if len(test) == 2:
    test[1] = [test[1]]
    
  for i in range(0, len(craftingListsCombined)):
    for j in range(0, len(craftingListsCombined[i])):
      itemToCraft = craftingListsCombined[i][j][0]
      itemsNeeded = craftingListsCombined[i][j][1]
      newList = []
      for item in set(itemsNeeded):
        newList.append([item, itemsNeeded.count(item)])
      itemsNeeded = newList
      for x in range(0, len(itemsNeeded)):
        material = itemsNeeded[x][0]
        materialQuantity = itemsNeeded[x][1]
        # check if craftable
        if playerInventory[material] >= materialQuantity and material == itemsNeeded[len(itemsNeeded) - 1][0]:
          craftable.append(itemToCraft)
        elif playerInventory[material] >= materialQuantity:
          continue
        else:
          break
      if test[1] == itemToCraft:
        acceptInput = True
        if test[1] in craftable:
          # convert back from list
          test[1] = test[1][0]
          for x in range(0, len(itemsNeeded)):
            # remove materials
            material = itemsNeeded[x][0]
            materialQuantity = itemsNeeded[x][1]
            playerInventory[material] = playerInventory[material] - materialQuantity
            print("You lost", str(materialQuantity), material + "s.")
          # crafting tools and armor
          if i <= 1:
            splitWords = itemToCraft[0].split("_")
            type = splitWords[0]
            tool = splitWords[1]
            sleep(1.5)
            playerInventory[tool] = type
            print("You have acquired a", type, tool + ".")
            sleep(1.25)
            return
          else:
            # items that you get multiple items of when crafted
            # wood planks
            if test[1] == "wood_plank":
              playerInventory["wood_plank"] = playerInventory["wood_plank"] + 4
              print("\nYou received 4 wood_planks!")
              # sticks
            elif test[1] == "stick":
              playerInventory["stick"] = playerInventory["stick"] + 4
              print("\nYou received 4 sticks!")        
            elif test[1] == "paper":
              playerInventory["sugar_cane"] = playerInventory["sugar_cane"] + 3
              print("\nYou received 3 sugar_canes!")
            elif test[1] == "blaze_powder":
              playerInventory["blaze_powder"] += 2
              print("\nYou received 2 blaze_powder!")
            else:
              playerInventory[test[1]] = playerInventory[test[1]] + 1
              print("\nYou received 1", test[1] + '.')
            sleep(2)
          return
        elif test[0] == "user":
          print("Insufficient materials")
          sleep(1.25)
          return
          
  if acceptInput != True and test[1] != 'r':
    print("Enter a valid input (all lowercase and underscores instead of spaces)...\n")
    sleep(1.25)
 
  if test == "craftable":
    clear()
    for item in craftable:
      print(item[0])

def crafting():
  craftingKey = 0
  while True:
    global key
    clear()
    print("\n[   Crafting menu   ]" + '\nXP: ', str(experience) + "\n\nPress [Q] to list all items\nPress [W] to list current craftable items\nPress [E] to craft an item\nPress [SPACE] to go back to the main menu\n")
    craftingKey = getkey()
    if craftingKey == keys.Q:
      for i in range(0, len(craftingListsCombined)):
        for j in range(0, len(craftingListsCombined[i])):
          itemTesting = craftingListsCombined[i][j][0]
          print(itemTesting)
      print("\n Press [SPACE] to go back")
      while True:
        craftingKey = getkey()
        if craftingKey == keys.SPACE:
          break
    elif craftingKey == keys.W:
      getCraftableItems("craftable")
      print("\nPress [SPACE] to exit.")
      while True:
        key = getkey()
        if key == keys.SPACE:
          break
    elif craftingKey == keys.E:
      clear()
      userTest = str(input("Input an item to craft (Type item exactly like the id value to craft): \n"))
      getCraftableItems(["user", userTest])
    elif craftingKey == keys.SPACE:
      break
  returnToHome()

def mining():
  clear()
  print("Hold [W] to continue mining!\n")
  blocksToReceive = 0
  experienceToGain = 0
  
  while True:
    global experience
    key = getkey()
    if key == keys.W:
      if playerInventory["pickaxe"] == 'none':
        print("\nYou don't have a pickaxe yet!\nCraft a pickaxe to begin mining.\n")
        sleep(1.75)
        returnToHome()
        return
      # generate random number to start combat; 2% chance
      rand = randint(0, 100)
      if rand <= 4:
        combat()
        if playerDied == True:
          playerDied == False
          return
        else:
          print("\nExploring the caves...\n(Press [SPACE] to leave the cave and restore your health)\n")
      else:
        print("\nExploring the caves...\n(Press [SPACE] to leave the cave)\n")
        blocksToReceive = blocksToReceive + 1
        experienceToGain = experienceToGain + 2
        if playerInventory["pickaxe"] == 'wooden':
          sleep(1.15)
        elif playerInventory["pickaxe"] == 'stone':
          sleep(0.6)
        elif playerInventory["pickaxe"] == 'iron':
          sleep(0.4)
        elif playerInventory["pickaxe"] == 'golden':
          sleep(.225)
        elif playerInventory["pickaxe"] == 'diamond':
          sleep(.3)
        elif playerInventory["pickaxe"] == 'netherite':
          sleep(.25)
    else:
      break
      
  blocksToReceive = blocksToReceive / 2
  blocksToReceive = int(blocksToReceive)
  pickaxeProbabilities = {
# type [cobblestone, gravel, granite, coal, iron, gold, lapis, diamond, obsidian]
    "wooden": (65, 15, 5, 15, 0, 0, 0, 0, 0),
    "stone": (55, 15, 10, 5, 15, 0, 0, 0, 0),
    "gold": (45, 10, 5, 10, 15, 5, 10, 0, 0),
    "iron": (35, 10, 10, 10, 10, 10, 10, 5, 0),
    "diamond": (30, 5, 10, 10, 15, 10, 10, 5, 5),
    "netherite": (30, 5, 5, 5, 15, 15, 15, 5, 5)
  }
  # test the probabilities of pickaxes
  # for pickaxeType in pickaxeProbabilities:
  #   print(sum(pickaxeProbabilities[pickaxeType])/100)
  #   print(len(pickaxeProbabilities[pickaxeType]))
  #   sleep(1)

  # generate random blocks to add to inventory
  if blocksToReceive > 0:
    print("\n")
    blocksToReceive = choices(["cobblestone", "gravel", "granite", "coal", "iron_ore", "gold_ore", "lapis_lazuli", "diamond", "obsidian"], weights=pickaxeProbabilities[playerInventory["pickaxe"]],  k=blocksToReceive)
    for block in set(blocksToReceive):
      playerInventory[block] += blocksToReceive.count(block)
      print("You received", blocksToReceive.count(block), block, "s.")
      sleep(.25)
    sleep(1)
    experience = experience + experienceToGain
    print("You gained", str(experienceToGain) + "XP!")
    experienceToGain = 0
    sleep(3)
  returnToHome()

enchantingUnlocked = False
def enchanting():
  clear()
  if enchantingUnlocked == False:
    print("\nYou don't have a enchantment table yet!\nCraft a enchantment table to unlock enchanting.\n")
    sleep(1.75)
    returnToHome()
    return

def smelting():
  clear()
  print("[   Smelting Menu   ]\n")
  if playerInventory["furnace"] < 1:
    print("You don't have a furnace yet!\nCraft a furnace to smelt.\n")
    sleep(1.5)
    returnToHome()
    return
  smeltable = {
    "cobblestone": "stone",
    "iron_ore": "iron_ingot",
    "gold_ore": "gold_ingot",
    "wood_log": "charcoal",
    "sand": "glass",
    "raw_beef": "cooked_beef",
    "raw_chicken": "cooked_chicken",
    "raw_mutton": "cooked_mutton",
    "raw_porkchop": "cooked_porkchop",
    "raw_salmon": "cooked_salmon",
    "gravel": "flint"
  }
  available = {}
  for key in smeltable:
    if playerInventory[key] > 0:
      if playerInventory[key] == 1:
        print("You have 1", key + '.')
      else:
        print("You have", playerInventory[key], key)
      available[key] = playerInventory[key]
  sleep(2)
  continueSmelting = True
  while continueSmelting:
    itemToSmelt = input("\nInput item to smelt (type exactly like item id)\n")
    quantityToSmelt = int(input("\nType amount of items to smelt\n"))
    if itemToSmelt in available:
      if available[itemToSmelt] < quantityToSmelt:
        print("You don't have that much", itemToSmelt + '.\n')
      else:
        fuel = playerInventory["coal"] + playerInventory["charcoal"]
        fuelUsed = int(quantityToSmelt/8)
        if quantityToSmelt % 8 != 0:
          fuelUsed += 1
        if fuel < fuelUsed:
          print("You don't have enough coal!")
          sleep(1)
        else:
          # removing coal
          for i in range(0, fuelUsed):
            if playerInventory["coal"] > 0:
              playerInventory["coal"] -= 1
            else:
              playerInventory["charcoal"] -= 1
          print("You used", str(fuelUsed), "coal/charcoal.\n")
          sleep(1.5)
          # actual smelting of materials
          for i in range(0, quantityToSmelt):
            playerInventory[itemToSmelt] -= 1
            playerInventory[smeltable[itemToSmelt]] += 1
            print(itemToSmelt, "was smelted into a", smeltable[itemToSmelt] + '!')
            sleep(.5)
    else:
      print("You can't smelt that!\n")
      sleep(1)
      
    print("Would you like to smelt anything else (y/n)?\n")
    while True:
      key = getkey()
      if key == keys.Y:
        break
      elif key == keys.N:
        continueSmelting = False
        break
  returnToHome()

# Play music

def intro():
  # Introduction
  clear()
  print("Initializing server... (This may take a moment!)\n\n[--                           ] 3%")
  sleep(1)
  clear()
  print("Initializing server... (This may take a moment!)\n\n[--------                     ] 24%")
  sleep(1)
  clear()
  print("Initializing server... (This may take a moment!)\n\n[-----------------            ] 63%")
  sleep(2)
  clear()
  print("Initializing server... (This may take a moment!)\n\n[------------------------     ] 87%")
  sleep(1)
  clear()
  print("Initializing server... (This may take a moment!)\n\n[---------------------------- ] 99%")
  sleep(2.75)
  clear()
  print("Initializing server... (This may take a moment!)\n\n[-----------------------------] 100%")
  sleep(1)
  print("\nWelcome to Minecraft the Text Adventure!")
  sleep(2)
  clear()
  # Player sees what biome they are in
  biome = choice(biomes)
  print('You spawn in the {}!'.format(biome))
  sleep(2.75)
  clear()
  
intro()
gameCompleted = False

while gameCompleted != True:
  home()
  key = getkey()
  if key == keys.Q:
    lumbering()
  elif key == keys.A:
    crafting()
  elif key == keys.W:
    mining()
  elif key == keys.S:
    smelting()
  elif key == keys.I:
    inventory()
