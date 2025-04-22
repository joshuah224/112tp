import pygame
import os
import sys

def stageSelectMenu():
    pygame.init()
    info = pygame.display.Info()
    screenWidth, screenHeight = info.current_w, info.current_h
    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    bgPath = os.path.join("assets", "StageSelection.png")
    stageSelectionBg = pygame.image.load(bgPath).convert()
    stageSelectionBg = pygame.transform.scale(stageSelectionBg, (screenWidth, screenHeight))

    stageRects = [
        pygame.Rect(130, 133, 250, 140),
        pygame.Rect(450, 133, 250, 140),
        pygame.Rect(130, 340, 250, 140),
        pygame.Rect(450, 340, 250, 140),
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                for i, stageRect in enumerate(stageRects):
                    if stageRect.collidepoint(mouseX, mouseY):
                        pygame.display.quit()
                        return i

        screen.blit(stageSelectionBg, (0, 0))

        mouseX, mouseY = pygame.mouse.get_pos()
        for stageRect in stageRects:
            if stageRect.collidepoint(mouseX, mouseY):
                pygame.draw.rect(screen, (255, 255, 0), stageRect, 4)

        pygame.display.flip()
        clock.tick(60)

stageSelectMenu()