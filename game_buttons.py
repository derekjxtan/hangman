#class to handle buttons like play
import pygame.font

class Playbutton():
	
	def __init__(self,screen,msg):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.width,self.height=200,100
		self.button_colour=(255,255,255)
		self.text_colour=(0,0,0)
		self.text_font=pygame.font.SysFont(None,48)
		
		#buid rect object
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		self.msg_image=self.text_font.render(msg,True,self.text_colour,self.button_colour)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center

	def draw_play_button(self):
		self.screen.fill(self.button_colour,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
