"""

VITA is my personal assistant 

"""

import var
import plugins
import sensor
import command
import sst


var.keyword_ok = False

def main():
    """Main prog"""
    
    #load plugins
    plugins.load()
    #init default sensors
    sens = sensor.Sensor()
    
    debug=var.debug
    #load and init plugins
   
    done=False    
    
    wk = sst.Keyword()
    wk.start()

    
    #main loop
    while not done:
        #waiting someone in front or IR sensor or someone saying magical word
        if (sens.is_someone==True or var.keyword_ok==True):
            #someone is here
            #so we try to recognise him/her with camera and ask what to do
            #if recognise
            #speak to recognised people
            #command.say("hello you")
            #else speak to unknown
            
            
            
            wk.join()

            
            #after delay without more restart thread
        #else:
            #sleep mode ?
            #if (debug):
            #    print("no one")
            


    exit()
if __name__ == '__main__':
    main()