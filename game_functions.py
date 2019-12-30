#store all game functions
import sys
import pygame
from time import sleep

from buttons import Buttons
from letters_guessed import Lettersguessed
from word_guess import Wordguess
from game_buttons import Playbutton
from announcements import Announcement

white=(255,255,255)

#check for keyboard and mouse events
def check_events(buttons,guesses,game_settings,play_button):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				sys.exit()
			if event.key==pygame.K_SPACE:
				game_settings.game_active=True
		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			for letter,coordinates in buttons.items():
				if mouse_x in range(coordinates[0],coordinates[1]) and mouse_y in range(coordinates[2],coordinates[3]):
					if letter not in guesses:
						guesses.append(letter)
						if letter not in game_settings.word:
							game_settings.tries_remaining-=1
							if game_settings.tries_remaining==0:
								game_settings.word_guess=game_settings.word
			check_play_button(play_button,mouse_x,mouse_y,game_settings)

#create play button
def create_play(play_button):
	play_button.draw_play_button()
	
#check play button
def check_play_button(play_button,mouse_x,mouse_y,game_settings):
	play_clicked=play_button.rect.collidepoint((mouse_x,mouse_y))
	if play_clicked and game_settings.game_active==False:
		game_settings.game_active=True









#update screen thorugh each loop of game
def update_screen(screen,buttons,guesses,game_settings,play_button):
	if game_settings.game_active==True:
		create_all_buttons(screen,buttons)
		show_letters(screen,guesses)
		show_word(screen,guesses,game_settings)
		hang(screen,game_settings)
		if game_settings.tries_remaining==0:
			create_announcement(screen,'Try Again!',(255,0,0))
		if game_settings.word==game_settings.word_guess and game_settings.tries_remaining!=0:
			create_announcement(screen,'Yaay!',(0,255,0))
	if game_settings.game_active==False:
		create_play(play_button)

#create button
def create_button(screen,msg,button_x,button_y,buttons):
	#create button
	button=Buttons(screen,msg,button_x,button_y)
	buttons[msg]=[button.rect.x,button.rect.x+80,button.rect.y,button.rect.y+80]
	button.draw_button()
	
def create_all_buttons(screen,buttons):
	#button=Buttons(screen,msg)
	num_but=13
	msgs1=['A','B','C','D','E','F','G','H','I','J','K','L','M']
	msgs2=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']	  
	
	#create first row of buttons
	for button_number,msg in zip(range(num_but),msgs1):
		button_width=80
		button_height=80
		row_number=0
		button_x=20+(20+button_width)*button_number
		button_y=20+(20+button_height)*row_number
		create_button(screen,msg,button_x,button_y,buttons)
	#create second row of buttons
	for button_number,msg in zip(range(num_but),msgs2):
		button_width=80
		button_height=80
		row_number=1
		button_x=20+(20+button_width)*button_number
		button_y=20+(20+button_height)*row_number
		create_button(screen,msg,button_x,button_y,buttons)
		
#display choosen letters
def show_letters(screen,guesses):
	letters=str('GUESSED: ')+str(guesses)
	show_letters=Lettersguessed(screen,letters)
	show_letters.draw_letters()
	
#display guess progress
def show_word(screen,guesses,game_settings):
	for guess in guesses:
		for letter in enumerate(game_settings.word):
			if letter[1]==guess:
				game_settings.word_guess[letter[0]]=letter[1]
	progress=str(game_settings.word_guess)
	show_guess=Wordguess(screen,progress)
	show_guess.draw_word()
	
#show hangman
def hang(screen,game_settings):
	tries=game_settings.tries_remaining
	if tries<10:
		pygame.draw.line(screen,white,(475,220),(875,220),10)
	if tries<9:
		pygame.draw.line(screen,white,(475,220),(475,620),10)
	if tries<8:
		pygame.draw.line(screen,white,(475,620),(875,620),10)
	if tries<7:
		pygame.draw.line(screen,white,(675,220),(675,270),10)
	if tries<6:
		pygame.draw.circle(screen,white,(675,320),50)
	if tries<5:
		pygame.draw.line(screen,white,(675,370),(675,500),10)
	if tries<4:
		pygame.draw.line(screen,white,(675,370),(600,400),10)
	if tries<3:
		pygame.draw.line(screen,white,(675,370),(750,400),10)
	if tries<2:
		pygame.draw.line(screen,white,(675,500),(600,530),10)
	if tries<1:
		pygame.draw.line(screen,white,(675,500),(750,530),10)

#create announcements
def create_announcement(screen,announcement,text_colour):
	announcement=Announcement(screen,announcement,text_colour)
	announcement.draw_announcement()






#end game;subject to change
def end_game(game_settings):
	if game_settings.word_guess==game_settings.word:
		return True
	if game_settings.tries_remaining==0:
		return True
		
#start new game
def new_game(guesses,game_settings):
	if end_game(game_settings)==True:
		game_settings.initialize_dynamic_settings()
		#word_guess==game_settings.word_guess.copy()
		game_settings.game_active=False
		guesses.clear()
		
