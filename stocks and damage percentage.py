# stocks and damage percentage
from types import SimpleNamespace

def playerStocks(player):
    player = SimpleNamespace
    player.stocks = 3
    player.damagePercentage = 0
    player.isDead = False
    isGameOver = False

    if hit(player):
        # redo after discussing w daniel about damage
        player.damagePercentage += 5
    if knocked(player):
        loseStock(player)
    if player.isDead == True:
        isGameOver = True

def distance(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**0.5

def hit(player):
    # discuss with daniel about hitbox
    return #within hitbox

def knocked(player):
    return #if out of map

def loseStock(player):
    if player.stocks > 0:
        player.stocks -= 1
    else:
        player.isDead = True