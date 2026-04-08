"""
Author: Gaby White
Learning Pygame
""" 

import pygame
from pygame import *
from engine import GameEngine
from vector import vec, pyVec
from constants import *
from button import Button
from drawable import Drawable
from os.path import join
import random
from images import *
from text import TextEntry
import textwrap
from soundManager import SoundManager

def main():
    #Initialize the module
    pygame.init()
    
    pygame.font.init()
    
    #Get the screen
    screen = pygame.display.set_mode(UPSCALED)
    drawSurface = pygame.Surface(RESOLUTION)

    STATE = "start"

    ENERGY = 10
    
    gameEngine = GameEngine()
    
    gameClock = pygame.time.Clock()

    outcome = ""

    GPA = 2.0
    STRESS = 0
    HAPPINESS = 0
    POPULARITY = 0
    OG = 2.0
    OH = 0
    OS = 0
    OP = 0
    YEAR = 1
    MONTH = 1

    BLACK = (0, 0, 0)

    text = TextEntry(vec(0,0), outcome)
    textGPA = TextEntry(vec(0,0), ("GPA: " + str(GPA)))
    textHAPPINESS = TextEntry(vec(0,0), ("HAPPINESS: " + str(HAPPINESS)))
    textPOPULARITY = TextEntry(vec(0,0), ("POPULARITY: " + str(POPULARITY)))
    textSTRESS = TextEntry(vec(0,0), ("STRESS: " + str(STRESS)))
    
    RUNNING = True
    sm = SoundManager.getInstance()

    sm.playBGM("music.mp3")
    
    while RUNNING:

        drawSurface.fill((255,255,255))
        gameEngine.draw(drawSurface)

        if STATE == 'gameplay' :
            BAR.draw(drawSurface)
            PLAY.draw(drawSurface)
            MENU.draw(drawSurface)
            ARROW1.draw(drawSurface)
            ARROW2.draw(drawSurface)
            SCROLLBAR.draw(drawSurface)
            date = TextEntry(vec(0,0), ("Year " + str(YEAR) + ", Month " + str(MONTH)))
            date.position = vec(2,2)
            date.draw(drawSurface)
            for button in BUTTONS :
                button.draw(drawSurface)
            for i in range(ENERGY) :
                ENERGYUNITS[i].draw(drawSurface)
        
        elif STATE == "end" :
            if GPA < 1 :
                letter = Button(vec(0,0), "ending0.png")
            elif GPA > 3.7 and HAPPINESS < 2 :
                letter = Button(vec(0,0), "ending2.png")
            elif GPA > 3.7 and POPULARITY < 2 :
                letter = Button(vec(0,0), "ending3.png")
            elif 3.5 > GPA > 2.5 and 4 <= POPULARITY <= 6 :
                letter = Button(vec(0,0), "ending5.png")
            elif GPA < 2.5 and POPULARITY > 7 :
                letter = Button(vec(0,0), "ending6.png")
            elif HAPPINESS >= 8 :
                letter = Button(vec(0,0), "ending7.png")
            elif STRESS >= 8 :
                letter = Button(vec(0,0), "ending8.png")
            elif POPULARITY > 7 and STRESS < 3 :
                letter = Button(vec(0,0), "ending9.png")
            else :
                letter = Button(vec(0,0), "ending4.png")
            letter.draw(drawSurface)
            NEXT.draw(drawSurface)

        elif STATE == 'start' :
            intro = Button(vec(100,50), "intro.png")
            intro.draw(drawSurface)
            START.draw(drawSurface)
        
        elif STATE == 'letter' :
            letter = Button(vec(0,0), "letter.png")
            letter.draw(drawSurface)
            NEXT.draw(drawSurface)

        elif STATE == 'stats' :

            str_g = f"{GPA:.2f}"
            if OG > GPA :
                textGPA = TextEntry(vec(0,0), ("GPA: "+ str_g), font="default24", color=(255, 0, 0))
            elif OG < GPA :
                textGPA = TextEntry(vec(0,0), ("GPA: "+ str_g), font="default24", color=(0, 255, 0))
            else :
                textGPA = TextEntry(vec(0,0), ("GPA: "+ str_g), font="default24")
            textGPA.position = vec(150,100)

            str_h = f"{HAPPINESS:.0f}"
            if OH > HAPPINESS :
                textHAPPINESS = TextEntry(vec(0,0), ("HAPPINESS: " + str_h), font="default24", color=(255,0,0))
            elif OH < HAPPINESS :
                textHAPPINESS = TextEntry(vec(0,0), ("HAPPINESS: " + str_h), font="default24", color=(0,255,0))
            else :
                textHAPPINESS = TextEntry(vec(0,0), ("HAPPINESS: " + str_h), font="default24")
            textHAPPINESS.position = vec(150,150)

            str_s = f"{STRESS:.0f}"
            if OS > STRESS :
                textSTRESS = TextEntry(vec(0,0), ("STRESS: " + str_s), font="default24", color=(255,0,0))
            elif OS < STRESS :
                textSTRESS = TextEntry(vec(0,0), ("STRESS: " + str_s), font="default24", color=(0,255,0))
            else :
                textSTRESS = TextEntry(vec(0,0), ("STRESS: " + str_s), font="default24")
            textSTRESS.position = vec(150,200)

            str_p = f"{POPULARITY:.0f}"
            if OP > POPULARITY :
                textPOPULARITY = TextEntry(vec(0,0), ("POPULARITY: " + str_p), font="default24", color=(255, 0,0))
            elif OP < POPULARITY :
                textPOPULARITY = TextEntry(vec(0,0), ("POPULARITY: " + str_p), font="default24", color=(0,255,0))
            else :
                textPOPULARITY = TextEntry(vec(0,0), ("POPULARITY: " + str_p), font="default24")
            textPOPULARITY.position = vec(150,250)

            textGPA.draw(drawSurface)
            textHAPPINESS.draw(drawSurface)
            textSTRESS.draw(drawSurface)
            textPOPULARITY.draw(drawSurface)

            text = TextEntry(vec(0,0), "YEAR " + str(YEAR) + ", MONTH " + str(MONTH) + " STATS", font="default24" )
            text.position = vec(10,30)
            text.draw(drawSurface)
            NEXT.draw(drawSurface)

        elif STATE == 'summary' :
            for button in BUTTONS :
                if button.clicked and not button.playType :
                    if button.id == 1 :
                        OS = STRESS
                        OH = HAPPINESS
                        STRESS += random.random()
                        HAPPINESS += random.random()
                        outcome += "After looking around the club fair, you decided to join the dance club. You have learned all the fresh moves to show your friends! "
                    if button.id == 2 :
                        OH = HAPPINESS
                        HAPPINESS += random.random()
                        outcome += "The number in your bank may be going down quickly, but your energy is through the roof! All the caffeine in those coffees are making it hard to sit still in class, but at least you do all of your homework quickly. "
                    if button.id == 3 :
                        OH = HAPPINESS
                        OP = POPULARITY
                        HAPPINESS += random.random()
                        POPULARITY += random.random()
                        outcome += "While in one of your classes, you get a Snapchat notification from an someone asking to grab dinner. You decide to go, if not for the comany, for the free meal. "
                    if button.id == 4 :
                        OH = HAPPINESS
                        HAPPINESS += random.random()
                        outcome += "With all the madness of your first month in college, you sure do need to stay fueled! And it doesn't hurt that the dining hall always has ice cream. "
                    if button.id == 5 :
                        OH = HAPPINESS
                        OP = POPULARITY
                        HAPPINESS += random.random()
                        POPULARITY += random.random()
                        outcome += "You decide to branch out during lunch one day and sit with a random table. They welcome you in and even invite you to a party that night."
                    if button.id == 6 :
                        outcome += "College is tiring... sometimes all you need is a little mid-day rest to keep your productivity high. "
                    if button.id == 7 :
                        OS = STRESS
                        OG = GPA
                        STRESS += random.random()
                        GPA += random.random()
                        outcome += "To keep grades up, and make sure your GPA if up, you head over to office hours every week. But the professors not only are helping you when struggling, it also is boosting your participation grade. "
                    if button.id == 8 :
                        OS = STRESS
                        OG = GPA
                        OH = HAPPINESS
                        OP = POPULARITY
                        STRESS -= random.random()
                        GPA -= random.random()
                        HAPPINESS += random.random()
                        POPULARITY += random.random()
                        outcome += "School is fun, sure. But the real point of college is to party. Hard. You truly know the meaning of 'play hard', but the 'work hard' part is still up for debate. "
                    if button.id == 9 :
                        OG = GPA
                        GPA -= random.random()
                        outcome += "Sometimes, all you need is mind numbing doomscrolling to lift your mood. Looking back at all the memories you made during your first month, you are excited to keep the whirlwind going. "
                    if button.id == 10 :
                        OG = GPA
                        OS = STRESS
                        STRESS += random.random()
                        GPA += random.random()
                        outcome += "Time to hit the books with midterms coming up. You need the 4.0 to stay a 4.0, and the library has become one of your best friends to accomplish that. "
                    if button.id == 11 :
                        OS = STRESS
                        OG = GPA
                        OH = HAPPINESS
                        HAPPINESS += random.random()
                        STRESS += random.random()
                        GPA += random.random()
                        outcome += "A break from studying gives you the perfect time to go out and help the local community. Doesn't hurt that your biology professor happens to be there every Saturday too. "
                    if button.id == 12 :
                        OH = HAPPINESS
                        OS = STRESS
                        HAPPINESS += random.random()
                        STRESS -= random.random()
                        outcome += "It is bulking season. For your mind, for your soul, and most importantly, for your body. To be the best in class, you need to be your best physically. "
                    button.clicked = False
            if HAPPINESS < 0 :
                HAPPINESS = 0
            if GPA < 0 :
                GPA = 0
            if GPA > 4.0 :
                GPA = 4.0
            if POPULARITY < 0 :
                POPULARITY = 0
            if STRESS < 0 :
                STRESS = 0
            ENERGY = 10
            # textNew = textwrap.fill(outcome, 15)
            words = outcome.split(' ')
            lines = []
            lineCurrent = ""
            line = ""
            for word in words :
                line = lineCurrent + word + " "
                if len(line) < 58 :
                    lineCurrent = line 
                else :
                    lines.append(line)
                    lineCurrent = ""
            
            lines.append(line)

            x, y = 10, 100
            for line in lines :
                text = TextEntry(vec(0,0), line)
                text.position = vec(x,y)
                text.draw(drawSurface)
                y += 25
            text = TextEntry(vec(0,0), "YEAR " + str(YEAR) + ", MONTH " + str(MONTH) + " RECAP", font="default24" )
            text.position = vec(10,30)
            text.draw(drawSurface)
            NEXT.draw(drawSurface)
        
        pygame.transform.scale(drawSurface,
                               pyVec(UPSCALED),
                               screen)
     
        pygame.display.flip()

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_position = event.pos
                if START.getCollisionRect().collidepoint(event.pos) and STATE == 'start':
                    STATE = "letter"
                elif NEXT.getCollisionRect().collidepoint(event.pos) and STATE == 'letter':
                    STATE = "gameplay"
                elif STATE == "gameplay" and not PLAY.getCollisionRect().collidepoint(event.pos):
                    for button in BUTTONS :
                        b_pos = button.getCollisionRect()
                        if button.getCollisionRect().collidepoint(event.pos) :
                            if button.clicked and not button.playType and not button.scrollType :
                                ENERGY += button.energy
                                button.clicked = False
                                button.handleEvent(event)
                            elif not button.clicked and not button.playType and not button.scrollType :
                                ENERGY -= button.energy
                                if ENERGY < 0 :
                                    sm.playSFX("wrong.mp3")
                                    ENERGY += button.energy
                                    button.clicked = False
                                    button.handleEvent(event)
                                else :
                                    sm.playSFX("good.mp3")
                                    button.clicked = True
                                    button.handleEvent(event)
                elif PLAY.getCollisionRect().collidepoint(event.pos) and STATE == 'gameplay':
                    STATE = "summary"

                elif ARROW1.getCollisionRect().collidepoint(event.pos) :
                    if CLICK == 0 :
                        SCROLLBAR.position = vec(0,0)
                    elif CLICK == 1 :
                        SCROLLBAR.position = vec(0,100) 
                    elif CLICK == 2 :
                        SCROLLBAR.position = vec(0,200)
                    elif CLICK == 3 :
                        SCROLLBAR.position = vec(0,300)

                    ARROW1.handleEvent(event)

                elif ARROW2.getCollisionRect().collidepoint(event.pos) :
                    if CLICK == 0 :
                        SCROLLBAR.position = vec(0,0)
                    elif CLICK == 1 :
                        SCROLLBAR.position = vec(0,100) 
                    elif CLICK == 2 :
                        SCROLLBAR.position = vec(0,200)
                    elif CLICK == 3 :
                        SCROLLBAR.position = vec(0,300)
                        
                    ARROW2.handleEvent(event)

                elif NEXT.getCollisionRect().collidepoint(event.pos) and STATE == 'summary' :
                    STATE = "stats"
                elif NEXT.getCollisionRect().collidepoint(event.pos) and STATE == 'stats' :
                    outcome = ''
                    for button in BUTTONS :
                        button.clicked = False
                    if MONTH <= 6 and GPA > 1:
                        MONTH += 1
                        STATE = "gameplay"
                    elif YEAR <= 3 and GPA > 1: 
                        YEAR += 1
                        MONTH = 1
                        STATE = "gameplay"
                    else :
                        YEAR = 1
                        MONTH = 1
                        STATE = "end" 
                elif NEXT.getCollisionRect().collidepoint(event.pos) and STATE == 'end' :
                    GPA = 2.0
                    STRESS = 0
                    POPULARITY = 0
                    HAPPINESS = 0
                    STATE = "start"

            gameEngine.handleEvent(event)
        
        gameClock.tick(60)
        seconds = gameClock.get_time() / 1000
        gameEngine.update(seconds)

        if STATE == 'gameplay' :
            for button in BUTTONS :
                button.update(seconds)
            BAR.update(seconds)
            PLAY.update(seconds)
            MENU.update(seconds)
            ARROW1.update(seconds)
            ARROW2.update(seconds)
            SCROLLBAR.update(seconds)
            for unit in ENERGYUNITS :
                unit.update(seconds)
        elif STATE == "start" :
            START.update(seconds)
        elif STATE == "summary" :
            text.update(seconds)
            NEXT.update(seconds)
        elif STATE == "stats" :
            textGPA.update(seconds)
            textHAPPINESS.update(seconds)
            textPOPULARITY.update(seconds)
            textSTRESS.update(seconds)
            NEXT.update(seconds)
        elif STATE == "letter" :
            NEXT.update(seconds)
        
        
    pygame.quit()


if __name__ == '__main__':
    main()