#!/usr/bin/env python
# title           : VITA
# description     : personal assistant for smart and connected mirror
# author          : CB2 Ltd.
# date            : 2016
# version         : 0.1.1
# notes           : www.vita.com
# license         : vita open source license
# python_version  : 2
#==============================================================================

# TODO LIST
# 1) 
# 2) 

import logging
import time
import sys
import plugins
import pygame
import ConfigParser

import var
import sensor
import command
import stt
import tts


var.keyword_ok = False

def main():

    ## Configuration file parsing

    configParser = ConfigParser.RawConfigParser()
    configParser.read('vita.conf')

    coreName = configParser.get('Identification', 'CORE_NAME')
    coreVersion = configParser.get('Identification', 'CORE_VERSION')

    logFileName = configParser.get('Logger', 'LOG_FILENAME')
    logFormat = configParser.get('Logger', 'LOG_FORMAT')
    logDateFormat = configParser.get('Logger', 'LOG_DATE_FORMAT')
    logPropagate = configParser.get('Logger', 'LOG_PROPAGATE').lower() in ("yes", "true")

    logLevelDict = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING, 'error': logging.ERROR, 'critical': logging.CRITICAL}
    logLevel = logLevelDict[configParser.get('Logger', 'LOG_LEVEL').lower()]

    ## logger initialization

    logFileName = 'log/' + time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime()) + '_' + logFileName

    logging.basicConfig(filename=logFileName, format=logFormat, datefmt=logDateFormat, level=logLevel)
    logging.propagate = logPropagate

    logging.info('****************************************************************************************')
    logging.info('START CORE ' + coreName + ' v' + coreVersion)

    logging.debug('sys.maxint = ' + str(sys.maxint))
    logging.debug('sys.argv = ' + str(sys.argv))
    logging.debug('sys.path = ' + str(sys.path))
    logging.debug('sys.platform = ' + str(sys.platform))
    logging.debug('sys.version = ' + str(sys.version))
    logging.debug('sys.api_version = ' + str(sys.api_version))
    logging.debug('sys.version_info = ' + str(sys.version_info))

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

        logging.info('STOP ' + coreName + ' v' + coreVersion)

    exit()
if __name__ == '__main__':
    main()

