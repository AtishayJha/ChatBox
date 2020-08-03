import pygame

import textwrap
from Database import Database

def main():
    pygame.init()
    string = ""
    x = 0
    initial_y = 525
    chatlst = Database.read()
    lastval = None
    ycounter = [10]
    n = len(chatlst)
    count = 0
    scroller = 0
    auto = True
    write = False

    def create(x, A, B, k, background, foreground):
        font = pygame.font.Font('CreatorCreditsBB.ttf', k)
        text = font.render(x, True, foreground, background)
        textRect = text.get_rect()
        textRect.midleft = (A, B)
        screen.blit(text, textRect)
    screen = pygame.display.set_mode((500, 550))

    def get(chatlst, string, initial_y, auto, n):
        keys = pygame.key.get_pressed() 
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key) 
            write = True
            if len(key) == 1:
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    string += key.upper()
                else:
                    string += key
            elif key=="space":
                string+=" "
            elif key == "backspace":
                string = string[:len(string) - 1]
            elif event.key == pygame.K_RETURN:
                write = False
                if string!="":
                    chatlst.append([string, 1, n])
                    string = ""
                    initial_y = 525
                    auto = True
                    n+=1
        return chatlst, string, initial_y, auto, n
    while True:
        recieved = client.recv()
        if recieved!="no":chatlst.append([recieved, 0, n])
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    Database.write(chatlst)
                    pygame.quit()
                    exit()
            chatlst, string, initial_y, auto, n = get(chatlst, string, initial_y, auto, n)
        for num, i in enumerate(chatlst):
            wrapper = textwrap.TextWrapper(width=15) 
            word_lststat = wrapper.wrap(text=i[0])
            word_lststatn = wrapper.wrap(text=chatlst[chatlst.index(i)-1][0])
            if auto == True:
                if ycounter[len(ycounter)-1]-scroller+50*len(word_lststat)+10>550:
                    scroller = ycounter[len(ycounter)-1]+50*len(word_lststat)+10-560
            if i[1]==1:
                statwidth = len(i[0])*25
                if len(word_lststat)>1:
                    statwidth = 15*20
                if i[0].count("m")>5:statwidth = 20*20
                if i[0].count("w")>5:statwidth = 20*20
                if i[2]>chatlst[num-1][2]:
                    ycounter.append(ycounter[num-1]+50*len(word_lststatn)+20)
                    ycounter = [i for n, i in enumerate(ycounter) if i not in ycounter[:n]] 
                pygame.draw.rect(screen, 
                                    (0, 0, 0), 
                                    ((490-statwidth), 
                                    ycounter[num]-scroller, 
                                    statwidth, 
                                    50*len(word_lststat)+10))
                count = 0
                for j in word_lststat:
                    create(j, (490-statwidth), ycounter[num]-scroller+25+count, 50, (0, 0, 0), (255, 255, 255))
                    count+=50
            elif i[1]==0:
                statwidth = len(i[0])*25
                if len(word_lststat)>1:
                    statwidth = 15*20
                if i[0].count("m")>5:statwidth = 20*20
                if i[0].count("w")>5:statwidth = 20*20
                if i[2]>chatlst[num-1][2]:
                    ycounter.append(ycounter[num-1]+50*len(word_lststatn)+20)
                    ycounter = [i for n, i in enumerate(ycounter) if i not in ycounter[:n]] 
                pygame.draw.rect(screen, 
                                    (0, 0, 0), 
                                    (10, 
                                    ycounter[num]-scroller, 
                                    statwidth, 
                                    50*len(word_lststat)+10))
                count = 0
                for j in word_lststat:
                    create(j, 10, int(ycounter[num]+count+25-scroller), 50, (0, 0, 0), (255, 255, 255))
                    count+=50
            if num==len(chatlst)-1:
                lastval = i
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    Database.write(chatlst)
                    pygame.quit()
                    exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==4:
                    if ycounter[0]-scroller<10:
                        scroller-=30
                        auto = False
                if event.button==5:
                    if ycounter[len(ycounter)-1]-scroller+50*len(lastval)+10*len(ycounter)+25>550:
                        scroller+=30
                        auto = False
            chatlst, string, initial_y, auto, n = get(chatlst, string, initial_y, auto, n)
        pygame.draw.rect(screen, (0, 0, 0), (-10, initial_y-31, 530, 560), 1)
        pygame.draw.rect(screen, (255, 255, 255), (-1, initial_y-30, 500, 560))
        if string.count("m")>6:wrapper = textwrap.TextWrapper(width=17) 
        if string.count("w")>6:wrapper = textwrap.TextWrapper(width=17) 
        else:wrapper = textwrap.TextWrapper(width=25) 
        word_list = wrapper.wrap(text=string)
        for i in word_list:
            if initial_y+x>540:
                initial_y-=50
            if initial_y+x<540 and write==True:
                initial_y+=50
            create(i, 0, initial_y+x, 50, (255, 255, 255), (0, 0, 0))
            create(i, 0, initial_y+x, 50, (255, 255, 255), (0, 0, 0))
            x+=50
        pygame.display.flip()
        x = 0
if __name__=='__main__':
    main()
