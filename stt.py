#bing speech api for now
import var
import speech_recognition as sr

    
class Stt():


    """
    This class waiting keyword or a sentence
    """
    def __init__(self, type):
        r = sr.Recognizer()
        #TODO webcam hack pc
        m = sr.Microphone(sample_rate = 44100, chunk_size = 512)
        with m as source:
            r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening
        if (type=="keyword"):
            self.stop_listening = r.listen_in_background(m, self.keyword_callback)
        else:
            self.stop_listening = r.listen_in_background(m, self.sentence_callback)

       


    # this is called from the background thread
    def keyword_callback(self, recognizer, audio):
        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            text = recognizer.recognize_bing(audio, var.stt_api_key,var.stt_lang)
            if (var.debug==True):
                print("BING Speech Recognition thinks you said " + text)
            if (text == var.stt_keyword):
                var.keyword_ok=True
            else:
                var.keyword_ok=False
        except sr.UnknownValueError:
            #TODO prevoir logs
            print("BING Speech Recognition could not understand audio")
        except sr.RequestError as e:
            #TODO prevoir logs
            print("Could no request results from BING Speech Recognition service; {0}".format(e))

            
    # this is called from the background thread
    def sentence_callback(self, recognizer, audio):
        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            var.sentence = recognizer.recognize_bing(audio, var.stt_api_key,var.stt_lang)
            if (var.debug==True):
                print("BING Speech Recognition thinks you said " + var.sentence)
           
        except sr.UnknownValueError:
            #TODO prevoir logs
            print("BING Speech Recognition could not understand audio")
        except sr.RequestError as e:
            #TODO prevoir logs
            print("Could no request results from BING Speech Recognition service; {0}".format(e))
            
    def stop(self):
        self.stop_listening()

        
 
