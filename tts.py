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

#pico for now
import var
import logging
import subprocess
import os
import sys
 
class Tts():

    def __init__(self):
	self.tmpfile="/tmp/tmp.wav"

    def say(self,text):
        devnull = open("/dev/null","w")
        subprocess.call(["pico2wave",  "-l" , var.tts_lang, "-w" , self.tmpfile, text],stderr=devnull)
        subprocess.call(["aplay", self.tmpfile],stderr=devnull)
        os.remove(self.tmpfile)

