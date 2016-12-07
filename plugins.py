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

#basic plugin system
import os
import sys
import var
import logging

 
global plugins


# load plugins
def load(path):
    plugins = {}
    sys.path.insert(0, path)
    for f in os.listdir(path):
        fname, ext = os.path.splitext(f)
        if ext == '.py':
            logging.debug('Load plugin ' + fname)
            mod = __import__(fname)
            plugins[fname] = mod.Plugin()
    sys.path.pop(0)
 
#for var.plugin in var.plugins.values():
    #var.plugin.run()