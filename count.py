import collections
from collections import Counter
from itertools import combinations
import re

characters = ['Dilbert',
'Boss',
'Wally',
'Alice',
'Dogbert',
'Asok',
'Ted',
'Howard',
'Carol',
'Ratbert',
'Catbert',
'Dilmom',
'Phil',
'Bob',
'Garbageman',
'Tina',
'Mordac',
'Topper',
'Dadbert',
'Liz',
'Dawn',
'Rex',
'CEO',
'Robot',
'Elbonian',
'Troll',
'doctor',
'Woman',
'Salesman',
'Coworker',
'Advisor',
'Marketing Guy',
'Monster']

# Two-dimensional array to keep track of character pair interactions
Pairs = [[0 for x in range(len(characters))] for x in range(len(characters))] 

print len(characters)
with open("dilbertstripsall_edited.txt") as f:
	#c = collections.Counter(f.read().split())
	# print str(c)
	for line in f:
		print "Looking at line " + line
		for character1 in characters:
			for character2 in characters:
				#discard duplicate character pair interactions
				if characters.index(character1) < characters.index(character2):
					# print str(characters.index(character1)) + " is less than " + str(characters.index(character2))
					if (character1 in line) and (character2 in line):
						print character1 + " and " + character2 + " appears on this line"
						Pairs[characters.index(character1)][characters.index(character2)] +=1
						print Pairs[characters.index(character1)][characters.index(character2)]

#Record number of interactions between source and target in CSV format for D3
for character1 in characters:
	for character2 in characters:
		if characters.index(character1) < characters.index(character2):
			# print character1 + " and " + character2 + " has " + str(Pairs[characters.index(character1)][characters.index(character2)]) + " interactions."
			print "source,target,value"
			print character1 + "," + character2 + "," + str(Pairs[characters.index(character1)][characters.index(character2)]) + " interactions."

