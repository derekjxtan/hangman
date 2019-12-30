#class to handle announcements like congrats/try again
import pygame.font

class Announcement():
	
	def __init__(self,screen,announcement,text_colour):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		self.text_colour=text_colour
		self.font=pygame.font.SysFont(None,300)
		
		self.prep_announcement(announcement)

	def prep_announcement(self,announcement):
		self.announ_image=self.font.render(announcement,True,self.text_colour)
		self.announ_image_rect=self.announ_image.get_rect()
		self.announ_image_rect.centerx=self.screen_rect.centerx
		self.announ_image_rect.top=300
		
	def draw_announcement(self):
		self.screen.blit(self.announ_image,self.announ_image_rect)
