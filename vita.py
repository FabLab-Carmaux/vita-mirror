"""

VITA is my personal assistant 

"""

import var

import sensor
import command
import sst


var.keyword_ok = False

def main():
    """Main prog"""
    #init default sensors
    sens = sensor.Sensor()
    
    debug=var.debug
    #load and init plugins
   
    done=False    
    
    wk = sst.Keyword()
    wk.start()

    
    #main loop
    while not done:
        #waiting someone in front or IR sensor
        if (sens.is_someone==True or var.keyword_ok==True):
            #someone is here
            #so we try to recognise him/her and ask what to do
            #if recognise
            #speak to recognised people
            command.say("hello brice")
            #else speak to unknown
            
            wk.join()
            wk.close()
            
            #after delay without more restart thread
        else:
            #sleep mode ?
            if (debug):
                print("no one")
            
        if (debug):
            print("loop")


    exit()
if __name__ == '__main__':
    main()