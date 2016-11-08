#bing speech api for now
import var
import sys
import time

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
        time.sleep(5)
        #magic word is here so True
        var.keyword_ok=True


