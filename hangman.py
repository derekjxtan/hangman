import pygame
import sys
from pygame.sprite import Group
from time import sleep

from settings import Settings
import game_functions as gf
from buttons import Buttons
from game_buttons import Playbutton

def run_game():
	#init game
	pygame.init()
	game_settings=Settings()
	
	
	screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
	pygame.display.set_caption("Hangman")
	bg_colour=game_settings.bg_colour
	
	buttons={}
	guesses=[]
	#word=game_settings.word
	#word_guess=game_settings.word_guess.copy()

		
	play_button=Playbutton(screen,'Play')	
	
	
		
	
	#start main loop of game
	while True:
		#watch for keyboard and mouse event
		gf.check_events(buttons,guesses,game_settings,play_button)
				
		#redraw screen during each pass through loop
		screen.fill(bg_colour)

		gf.update_screen(screen,buttons,guesses,game_settings,play_button) 

		#make most recently drawn screen visible
		pygame.display.flip()
		
		if gf.end_game(game_settings)==True:
			sleep(1)
		gf.new_game(guesses,game_settings)		
		
run_game()
