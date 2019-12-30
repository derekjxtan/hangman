#class to show the letters that have been already choosen
import pygame.font

class Lettersguessed():
	
	def __init__(self,screen,letters):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.text_colour=(255,255,255)
		self.font=pygame.font.SysFont(None,30)
		
		self.prep_letters(letters)
		
	def prep_letters(self,letters):
		self.letters_image=self.font.render(letters,True,self.text_colour)
		self.letters_image_rect=self.letters_image.get_rect()
		self.letters_image_rect.left=20
		self.letters_image_rect.top=220		
	
	def draw_letters(self):
		self.screen.blit(self.letters_image,self.letters_image_rect)
		
		
