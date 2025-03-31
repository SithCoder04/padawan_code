import pygame
pygame.init()

# Loading and playing a sound effect:

soundObj = pygame.mixer.Sound('f1.mp3')

soundObj.play()

 

# Loading and playing background music:

pygame.mixer.music.load('f1.mp3')

pygame.mixer.music.play(-1, 0.0)

# ...some more of your code goes here...

pygame.mixer.music.stop()
