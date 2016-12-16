import pygame
'''
screen = pygame.display.set_mode((640, 480))
pygame.draw.rect(screen, (0,255,255), (200, 150, 200, 200))
pygame.draw.circle(screen, (10,10,10), (300, 250), 100) 
'''

screen = pygame.display.set_mode((640, 480))
pygame.draw.rect(screen, (255,255,255), (200, 150, 255, 150))
pygame.draw.rect(screen, (255,0,0), (370, 150, 85, 150))
pygame.draw.rect(screen, (0,255,0), (200, 150, 85, 150))



pygame.display.update()


