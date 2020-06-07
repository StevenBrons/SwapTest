import random
import numpy as np

DIMENSION = 4
WIDTH = 4
WORDS = ["denk","boek","keer","plus","beer", "dier", "dans", "reep", "kant", "bank","zand","raad","kier","door","deur","neus","kers","vier","acht","fles","durf", "nies","zand"]
# , ,,"naam" , "deeg", "riep", "hoop", "niet", "voor", "kaas","mand","tand","want", "wier"

def createDimension(dimension):
	if (dimension == 1):
		return [None] * WIDTH
	return [createDimension(dimension -1) for i in range(0,WIDTH)]

BOARD = np.array(createDimension(DIMENSION))

def getEdges(item1, item2, dimension):
	if (dimension ==  1):
		return [[item1],[item2]]
	newPositions = []
	for sp in getEdges(item1, item2,dimension - 1):
		p1 = sp.copy()
		p1.append(item1)
		p2 = sp.copy()
		p2.append(item2)
		newPositions.append(p1)
		newPositions.append(p2)
	return newPositions

START_POSITIONS = getEdges(0, WIDTH - 1, DIMENSION)
DIRECTIONS = [e for e in getEdges(0, 1, DIMENSION) if e != [0] * DIMENSION]

def canPlaceWordAt(word,start,dr):
	hits = 0
	for i in range(0,WIDTH):
		curPos = BOARD[tuple(np.array(start) + (dr * i))]
		if curPos == word[i]:
			hits += 1
			continue
		if curPos != None:
			return -1
	return hits

def placeWordAt(word,start,dr):
	for i in range(0,WIDTH):
		BOARD[tuple(np.array(start) + (dr * i))] = word[i]

def findBestPlacement(word):
	random.shuffle(START_POSITIONS)
	random.shuffle(DIRECTIONS)
	valid = False
	i = 0
	j = 0
	best = [None,None]
	bestScore = -1
	for i in range(0,len(START_POSITIONS)):
		for j in range(0,len(DIRECTIONS)):
			pos = np.array(START_POSITIONS[i])
			dr = np.array(DIRECTIONS[j])
			for a in range(0,DIMENSION):
				dr[a] = dr[a] if pos[a] == 0 else -1 * dr[a]
			score = canPlaceWordAt(word,pos,dr)
			if score > bestScore:
				bestScore = score
				best[0] = pos
				best[1] = dr
	return best

BOARD_BAC = BOARD.copy()

found = False
attempt = 0
while (not found):
	random.shuffle(WORDS)
	BOARD = BOARD_BAC.copy()
	attempt += 1
	try:
		for word in WORDS:
			best = findBestPlacement(word)
			placeWordAt(word, best[0],best[1])
		found = True
		pass
	except:
		pass

print(BOARD)
print(attempt)