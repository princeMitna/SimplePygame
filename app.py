import pygame
import game as gc
from pygame import display,event,image
from animal import Animal
from time import sleep
def find_index(x,y):
    row =y//gc.IMAGE_SIZE
    col=x//gc.IMAGE_SIZE
    index =row*gc.NUM_TILES_SIDE+col
    return index

pygame.init()

display.set_caption("My Game")

screen=display.set_mode((512,512))

matched=image.load("other_assets/matched.png")





running=True

tiles=[Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
c=[]

while running:
    current_event=event.get()

    for e in current_event:
        if e.type ==pygame.QUIT:
            running=False

        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:
                running=False

        if e.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            print(mouse_x,mouse_y)
            

            index = find_index(mouse_x,mouse_y)
            if index not in c:

                c.append(index)
            if len(c)>2:
                c=c[1:]



    screen.fill((255,255,255))
    t=0
    for _,tile in enumerate(tiles):
        image_i =tile.image if tile.index in c else tile.box
        if not tile.skip:

            screen.blit(image_i,(tile.col *gc.IMAGE_SIZE,tile.row*gc.IMAGE_SIZE))
        else:
            t+=1
    if len(c)==2:
        idx1,idx2=c
        if tiles[idx1].name==tiles[idx2].name:
            tiles[idx1].skip=True
            tiles[idx2].skip=True
            sleep(0.4)
            screen.blit(matched,(0,0))
            display.flip()
            sleep(0.4)
            c=[]

    if t==len(tiles):
        running=False

    display.flip()


print("Goodbye!")



