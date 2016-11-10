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


    import speech_recognition as sr

    # this is called from the background thread
    def callback(recognizer, audio):
        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            text = recognizer.recognize_bing(audio, var.stt_api_key,var.stt_lang)
            print("BING Speech Recognition thinks you said " + text)
            if (text == var.stt_keyword):
                var.keyword_ok=True
            else:
                var.keyword_ok=False
        except sr.UnknownValueError:
            print("BING Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could no request results from BING Speech Recognition service; {0}".format(e))

    r = sr.Recognizer()
    m = sr.Microphone(2)
    with m as source:
        r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

    stop_listening = r.listen_in_background(m, callback)
