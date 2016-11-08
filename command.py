"""
command :
type display, light, external command, say ...
"""

import var

debug=var.debug


def say(text):
    """
    use pico tts to speak
    """
    if (debug):
        print("say "+text)
    
def external_url(url):
    """
    call external url
    """
    print("call "+url)