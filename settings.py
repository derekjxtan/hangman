import json
from random import randint

filename='words.json'
with open(filename) as f_obj:
	words=json.load(f_obj)





class Settings():
	#store all game settings and customizables
	
	def __init__(self):
		#screen settings
		self.screen_width=1350
		self.screen_height=800
		self.bg_colour=(0,0,0)
		
		#word to solve

		
		self.game_active=False
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.tries_remaining=10
		n=randint(0,len(words))
		self.word=words[n]
		self.word_guess=[]
		for x in range(len(self.word)):
			self.word_guess.append('_')
