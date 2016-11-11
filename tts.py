#pico for now
import var
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

