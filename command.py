"""
command :
type display, light, external command, ...
"""

import var

debug=var.debug


def external_url(url):
    """
    call external url
    """
    print("call "+url)
