from pygame import *
from classes import GameSprite
init()

width,height=900,750
window=display.set_mode((width,height))
display.set_caption('Snail Bob')
click=time.Clock()

my_font=font.SysFont('timesnewroman',100)
title=my_font.render('Snail Bob',True,(0,0,0))

play_but=GameSprite('assets/images/play_but.png',375,400,150,50)
rule_but=GameSprite('assets/images/rules.png',375,470,150,50)
rules_rect=Rect(375,470,300,250)
returnr_but=GameSprite('assets/images/return_but.png',385,480,30,30)
return_but=GameSprite('assets/images/return_but.png',10,10,50,50)
set_but=GameSprite('assets/images/settings_but.png',840,10,50,50)
sets_rect=Rect(590,10,300,250)
returns_but=GameSprite('assets/images/return_but.png',600,20,30,30)
exit_but=GameSprite('assets/images/Exit.png',10,10,50,50)
level1_but=GameSprite('assets/images/1.png',400,80,100,100)
level2_but=GameSprite('assets/images/2.png',400,230,100,100)
level3_but=GameSprite('assets/images/3.png',400,380,100,100)

menu_bg=transform.scale(image.load('assets/images/menu_bg.jpg'),(width,height))
level1_bg=transform.scale(image.load('assets/images/level1.jpg'),(width,height))
level2_bg=transform.scale(image.load('assets/images/level2.jpg'),(width,height))
level3_bg=transform.scale(image.load('assets/images/level3.jpg'),(width,height))

running=True
main='menu'

while running:
    x,y=mouse.get_pos()
    for e in event.get():
        if e.type==QUIT:
            running=False

        if e.type==MOUSEBUTTONDOWN:
            if main=='menu':
                if play_but.rect.collidepoint(x, y):
                    main = 'map'
                elif rule_but.rect.collidepoint(x,y):
                    main='rule'
                elif set_but.rect.collidepoint(x,y):
                    main='set'
                elif exit_but.rect.collidepoint(x,y):
                    running=False

            elif main=='map':
                if return_but.rect.collidepoint(x,y):
                    main='menu'
                if level1_but.rect.collidepoint(x,y):
                    main='level1'
                if level2_but.rect.collidepoint(x,y):
                    main='level2'
                if level3_but.rect.collidepoint(x,y):
                    main='level3'

            elif main=='level1':
                if return_but.rect.collidepoint(x,y):
                    main='map'

            elif main=='level2':
                if return_but.rect.collidepoint(x,y):
                    main='map'

            elif main=='level3':
                if return_but.rect.collidepoint(x,y):
                    main='map'

            elif main=='rule':
                if returnr_but.rect.collidepoint(x,y):
                    main='menu'

            elif main=='set':
                if returns_but.rect.collidepoint(x,y):
                    main='menu'

    if main=='menu':
        window.blit(menu_bg,(0,0))
        play_but.reset(window)
        rule_but.reset(window)
        set_but.reset(window)
        exit_but.reset(window)
        window.blit(title,(250,200))

    elif main=='rule':
        window.blit(menu_bg,(0,0))
        play_but.reset(window)
        draw.rect(window, (200,200,200), rules_rect)
        returnr_but.reset(window)
        set_but.reset(window)
        exit_but.reset(window)
        window.blit(title, (250, 200))

    elif main=='set':
        window.blit(menu_bg,(0,0))
        window.blit(title, (250, 200))
        play_but.reset(window)
        rule_but.reset(window)
        draw.rect(window,(255,255,255),sets_rect)
        returns_but.reset(window)
        exit_but.reset(window)

    elif main=='map':
        window.blit(menu_bg,(0,0))
        return_but.reset(window)
        level1_but.reset(window)
        level2_but.reset(window)
        level3_but.reset(window)

    elif main=='level1':
        window.blit(level1_bg,(0,0))
        return_but.reset(window)

    elif main=='level2':
        window.blit(level2_bg,(0,0))
        return_but.reset(window)

    elif main=='level3':
        window.blit(level3_bg,(0,0))
        return_but.reset(window)

    display.update()
    click.tick(70)