#bing speech api for now
import var
import sys
import time
import speech_recognition as sr
import threading

class Keyword(threading.Thread):

    
    """
    This class waiting keywork to ask me something
    """

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        """
        wait the magic word
        """
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Microsoft Bing Voice Recognition
        try:
            text = r.recognize_bing(audio, key=var.sst_api_key)
            if (text == var.sst_keyword):
                return True
            else:
                print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=var.sst_api_key), var.sst_lang)
                return False
        except sr.UnknownValueError:
            print("Microsoft Bing Voice Recognition could not understand audio")
            return False
        except sr.RequestError as e:
            print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
            return False