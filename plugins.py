#basic plugin system
import os
import sys
import var
 
path = var.plugin_path
var.plugins = {}
 
# load plugins
def load():
    sys.path.insert(0, path)
    for f in os.listdir(path):
        fname, ext = os.path.splitext(f)
        if ext == '.py':
            if (var.debug):
                print("Load plugin "+fname)
            mod = __import__(fname)
            var.plugins[fname] = mod.Plugin()
    sys.path.pop(0)
 
#for var.plugin in var.plugins.values():
    #var.plugin.run()