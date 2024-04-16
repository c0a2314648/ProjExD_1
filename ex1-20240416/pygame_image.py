import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koka_img = pg.image.load("fig/3.png") #練習２
    koka_rct = koka_img.get_rect() #練習８－１
    koka_rct.center = 300, 200 #練習８－２
    koka_img = pg.transform.flip(koka_img, True, False)
    bg2_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg2_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #練習８－３
        if key_lst[pg.K_UP]:           #練習８－４
            koka_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            koka_rct.move_ip((0, 1))
        if key_lst[pg.K_LEFT]:
            koka_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            koka_rct.move_ip((2, 0))
        if key_lst[pg.K_LEFT] == False or key_lst[pg.K_RIGHT] == False:
            koka_rct.move_ip((-1, 0))

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0]) #練習６
        screen.blit(bg2_img, [-x+1600, 0]) #練習７－１
        screen.blit(bg_img, [-x+3200, 0]) #練習７－２
        screen.blit(bg2_img, [-x+4800, 0]) #練習７－２
        screen.blit(koka_img, koka_rct) #練習４
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()