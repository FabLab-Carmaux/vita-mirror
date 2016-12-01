"""

VITA is my personal assistant 

"""

import var
import plugins
import sensor
import command
import stt
import tts

import pygame

var.keyword_ok = False

def main():
    """Main prog"""
    
    #load plugins
    plugins.load()
    #init default sensors
    sens = sensor.Sensor()
    
    debug=var.debug
   
    done=False    
    
    wk=stt.Stt("keyword")
    voice=tts.Tts()
    voice.say("vita fait pouet pouet")

    #pygame init
    pygame.init()
    screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
    pygame.mouse.set_visible(0)

    font = pygame.font.SysFont("dejavusansmono",72)
    text = font.render("", True, (250, 250, 250))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    done = False
    
    #main loop
    while not done:
        screen.blit(background, (0, 0))
        #waiting someone in front or IR sensor or someone saying magical word
        if (sens.is_someone==True or var.keyword_ok==True):
            var.keyword_ok = False
            wk.stop()
            #someone is here
            #so we try to recognise him/her with camera and ask what to do
            #if recognise
            #speak to recognised people
            voice.say("bonjour brice")
            text = font.render("Bonjour", True, (250, 250, 250))
            wk=stt.Stt("keyword")
            #else speak to unknown
            
            wk.stop()
            

            
            #after delay without more restart thread
        #else:
            #sleep mode ?
            #if (debug):
            #    print("no one")
            
        screen.blit(text,((pygame.display.Info().current_w/2)-(text.get_width()/2),(pygame.display.Info().current_h/2)-(text.get_height()/2)))
        pygame.display.flip()

    exit()
if __name__ == '__main__':
    main()
