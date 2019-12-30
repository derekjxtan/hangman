#class to manage visualisation of guessing process
import pygame

class Wordguess():
	
	def __init__(self,screen,word_guess):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.text_colour=(255,255,255)
		self.font=pygame.font.SysFont(None,72)
		
		self.prep_word(word_guess)
		
	def prep_word(self,word_guess):
		self.word_image=self.font.render(word_guess,True,self.text_colour)
		self.word_image_rect=self.word_image.get_rect()
		self.word_image_rect.centerx=self.screen_rect.centerx
		self.word_image_rect.bottom=self.screen_rect.bottom-50

	def draw_word(self):
		self.screen.blit(self.word_image,self.word_image_rect)
