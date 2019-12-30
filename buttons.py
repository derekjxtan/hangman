import pygame.font

class Buttons():
	
	def __init__(self,screen,msg,button_x,button_y):
		"""initialize button attributes"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		#set dimensions of buttons
		self.width,self.height=80,80
		self.button_colour=(255,255,255)
		self.text_colour=(0,0,0)
		self.font=pygame.font.SysFont(None,48)
		
		#build button rect object
		self.rect=pygame.Rect(0,0,self.width,self.height)
		
		#Move button to position
		self.rect.left=button_x
		self.rect.top=button_y
		
		#prep message
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		"""turn msg into a rendered image and center text on button"""
		self.msg_image=self.font.render(msg,True,self.text_colour,self.button_colour)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center		
		
	def draw_button(self):
		#draw blank button and then draw message
		self.screen.fill(self.button_colour,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
