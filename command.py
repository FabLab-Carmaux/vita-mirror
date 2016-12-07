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
