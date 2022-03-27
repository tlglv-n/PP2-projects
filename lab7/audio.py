import os
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
playlist = ["m1.flac", "m2.flac"]
pygame.mixer.music.load(playlist[0])
pygame.mixer.music.play()

image = pygame.image.load("C:/ZNBURG/courses/PP2/lab7/text.png")
cnt = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pygame.mixer.music.pause()
            if event.key == pygame.K_e:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            if event.key == pygame.K_w:
                pygame.mixer.music.play()
            if event.key == pygame.K_2:
                pygame.mixer.music.stop()
                cnt += 1
                if cnt >= len(playlist) - 1:
                    cnt -= len(playlist)
                pygame.mixer.music.load(playlist[cnt])
                pygame.mixer.music.play()
            if event.key == pygame.K_1:
                pygame.mixer.music.stop()
                cnt -= 1
                if cnt <= 0:
                    cnt += len(playlist)
                pygame.mixer.music.load(playlist[cnt])
                pygame.mixer.music.play()
        screen.blit(image, (0, 0))
        pygame.display.flip()

pygame.quit()
