#a imagem não é exibida
import pygame
pygame.init()
pygame.image.load('Vergil.jpg')
pygame.mixer.music.load('musicateste.mp3')
pygame.mixer.music.play()
pygame.event.wait()
