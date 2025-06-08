import sys

if sys.platform == 'win32':
    # On Windows, re-export winloop as uvloop
    from winloop import *
else:
    # On non-Windows, re-export the real uvloop
    from uvloop import *  # This imports the actual uvloop package