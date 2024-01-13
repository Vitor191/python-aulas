import pygame

caminho_arquivo_mp3 = r'Dynasty.mp3'
pygame.init()
pygame.mixer.music.load(caminho_arquivo_mp3)

pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
