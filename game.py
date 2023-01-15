from config import *
def update(x, y, tmx):
    if x < 0:
        x = 0
    if x > 768:
        x = 768
    if y < 50:
        global roundx
        roundx = roundx + 1
        global mercedesc1
        mercedesc1 = mercedesc1 + 0.3
        global player2y, player1y, tm1, tm2
        player2y = 58
        player1y = 768
        y = 50
        tm1 = tm1 + tmx - tm1 - tm2
    if y > 768:
        y = 768
    screen.blit(tesla, (x, y))


def update2(x, y, tmx):
    if x < 0:
        x = 0
    if x > 768:
        x = 768
    if y < 50:
        y = 50
    if y > 768:
        global roundx
        roundx = roundx + 1
        global mercedesc2
        mercedesc2 = mercedesc2 + 0.3
        global player1y, player2y, tm1, tm2
        player1y = 768
        player2y = 58
        y = 768
        tm2 = tm2 + tmx - tm2 - tm1
    screen.blit(teslax, (x, y))


def mercedescross(x, y):
    screen.blit(mercedes, (x, y))


def iscollision(a, b, x, y):
    a += 16
    b += 16
    x += 16
    y += 16
    dist = math.sqrt(pow(a - x, 2) + pow(b - y, 2))
    if dist < 37:
        return True
    else:
        return False


def aftercol(x, tmx):
    global dead1, dead2, tm1, tm2
    if abs(x - 1) < 0.1:
        dead1 = 1
        tm1 = tm1 + tmx - tm1 - tm2
    else:
        dead2 = 1
        tm2 = tm2 + tmx - tm1 - tm2
    screen.blit(over, overrect)
    pygame.display.update()
    time.sleep(5)
    global roundx, player1y, player2y
    roundx += 1
    player2y = 58
    player1y = 768


def gameover():
    screen.fill(black)
    screen.blit(gameoverx, gameoverrect)
    pygame.display.update()
    time.sleep(2)
    screen.fill(black)
    screen.blit(playerscore1, playerscore1rect)
    pygame.display.update()
    time.sleep(2)
    screen.fill(black)
    screen.blit(playerscore2, playerscore2rect)
    pygame.display.update()
    time.sleep(2)
    screen.fill(black)
    screen.blit(finalmess, finalmessrect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()


screen = pygame.display.set_mode(size)
pygame.display.update()
running = True
clock = pygame.time.Clock()
while running:
    toppart = font.render(
        "score1:" + str(int(score1g + score1m)) + " score2:" + str(int(score2m + score2g)) + " time1:" + str(
            tm1) + " time2:" + str(tm2) + " round:" + str(rnd), True, white, black)
    toppartrect = toppart.get_rect()
    toppartrect.center = (width // 2, 25)
    score1 = (score1m + score1g)
    score2 = (score2g + score2m)
    screen.fill(black)
    rnd = int(int(roundx) / int(2))
    print(rnd, score1m, score1g, score2m, score2g, dead1, dead2, "\n")
    print(tm1, tm2, "\n")
    tm = int(pygame.time.get_ticks() / 1000)
    over = font.render('GAMEOVER! for you: ' + str(rnd) + "\n get ready playa", True, black, white)
    overrect = over.get_rect()
    overrect.center = (width // 2, height // 2)
    if (tm1 and tm2) > 0:
        playerscore1 = font.render("player1's score: " + str(int(score1 / tm1)), True, white, black)
        playerscore1rect = playerscore1.get_rect()
        playerscore1rect.center = (width // 2, height // 2)
        playerscore2 = font.render("player2's score: " + str(int(score2 / tm2)), True, white, black)
        playerscore2rect = playerscore2.get_rect()
        playerscore2rect.center = (width // 2, height // 2)
    if score1 > score2:
        finalmess = font.render("player1 won!", True, white, black)
    else:
        finalmess = font.render("player2 won!", True, white, black)
    finalmessrect = finalmess.get_rect()
    finalmessrect.center = (width // 2, height // 2)
    pygame.draw.rect(screen, beige, (0, 0, 800, 50))
    pygame.draw.rect(screen, green, (0, 50, 800, 50))
    pygame.draw.rect(screen, brown, (0, 750, 800, 50))
    pygame.draw.rect(screen, brown, (0, 650, 800, 50))
    pygame.draw.rect(screen, brown, (0, 550, 800, 50))
    pygame.draw.rect(screen, brown, (0, 450, 800, 50))
    pygame.draw.rect(screen, brown, (0, 350, 800, 50))
    pygame.draw.rect(screen, brown, (0, 250, 800, 50))
    pygame.draw.rect(screen, brown, (0, 150, 800, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1xchange = 0.5
                player2xchange = 0.5
            if event.key == pygame.K_LEFT:
                player1xchange = -0.5
                player2xchange = -0.5
            if event.key == pygame.K_UP:
                player1ychange = -0.5
            if event.key == pygame.K_DOWN:
                player2ychange = 0.5
        if event.type == pygame.KEYUP:
            player1xchange = 0
            player1ychange = 0
            player2xchange = 0
            player2ychange = 0
    if roundx % 2 == 0:
        if abs(dead1 - 1) < 0.1:
            roundx += 1
        else:
            print('loli\n')
            player1x += player1xchange
            player1y += player1ychange
            update(player1x, player1y, tm)
            i = 0
            while i < 9:
                screen.blit(gas, (gasx[i], gasy[i]))
                i += 1
            i = 0
            while i < 7:
                if abs(((6.65 - i) * 100) - player1y) < 0.1:
                    score1m += 10
                if mercedesx[i] > width:
                    mercedeschange[i] = -mercedesc1
                if mercedesx[i] < 0:
                    mercedeschange[i] = mercedesc1
                mercedesx[i] = mercedesx[i] + mercedeschange[i]
                mercedescross(mercedesx[i], mercedesy[i])
                i += 1
            for i in range(7):
                col = iscollision(player1x, player1y, mercedesx[i], mercedesy[i])
                if col:
                    aftercol(1, tm)
            for i in range(9):
                col = iscollision(player1x, player1y, gasx[i], gasy[i])
                if col:
                    aftercol(1, tm)
            for i in range(6):
                if abs(((6.2 - i) * 100) - player1y) < 0.1:
                    score1g += scoreg[5 - i]
    if roundx % 2 == 1:
        if abs(dead2 - 1) < 0.1:
            roundx += 1
        else:
            player2x += player2xchange
            player2y += player2ychange
            update2(player2x, player2y, tm)
            i = 0
            while i < 9:
                screen.blit(gas, (gasx[i], gasy[i]))
                i += 1
            i = 0
            while i < 7:
                if abs(((i + 1.5) * 100) - player2y) < 0.1:
                    score2m += 10
                if mercedesx[i] > width:
                    mercedeschange[i] = -mercedesc2
                if mercedesx[i] < 0:
                    mercedeschange[i] = mercedesc2
                mercedesx[i] = mercedesx[i] + mercedeschange[i]
                mercedescross(mercedesx[i], mercedesy[i])
                i += 1
            for i in range(7):
                col = iscollision(player2x, player2y, mercedesx[i], mercedesy[i])
                if col:
                    aftercol(2, tm)
            for i in range(9):
                col = iscollision(player2x, player2y, gasx[i], gasy[i])
                if col:
                    aftercol(2, tm)
            for i in range(6):
                if abs(((i + 2) * 100) - player2y) < 0.1:
                    score2g += scoreg[i]
    clock.tick(600)
    screen.blit(toppart, toppartrect)
    pygame.display.update()
    if abs(dead1 * dead2 - 1) < 0.1:
        gameover()
