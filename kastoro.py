#!/usr/bin/env python
# kastoro (c) Jrabbit (Jack Laxson) released under gpl v3
import shutil
import os.path
#temporary settings until commandline option lib is chosen.
turn_off_logging = True
delete_existing_logs = False


#utilities
def delete_directory(nice_path):
    """Take expandable path. Deletes folder and paths below"""
    #translate ~ and any weird vars
    path = os.path.expandvars(os.path.expanduser(nice_path))
    shutil.rmtree(path)

class Empathy(object):
    needs_GIO = True
    needs_augeas = False
    def disable():
        try:
            from gi.repository import Gio
        except ImportError:
            print "Currently targeting GTK."

        log_setting = Gio.Settings.new("org.freedesktop.Telepathy.Logger")
        if not log_setting.get_boolean("enabled"):
            #Then we're done already
            return True
        else:
            log_setting.set_boolean("enabled", False)
            return True
    def delete():
        delete_directory("~/.local/share/TpLogger/logs")

def disable_logs(every, *args, **kawargs):
    if every:
        Empathy.disable()

def delete_logs(every, *args, **kwargs):
    if every:
        Empathy.delete()

def main():
    if turn_off_logging:
        disable_logs(every=True)
    if delete_existing_logs:    
        delete_logs()

if __name__ == '__main__':
    main()