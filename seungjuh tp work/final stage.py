import pygame
import os
from stageSelectMenu import stageSelectMenu

class Camera:
    def __init__(self, screenW, screenH, worldW, worldH, 
                 margin=200, zoomMin=0.5, zoomMax=1.5, zoomSmooth=0.1):
        self.sw, self.sh = screenW, screenH
        self.ww, self.wh = worldW, worldH
        self.margin = margin
        self.zoomMin = zoomMin
        self.zoomMax = zoomMax
        self.zoomSmooth = zoomSmooth
        self.zoom = 1.0
        self.x = 0
        self.y = 0

    def update(self, p1, p2):
        midX = (p1.x + p1.width/2 + p2.x + p2.width/2) / 2
        midY = (p1.y + p1.height/2 + p2.y + p2.height/2) / 2
        dx = abs((p1.x + p1.width/2) - (p2.x + p2.width/2))
        dy = abs((p1.y + p1.height/2) - (p2.y + p2.height/2))
        dist = max(dx, dy)
        target = self.sw / (dist + self.margin)
        target = max(self.zoomMin, min(self.zoomMax, target))
        self.zoom += (target - self.zoom) * self.zoomSmooth
        camW = self.sw / self.zoom
        camH = self.sh / self.zoom
        self.x = midX - camW/2
        self.y = midY - camH/2
        self.x = max(0, min(self.x, self.ww - camW))
        self.y = max(0, min(self.y, self.wh - camH))

    def applyRect(self, rect):
        return pygame.Rect(
            (rect.x - self.x) * self.zoom,
            (rect.y - self.y) * self.zoom,
            rect.width * self.zoom,
            rect.height * self.zoom
        )

    def drawBackground(self, screen, bgImage):
        scaled = pygame.transform.smoothscale(
            bgImage,
            (int(self.ww * self.zoom), int(self.wh * self.zoom))
        )
        screen.blit(scaled, (-self.x * self.zoom, -self.y * self.zoom))

class Player:
    def __init__(self, x, y, width=32, height=48, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vy = 0

    def applyGravity(self, gravity, maxFallSpeed, tileSize=32):
        self.vy = min(self.vy + gravity, maxFallSpeed)
        self.y += self.vy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

def mushroomKingdom(rows, cols):
    stageMushroom = [[0 for _ in range(cols)] for _ in range(rows)]
    
    mainPlatformStart = int(cols * 0.13)
    mainPlatformEnd = int(cols * 0.93)
    for x in range(mainPlatformStart, mainPlatformEnd):
        stageMushroom[rows - 7][x] = 1
    
    floatingPlatformStart1 = int(cols * 0.23)
    floatingPlatformEnd1 = int(cols * 0.43)
    for x in range(floatingPlatformStart1, floatingPlatformEnd1):
        stageMushroom[rows - 12][x] = 2
    
    floatingPlatformStart2 = int(cols * 0.63)
    floatingPlatformEnd2 = int(cols * 0.84)
    for x in range(floatingPlatformStart2, floatingPlatformEnd2):
        stageMushroom[rows - 14][x] = 2
    
    floatingPlatformStart3 = int(cols * 0.35)
    floatingPlatformEnd3 = int(cols * 0.53)
    for x in range(floatingPlatformStart3, floatingPlatformEnd3):
        stageMushroom[rows - 17][x] = 2
        
    return stageMushroom

def smallBattlefield(rows, cols):
    stageSmallBattlefield = [[0 for _ in range(cols)] for _ in range(rows)]
    
    mainPlatformStart = int(cols * 0.20)
    mainPlatformEnd = int(cols * 0.80)
    
    for x in range(mainPlatformStart, mainPlatformEnd):
        stageSmallBattlefield[rows - 11][x] = 1
    
    leftFloatingPlatformStart = int(cols * 0.30)
    leftFloatingPlatformEnd = int(cols * 0.45)
    for x in range(leftFloatingPlatformStart, leftFloatingPlatformEnd):
        stageSmallBattlefield[rows - 16][x] = 2
    
    rightFloatingPlatformStart = int(cols * 0.58)
    rightFloatingPlatformEnd = int(cols * 0.74)
    for x in range(rightFloatingPlatformStart, rightFloatingPlatformEnd):
        stageSmallBattlefield[rows - 16][x] = 2
    return stageSmallBattlefield

def dreamLand(rows, cols):
    stageDreamLand = [[0 for _ in range(cols)] for _ in range(rows)]
    
    mainPlatformStart = int(cols * 0.25)
    mainPlatformEnd = int(cols * 0.78)
    for x in range(mainPlatformStart, mainPlatformEnd):
        stageDreamLand[rows - 7][x] = 1
    for x in range(int(cols * 0.31), int(cols * 0.43)):
        stageDreamLand[rows - 13][x] = 2
    for x in range(int(cols * 0.62), int(cols * 0.74)):
        stageDreamLand[rows - 13][x] = 2
    
    floatingRow2 = rows // 2
    for x in range(int(cols * 0.45), int(cols * 0.58)):
        stageDreamLand[floatingRow2 - 2][x] = 2
    
    return stageDreamLand

def peachCastle(rows, cols):
    stagePeachCastle = [[0 for _ in range(cols)] for _ in range(rows)]
    
    mainPlatformStart = int(cols * 0.2)
    mainPlatformEnd = int(cols * 0.83)
    for x in range(mainPlatformStart, mainPlatformEnd):
        stagePeachCastle[rows - 7][x] = 1
    
    roundPlatformsStart = int(cols * 0.37)
    roundPlatformsEnd = int(cols * 0.67)
    for x in range(roundPlatformsStart, roundPlatformsEnd):
        stagePeachCastle[rows - 11][x] = 2
    
    bridgeStart = int(cols * 0.43)
    bridgeEnd = int(cols * 0.6)
    for x in range(bridgeStart, bridgeEnd):
        stagePeachCastle[rows - 17][x] = 2
    
    return stagePeachCastle

def getStage(stageName):
    info = pygame.display.Info()
    screenWidth, screenHeight = info.current_w, info.current_h
    tileSize = 32
    
    rows = screenHeight // tileSize
    cols = screenWidth // tileSize
    
    if stageName == "mushroomKingdom":
        stage = mushroomKingdom(rows, cols)
    elif stageName == "smallBattlefield":
        stage = smallBattlefield(rows, cols)
    elif stageName == "dreamLand":
        stage = dreamLand(rows, cols)
    elif stageName == "peachCastle":
        stage = peachCastle(rows, cols)
    else:
        print("CODER ERROR, used unavailable stage name!")
        quit()
    return stage

def isOnGround(player, stage, tileSize=32):
    leftCol = player.x // tileSize
    rightCol = (player.x + player.width) // tileSize
    bottomRow = (player.y + player.height) // tileSize
    for col in range(leftCol, rightCol + 1):
        if 0 <= bottomRow < len(stage) and 0 <= col < len(stage[0]):
            if stage[bottomRow][col] in [1, 2, 3]:
                return True
    return False

def getCountdownImages(screenWidth):
    countdownFilenames = [
        "countdown_3.png",
        "countdown_2.png",
        "countdown_1.png",
        "countdown_go.png",
    ]
    countdownImages = []
    for filename in countdownFilenames:
        path = os.path.join("assets", filename)
        image = pygame.image.load(path).convert_alpha()
        if "GO" not in filename:
            desiredWidth = screenWidth // 5
        else:
            desiredWidth = screenWidth // 2
        aspectRatio = image.get_height() / image.get_width()
        desiredHeight = int(desiredWidth * aspectRatio)
        image = pygame.transform.smoothscale(image, (desiredWidth, desiredHeight))
        countdownImages.append(image)
    return countdownImages

def runCountdown(screen, bgImage, countdownImages, countdownDuration, offsetY, clock, screenWidth, screenHeight):
    pygame.mixer.music.load('assets/countdown.mp3')
    pygame.mixer.music.play(1)
    pygame.time.wait(670)
    for image in countdownImages:
        stepStart = pygame.time.get_ticks()
        while pygame.time.get_ticks() - stepStart < countdownDuration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
            screen.blit(bgImage, (0, 0))
            rect = image.get_rect(center=(screenWidth // 2, screenHeight // 2 - offsetY))
            screen.blit(image, rect)
            pygame.display.flip()
            clock.tick(60)

def game():
    pygame.init()
    info = pygame.display.Info()
    screenWidth, screenHeight = info.current_w, info.current_h
    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    # change tile size
    tileSize = 32
    cols = screenWidth // tileSize
    rows = screenHeight // tileSize
    worldW = cols * tileSize
    worldH = rows * tileSize
    camera = Camera(screenWidth, screenHeight, worldW, worldH)
    
    stage = getStage("dreamLand")
    bgPath = os.path.join("assets", "dream_land.webp")
    bgImage = pygame.image.load(bgPath).convert()
    bgImage = pygame.transform.smoothscale(bgImage, (screenWidth, screenHeight))
    
    countdownDuration = 1000
    offsetY = screenHeight // 10
    runCountdown(
        screen, bgImage, getCountdownImages(screenWidth),
        countdownDuration, offsetY, clock, screenWidth, screenHeight
    )
    player1 = Player(screenWidth//2 - 100, 100, color=(255,0,0))
    player2 = Player(screenWidth//2 + 100, 100, color=(0,0,255))
    player1SpawnX, player1SpawnY = player1.x, player1.y
    player2SpawnX, player2SpawnY = player2.x, player2.y
    
    speed = 5
    jumpPower = 15
    gravity = 1
    maxFallSpeed = 12
    
    gameEndImage = pygame.image.load(os.path.join("assets","game_end.webp")).convert()
    gameEndImage = pygame.transform.smoothscale(gameEndImage, (screenWidth, screenHeight))
    gameSound = pygame.mixer.Sound(os.path.join("assets","game_sound.mp3"))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
               event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and isOnGround(player1, stage, tileSize):
                    player1.vy = -jumpPower
                if event.key == pygame.K_UP and isOnGround(player2, stage, tileSize):
                    player2.vy = -jumpPower
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player1.x -= speed
        if keys[pygame.K_d]:
            player1.x += speed
        if keys[pygame.K_s]:
            player1.y += speed
        if keys[pygame.K_LEFT]:
            player2.x -= speed
        if keys[pygame.K_RIGHT]:
            player2.x += speed
        if keys[pygame.K_DOWN]:
            player2.y += speed
        for p in (player1, player2):
            if not isOnGround(p, stage, tileSize):
                p.applyGravity(gravity, maxFallSpeed)
            else:
                p.vy = 0
        
        if player1.y > screenHeight:
            player1.x, player1.y, player1.vy = player1SpawnX, player1SpawnY, 0
        if player2.y > screenHeight:
            player2.x, player2.y, player2.vy = player2SpawnX, player2SpawnY, 0
        
        camera.update(player1, player2)
        camera.drawBackground(screen, bgImage)
       
        for r in range(len(stage)):
            for c in range(len(stage[0])):
                if stage[r][c] != 0:
                    color = (100,100,100) if stage[r][c] == 1 else (150,150,150)
                    tileRect = pygame.Rect(c*tileSize, r*tileSize, tileSize, tileSize)
                    # pygame.draw.rect(screen, color, camera.applyRect(tileRect))
        
        for p in (player1, player2):
            pr = pygame.Rect(p.x, p.y, p.width, p.height)
            pygame.draw.rect(screen, p.color, camera.applyRect(pr))
        
        # stock labels
        # stockLabel1    = stockFont.render(f"Stocks: {stocks1}", True, stockColor)
        # dmgLabel1 = stockFont.render(f"Damage: {dmg1}%", True, stockColor)
        # screen.blit(stockLabel1, (10, 10))
        # screen.blit(dmgLabel1, (10, 10 + 15))

        # stockLabel2    = stockFont.render(f"Stocks: {stocks2}", True, stockColor)
        # dmgLabel2 = stockFont.render(f"Damage: {dmg2}%", True, stockColor)
        # screen.blit(stockLabel2, (10, 10))
        # screen.blit(dmgLabel2, (10, 10 + 15))

        # if (player1.getStocks() == 0) or (player2.getStocks() == 0):
        #     gameSound.play()
        #     screen.fill((0, 0, 0))
        #     screen.blit(gameEndImage, (0, 0))
        #     pygame.display.flip()
        #     soundLength = gameSound.get_length()
        #     pygame.time.wait(int(soundLength * 1000))
        #     running = False

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

game()