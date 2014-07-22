#!/usr/bin/env python
# kastoro (c) Jrabbit (Jack Laxson) released under gpl v3



#temporary settings until commandline option lib is chosen.
turn_off_logging = True
delete_existing_logs = False

def disable_empathy():
    try:
        from gi.repository import Gio
    except ImportError:
        print "Currently targeting GTK."
    log_setting = Gio.Settings.new("org.freedesktop.Telepathy.Logger")
    if not log_setting.get_boolean("enabled"):
        #Then we're done already
        return True
    

def disable_logs(all, *args, **kawargs):
    pass

def delete_logs(all, *args, **kwargs):
    pass

def main():
    if turn_off_logging:
        disable_logs()
    if delete_existing_logs:    
        delete_logs()

if __name__ == '__main__':
    main()