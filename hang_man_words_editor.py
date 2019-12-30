import json

words=[#emotions
	   ['H','A','P','P','Y'],
	   ['S','A','D'],
	   ['A','N','G','R','Y'],
	   ['W','O','R','R','I','E','D'],
	   ['S','U','R','P','R','I','S','E','D'],
	   #animals
	   ['F','I','S','H'],
	   ['C','H','I','C','K','E','N'],
	   ['H','O','R','S','E'],
	   ['S','H','E','E','P'],
	   ['E','A','G','L','E'],
	   #fruits
	   ['A','P','P','L','E'],
	   ['B','A','N','A','N','A'],
	   ['C','H','E','R','R','Y'],
	   ['S','T','R','A','W','B','E','R','R','Y'],
	   ['C','O','C','O','N','U','T'],
	   #musical instruments
	   ['U','K','U','L','E','L','E'],
	   ['G','U','I','T','A','R'],
	   ['P','I','A','N','O'],
	   ['D','R','U','M'],
	   ['X','Y','L','O','P','H','O','N','E'],
	   ]
	   
filename='words.json'
with open(filename,'w') as f_obj:
	json.dump(words,f_obj)
