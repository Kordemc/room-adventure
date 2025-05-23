###########################################################################################
# Name: 
# Date: 
# Description: 
###########################################################################################
from tkinter import *

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room:
	# the constructor
	def __init__(self, name, image):
		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits = {}
		self.items = {}
		self.grabbables = []

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate dictionary
		self._items[item] = desc

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
	# the constructor
	def __init__(self, parent):
		# call the constructor in the superclass
		Frame.__init__(self, parent)

	# creates the rooms
	def createRooms(self):
		r1 = Room("The Body, elven by the looks of it, head caved in, hard to identify, I take a drag of a cigar as the smoke wisps through my eye sockets. the body was let out in the open, whoever did this wanted people to see. \n theres a necklace on the body of a gold symbol of two m's, Malone Family symbol, only higher ups get those. he wont take too kindly to someone killig one of his 'sons'. and a bloody pipe next to him. Theres a fire escape to the west ther car is back south and theres an open alley ahead of me.", "thebody.gif")
		r2 = Room("The car, Ulysses is next to the crusier, scanning the area trying to make sure everything's clear ", "thecar.gif")
		r3 = Room("The Fire Escape, theres a red stain and i got a weird vibe, magic was used around here, residue from magic usage, i should check that out. ever since i died i started to feel arcane disurbances but Ulysess probably felt it before we got here.", "thefireescape.gif")
		r4 = Room("The Alley, nothin' too much to see here, except for a mark on the ground. Looks like maybe a footprint. another drag of the cigar and a puff of smoke exits through my teeth.", "thealley.gif")
		r1.addExit("west", r3)
		r1.addExit("south", r2)
		r1.addExit("north", r4)
		r1.addGrabbable("necklace")
		# item
		r1.addItem("pipe", "It seems too easy for it to be the murder weapon, but again this was a display so i can't count it out. i may not have finger prints but I'll leave it here. Don't want another lecture from Pyrestone")
		r1.addItem("body", "Judging by the ears, and his usual outfit its Delsaran Smith, A malone family Lieutenant, they aren't all bad, and I'd say he was kindest out of the ones ive met. He didn't deserve this...")
		r2.addExit("north", r1)
		r2.addExit("south", None)
		#items room 2
		r2.addItem("ulysses", "Ulyesses Steele, a Human Male, standing at average height, light skin with markingings that go from his fingers down to his forearms. Hes wearing glasses that he hasn't needed for years after...maybe not the time to get into that. We go way back, and he's the best Sorcerer I know.")
		r2.addItem("car", "Our newest police crusier after the last one got zapped by a wizard that lost his marbles. Ulysses seemed to noticed my attention and says: 'you trying to go? got everything you needed? you can take the keys if you want and we can head out' He holds the car keys out to me")
		#grabbles in room 2
		r2.addGrabbable("keys")
		#room 3 exits
		r3.addExit("east",r1)
		# room 3 items
		r3.addItem("residue", "Arcane residue, by the looks of it conjuration...worst case its a teleportation spell, which would mean we're dealing with a powerful caster, teleportaion isn't easy.")
		r3.addItem("stain", "Blood from up here? guess they moved the body through here, unless the blood isn't the victum's....ill leave a not for Forensics")
		#room 4 exits
		r4.addExit("south", r1)
		#room 4 items
		r4.addItem("marks", "Drag marks? no looks like a footprint or somthing. left by an old shoe, gotta leave a note for this too before Forensics gets here")
		#setting room 1 as the current room
		currentRoom = r1

	# sets up the GUI
	def setupGUI(self):

	# sets the current room image
	def setRoomImage(self):

	# sets the status displayed on the right of the GUI
	def setStatus(self, status):

	# plays the game
	def play(self):
		# add the rooms to the game
		self.createRooms()
		# configure the GUI
		self.setupGUI()
		# set the current room
		self.setRoomImage()
		# set the current status
		self.setStatus("")

	# processes the player's input
	def process(self, event):

##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
