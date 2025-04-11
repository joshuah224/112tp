import pygame # type: ignore
import random
from types import SimpleNamespace

def main():
    pygame.init()

    info = pygame.display.Info()
    screenWidth, screenHeight = info.currentW, info.currentH 
    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)

    tileSize = 32
    cols = screenWidth // tileSize
    rows = screenHeight // tileSize
    
    # yggdrasil's atlar
    stageYggdrasilsAtlar = [[0 for _ in range(cols)] for _ in range(rows)]
    mainPlatformStart = int(cols * 0.20)
    mainPlatformEnd = int(cols * 0.80)
    for x in range(mainPlatformStart, mainPlatformEnd):
        stageYggdrasilsAtlar[rows - 3][x] = 1

    # small battlefield
    stageSmallBattlefield = [[0 for _ in range(cols)] for _ in range(rows)]
    mainPlatformStart = int(cols * 0.20)
    mainPlatformEnd = int(cols * 0.80)
    for x in range(mainPlatformStart, mainPlatformEnd):
        stageSmallBattlefield[rows - 3][x] = 1

    floatingRow = max(0, rows-5)
    
    leftFloatingPlatformStart = int(cols * 0.25)
    leftFloatingPlatformEnd = int(cols * 0.45)
    for x in range(leftFloatingPlatformStart, leftFloatingPlatformEnd):
        stageSmallBattlefield[floatingRow][x] = 2

    rightFloatingPlatformStart = int(cols * 0.55)
    rightFloatingPlatformEnd = int(cols * 0.75)
    for x in range(rightFloatingPlatformStart, rightFloatingPlatformEnd):
        stageSmallBattlefield[floatingRow][x] = 2

    # big battlefield
    stageBigBattlefield = [[0 for _ in range(cols)] for _ in range(rows)]
    mainPlatformStart = int(cols * 0.20)
    mainPlatformEnd = int(cols * 0.80)
    bottomRow = rows - 3
    for x in range(mainPlatformStart, mainPlatformEnd):
        stageBigBattlefield[bottomRow][x] = 1
    
    floatingRow1 = max(0, rows-5)
    for x in range(int(cols * 0.15), int(cols * 0.30)):
        stageBigBattlefield[floatingRow1][x] = 2
    for x in range(int(cols * 0.40), int(cols * 0.60)):
        stageBigBattlefield[floatingRow1][x] = 2
    for x in range(int(cols * 0.70), int(cols * 0.85)):
        stageBigBattlefield[floatingRow1][x] = 2

    floatingRow2 = rows // 2
    for x in range(int(cols * 0.20), int(cols * 0.35)):
        stageBigBattlefield[floatingRow2][x] = 2
    for x in range(int(cols * 0.45), int(cols * 0.55)):
        stageBigBattlefield[floatingRow2][x] = 2
    for x in range(int(cols * 0.65), int(cols * 0.80)):
        stageBigBattlefield[floatingRow2][x] = 2
    
    floatingRow3 = rows // 4
    for x in range(int(cols * 0.15), int(cols * 0.30)):
        stageBigBattlefield[floatingRow3][x] = 2
    for x in range(int(cols * 0.40), int(cols * 0.60)):
        stageBigBattlefield[floatingRow3][x] = 2
    for x in range(int(cols * 0.70), int(cols * 0.85)):
        stageBigBattlefield[floatingRow3][x] = 2

    # Pokemon stadium 2
    stagePokemonStadium = [[0 for _ in range(cols)] for _ in range(rows)]
    mainPlatformStart = int(cols * 0.20)
    mainPlatformEnd = int(cols * 0.80)
    for x in range(mainPlatformStart, mainPlatformEnd):
        stagePokemonStadium[rows - 3][x] = 1

    floatingRow = max(0, rows-5)
    
    leftFloatingPlatformStart = int(cols * 0.25)
    leftFloatingPlatformEnd = int(cols * 0.45)
    for x in range(leftFloatingPlatformStart, leftFloatingPlatformEnd):
        stagePokemonStadium[floatingRow][x] = 2

    rightFloatingPlatformStart = int(cols * 0.55)
    rightFloatingPlatformEnd = int(cols * 0.75)
    for x in range(rightFloatingPlatformStart, rightFloatingPlatformEnd):
        stagePokemonStadium[floatingRow][x] = 2

    stages = {"Yggdrasil's Atlar": stageYggdrasilsAtlar,
              "Small Battlefield": stageSmallBattlefield,
               "Big Battlefield": stageBigBattlefield, 
               "Pokémon Stadium 2": stagePokemonStadium
            }



def isOnGround(player, stage, tileSize=32):

    leftCol = player.x // tileSize
    rightCol = (player.x + player.width) // tileSize
    bottomRow = (player.y + player.height) // tileSize

    for col in range(leftCol, rightCol+1):
        if bottomRow < 0 or bottomRow >= len(stage) or col < 0 or col >= len(stage[0]):
            if stage[bottomRow][col] == 1 or 2 or 3:
                return True
    return False

def drawGO(screen, font, text, screen_width, screen_height):
    
    info = pygame.display.Info()
    screenWidth, screenHeight = info.currentW, info.currentH 
    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
    
    font = pygame.font.Sysfont("ITC Kabel Bold", 50)
    text = ["3", "2", "1", "GO"]

    for msg in text:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                




pygame.quit()

